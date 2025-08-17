from fastapi import APIRouter
from app.services import prediction_service
from app.services.prediction_service import PredictionInput, PredictionOutput

router = APIRouter(
    prefix="/predict",
    tags=["Prediction - 预测"],
)

@router.post("/flood_drought", response_model=PredictionOutput)
async def predict_flood_drought(data: PredictionInput):
    """
    接收水文数据并返回洪水或干旱风险预测。
    - **rainfall_mm**: 降雨量 (毫米)
    - **river_level_m**: 河流水位 (米)
    """
    return prediction_service.get_prediction(data)

from fastapi import APIRouter
from app.services import analysis_service
from app.services.analysis_service import WaterQualityInput, WaterQualityOutput

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis - 分析"],
)

@router.post("/water_quality", response_model=WaterQualityOutput)
async def analyze_water_quality(data: WaterQualityInput):
    """
    接收水质参数，返回分析评估和建议。
    - **ph**: pH值
    - **turbidity_ntu**: 浊度 (NTU)
    - **dissolved_oxygen_mg_l**: 溶解氧 (毫克/升)
    """
    return analysis_service.get_analysis(data)

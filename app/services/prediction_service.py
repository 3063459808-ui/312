from pydantic import BaseModel

class PredictionInput(BaseModel):
    rainfall_mm: float
    river_level_m: float

class PredictionOutput(BaseModel):
    risk_level: str
    message: str

def get_prediction(data: PredictionInput) -> PredictionOutput:
    """
    一个模拟的洪水/干旱预测函数。
    真实的实现需要复杂的模型和大量数据。
    """
    if data.rainfall_mm > 50 and data.river_level_m > 3.0:
        return PredictionOutput(
            risk_level="高 (High)",
            message="预测：未来24小时内有高洪水风险。"
        )
    elif data.rainfall_mm < 5 and data.river_level_m < 0.5:
        return PredictionOutput(
            risk_level="中 (Medium)",
            message="预测：未来一周内有干旱风险。"
        )
    else:
        return PredictionOutput(
            risk_level="低 (Low)",
            message="预测：当前水文状况稳定。"
        )

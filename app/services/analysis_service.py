from pydantic import BaseModel
from typing import List

class WaterQualityInput(BaseModel):
    ph: float
    turbidity_ntu: float
    dissolved_oxygen_mg_l: float

class WaterQualityOutput(BaseModel):
    assessment: str
    recommendations: List[str]

def get_analysis(data: WaterQualityInput) -> WaterQualityOutput:
    """
    一个模拟的水质数据分析函数。
    真实的实现需要专业的标准和阈值。
    """
    recommendations = []
    assessment = "水质良好 (Good)"

    if not (6.5 <= data.ph <= 8.5):
        assessment = "水质异常 (Abnormal)"
        recommendations.append("pH值异常，建议调查污染源。")

    if data.turbidity_ntu > 5.0:
        assessment = "水质异常 (Abnormal)"
        recommendations.append("浊度过高，可能存在悬浮物污染。")

    if data.dissolved_oxygen_mg_l < 4.0:
        assessment = "水质异常 (Abnormal)"
        recommendations.append("溶解氧过低，可能对水生生物构成威胁。")

    if not recommendations:
        recommendations.append("未发现显著问题。")

    return WaterQualityOutput(
        assessment=assessment,
        recommendations=recommendations
    )

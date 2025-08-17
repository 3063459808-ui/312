from pydantic import BaseModel

class OptimizationInput(BaseModel):
    reservoir_level_m: float
    downstream_demand_m3_s: float
    inflow_m3_s: float

class OptimizationOutput(BaseModel):
    outflow_m3_s: float
    message: str

def get_optimization(data: OptimizationInput) -> OptimizationOutput:
    """
    一个模拟的水库调度优化函数。
    真实的实现需要运筹学模型和实时数据。
    """
    # 简单的逻辑：尽量匹配下游需水，但要考虑水位
    target_outflow = data.downstream_demand_m3_s

    if data.reservoir_level_m > 100: # 假设100米是警戒水位
        # 水位太高，需要加大下泄流量
        target_outflow = data.inflow_m3_s * 1.2
        message = "建议：水位过高，增加下泄流量以防洪。"
    elif data.reservoir_level_m < 70: # 假设70米是死水位
        # 水位太低，需要减少下泄流量
        target_outflow = data.inflow_m3_s * 0.8
        message = "建议：水位过低，减少下泄流量以蓄水。"
    else:
        message = "建议：调度方案正常，满足下游需求。"


    return OptimizationOutput(
        outflow_m3_s=round(target_outflow, 2),
        message=message
    )

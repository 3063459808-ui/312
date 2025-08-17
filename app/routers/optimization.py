from fastapi import APIRouter
from app.services import optimization_service
from app.services.optimization_service import OptimizationInput, OptimizationOutput

router = APIRouter(
    prefix="/optimize",
    tags=["Optimization - 优化"],
)

@router.post("/reservoir_dispatch", response_model=OptimizationOutput)
async def optimize_reservoir_dispatch(data: OptimizationInput):
    """
    接收水库和需水数据，返回建议的调度方案。
    - **reservoir_level_m**: 当前水库水位 (米)
    - **downstream_demand_m3_s**: 下游需水量 (立方米/秒)
    - **inflow_m3_s**: 水库入流量 (立方米/秒)
    """
    return optimization_service.get_optimization(data)

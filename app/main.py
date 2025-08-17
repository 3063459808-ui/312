from fastapi import FastAPI

app = FastAPI(
    title="水利AI助手 (Water Conservancy AI Agent)",
    description="一个用于辅助水利工程师工作的AI工具，具备洪水预测、水库调度优化和水质分析等功能。",
    version="0.1.0",
)

# 引入API路由
from .routers import prediction, optimization, analysis

app.include_router(prediction.router)
app.include_router(optimization.router)
app.include_router(analysis.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "欢迎使用水利AI助手 (Welcome to the Water Conservancy AI Agent)"}

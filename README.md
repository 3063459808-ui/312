# 水利AI助手 (Water Conservancy AI Agent)

这是一个用于辅助水利工程师工作的AI工具，旨在提供洪水预测、水库调度优化和水质分析等功能。

本项目当前为一个基础框架，核心业务逻辑由占位符函数模拟。

## 项目结构

```
/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI 应用主文件
│   ├── services/               # 核心业务逻辑
│   │   ├── prediction_service.py
│   │   ├── optimization_service.py
│   │   └── analysis_service.py
│   └── routers/                # API 路由
│       ├── prediction.py
│       ├── optimization.py
│       └── analysis.py
├── requirements.txt            # Python 依赖
└── README.md                   # 项目说明
```

## 如何运行

1.  **安装依赖:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **启动应用:**
    ```bash
    uvicorn app.main:app --reload
    ```
    应用将在 `http://127.0.0.1:8000` 运行。

3.  **API 文档:**
    访问 `http://127.0.0.1:8000/docs` 可以查看和测试所有API接口。

## 如何开发

当前的核心功能位于 `app/services/` 目录中，均为模拟函数。

要将本项目用于实际生产，你需要：

1.  **收集数据:** 为每个功能（预测、优化、分析）收集大量的历史和实时数据。
2.  **训练模型:** 使用机器学习、深度学习或运筹学方法，根据收集到的数据训练模型。
3.  **替换占位符:**
    *   将你训练好的模型文件（例如 `.pkl`, `.h5` 等格式）保存在项目中（建议新建一个 `models` 目录）。
    *   修改 `app/services/` 中的相应服务文件，加载你的模型，并用模型的推理结果替换掉当前的模拟逻辑。

例如，在 `prediction_service.py` 中，你可以将 `get_prediction` 函数修改为：

```python
# from your_model_library import load_model # 伪代码

# model = load_model("models/flood_prediction_model.pkl") # 伪代码

def get_prediction(data: PredictionInput) -> PredictionOutput:
    # 1. 对输入数据进行预处理 (伪代码)
    # processed_data = preprocess(data)

    # 2. 使用模型进行预测 (伪代码)
    # prediction_result = model.predict(processed_data)

    # 3. 格式化输出 (伪代码)
    # return format_output(prediction_result)

    # ... 以下是当前占位符逻辑，需要被替换
    if data.rainfall_mm > 50 and data.river_level_m > 3.0:
        # ...
```

## API 概览

- `POST /predict/flood_drought`: 洪水/干旱预测
- `POST /optimize/reservoir_dispatch`: 水库调度优化
- `POST /analyze/water_quality`: 水质分析

详情请参阅 [API 文档](http://127.0.0.1:8000/docs)。

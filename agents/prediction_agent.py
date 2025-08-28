from .base_agent import BaseAgent

class PredictionAgent(BaseAgent):
    """
    一个专门用于预测的Agent。
    在当前版本中，它只返回固定的、模拟的预测数据。
    """
    def perceive(self, environment_state: dict) -> None:
        """
        对于这个简单的占位符Agent，我们暂时不需要感知任何外部状态。
        我们只是记录一下收到的环境信息（虽然并未使用）。
        """
        self.state['last_environment_state'] = environment_state
        print(f"[{self.name}] 感知到环境状态: {environment_state}")

    def act(self) -> dict:
        """
        执行“预测”动作，返回一个包含模拟数据的字典。
        在真实的实现中，这里会运行一个复杂的模型（例如MLP或调用大模型API）。
        """
        print(f"[{self.name}] 正在执行预测动作...")

        # 模拟的预测结果
        prediction_result = {
            "predicted_inflow_m3_s": [100, 110, 120, 115, 105], # 预测未来5个时间步的入库流量
            "predicted_rainfall_mm": [5, 2, 0, 1, 3], # 预测未来5个时间步的降雨量
            "confidence": 0.85
        }

        print(f"[{self.name}] 生成预测结果: {prediction_result}")
        return prediction_result

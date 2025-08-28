from .base_agent import BaseAgent

class DemandAgent(BaseAgent):
    """
    一个专门用于预测下游用水需求的Agent。
    在当前版本中，它只返回固定的、模拟的预测数据。
    """
    def perceive(self, environment_state: dict) -> None:
        """
        对于这个简单的占位符Agent，我们暂时不需要感知任何外部状态。
        """
        self.state['last_environment_state'] = environment_state
        print(f"[{self.name}] 感知到环境状态: {environment_state}")

    def act(self) -> dict:
        """
        执行“需求预测”动作，返回一个包含模拟需水量的字典。
        在真实的实现中，这里可能会分析历史数据或社会活动日历。
        """
        print(f"[{self.name}] 正在执行需水预测动作...")

        # 模拟的预测结果
        demand_result = {
            "predicted_demand_m3_s": [80, 85, 90, 88, 82] # 预测未来5个时间步的下游需水量
        }

        print(f"[{self.name}] 生成需水预测结果: {demand_result}")
        return demand_result

from typing import List
from .base_agent import BaseAgent

class MPCAgent(BaseAgent):
    """
    一个作为总指挥的协调Agent。
    它负责从其他Agent收集信息，并做出最终决策。
    """
    def __init__(self, name: str, subordinate_agents: List[BaseAgent]):
        """
        初始化MPC Agent。
        :param name: Agent的名称。
        :param subordinate_agents: 一个包含所有下级Agent的列表。
        """
        super().__init__(name)
        self.subordinate_agents = subordinate_agents

    def perceive(self, environment_state: dict) -> None:
        """
        从所有下级Agent那里收集信息（它们的`act`结果）。
        """
        print(f"[{self.name}] 正在从下级Agent收集信息...")

        # 将每个下级Agent的输出（它们自己的`act`结果）存储到MPC Agent的状态中
        collected_data = {}
        for agent in self.subordinate_agents:
            # 注意：这里我们假设每个下级Agent的名称是唯一的，并用作键
            collected_data[agent.name] = agent.act()

        self.state['collected_data'] = collected_data
        print(f"[{self.name}] 信息收集完成: {self.state['collected_data']}")

    def act(self) -> dict:
        """
        根据收集到的信息，执行“优化决策”动作。
        在当前版本中，这是一个非常简化的决策逻辑。
        """
        print(f"[{self.name}] 正在执行优化决策...")

        # 从状态中获取收集到的数据
        prediction_data = self.state['collected_data'].get('PredictionAgent_1', {})
        demand_data = self.state['collected_data'].get('DemandAgent_1', {})

        # 简化决策逻辑：假设我们只关心第一个时间步的需水，并直接将其作为出流量
        # 在真实的MPC中，这里会是一个复杂的优化计算过程
        try:
            # 获取需求预测列表中的第一个值
            target_outflow = demand_data.get("predicted_demand_m3_s", [0])[0]
        except (IndexError, TypeError):
            target_outflow = 0 # 如果数据格式不正确或为空，则默认为0

        decision = {"optimal_outflow_m3_s": target_outflow}

        print(f"[{self.name}] 生成最终决策: {decision}")
        return decision

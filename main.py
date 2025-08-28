from agents.prediction_agent import PredictionAgent
from agents.demand_agent import DemandAgent
from agents.mpc_agent import MPCAgent

def main():
    """
    主执行函数，用于编排整个多智能体决策流程。
    """
    print("--- 多智能体水利决策系统启动 ---")

    # 1. 初始化所有Agent
    prediction_agent = PredictionAgent(name="PredictionAgent_1")
    demand_agent = DemandAgent(name="DemandAgent_1")

    # MPC Agent需要知道它的下级Agent是谁
    mpc_agent = MPCAgent(name="MPCAgent_1", subordinate_agents=[prediction_agent, demand_agent])

    print("\n--- Agent初始化完成 ---")
    print(f"  - {prediction_agent}")
    print(f"  - {demand_agent}")
    print(f"  - {mpc_agent}")

    # 2. 定义当前的外部环境状态（在这个简单示例中，它可能很简单）
    # 在真实系统中，这可能包含当前的水位、闸门状态等实时数据。
    current_environment = {
        "timestamp": "2025-08-28 00:00:00",
        "current_reservoir_level_m": 125.5
    }

    print(f"\n--- 当前环境状态 --- \n{current_environment}")

    # 3. 编排决策流程

    # a. 首先，让所有专用Agent感知环境（如果它们需要的话）
    #    在我们的例子里，这一步是为了让它们记录最新状态
    print("\n--- 专用Agent感知阶段 ---")
    prediction_agent.perceive(current_environment)
    demand_agent.perceive(current_environment)

    # b. 然后，让MPC协调Agent感知环境
    #    根据我们的设计，它的`perceive`方法会触发它去调用下级Agent的`act`方法来收集信息
    print("\n--- MPC Agent感知与信息收集阶段 ---")
    mpc_agent.perceive(current_environment)

    # c. 最后，让MPC Agent根据它收集到的信息，执行最终的决策动作
    print("\n--- MPC Agent决策阶段 ---")
    final_decision = mpc_agent.act()

    print("\n--- 系统决策完成 ---")
    print(f"最终决策结果: {final_decision}")
    print("--- 系统运行结束 ---")


if __name__ == "__main__":
    main()

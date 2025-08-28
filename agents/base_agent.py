from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    一个所有智能体的抽象基类 (Abstract Base Class)。
    它定义了所有Agent都必须拥有的通用接口。
    """
    def __init__(self, name: str):
        """
        初始化Agent。
        :param name: Agent的唯一名称。
        """
        self.name = name
        self.state = {} # 用于存储Agent的内部状态

    @abstractmethod
    def perceive(self, environment_state: dict) -> None:
        """
        感知环境状态或从其他Agent接收信息。
        这个方法应该用来更新Agent的内部状态。

        :param environment_state: 包含当前环境信息的字典。
        """
        pass

    @abstractmethod
    def act(self) -> dict:
        """
        根据内部状态，执行一个动作并返回结果。

        :return: 一个包含动作或其结果的字典。
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name})>"

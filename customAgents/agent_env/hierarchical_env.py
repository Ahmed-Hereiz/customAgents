from typing import List
from customAgents.agent_env import BaseEnv
from customAgents.agent_routers import BaseRouter
from customAgents.agent_runtime import BaseRuntime


class HierarchialEnv(BaseEnv):
    def __init__(self, agents: List[BaseRuntime], routers: List[BaseRouter] = None):
        super().__init__(agents, routers)
        
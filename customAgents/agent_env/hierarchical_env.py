from typing import List, Union
from customAgents.agent_env import BaseEnv
from customAgents.agent_routers import BaseRouter
from customAgents.agent_runtime import BaseRuntime


class HierarchialEnv(BaseEnv):
    def __init__(self, env_items: Union[List[BaseRuntime], List[BaseRouter]]):
        
        self.env_items = env_items

        super().__init__(agents=None, routers=None)

    def run(self):

        for item in self.env_items:
            if type(item) is BaseRuntime:
                item.loop()
            elif type(item) is BaseRouter:
                item.exec_router()
            elif type(item) is list:
                pass

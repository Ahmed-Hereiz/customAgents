from customAgents.agent_env import BaseEnv

class ReflectionEnv(BaseEnv):
    def __init__(self, agents):
        if len(agents) != 2:
            raise ValueError("Reflection class must be initialized with exactly 2 agents.")
        super().__init__(agents)

    def run(self, num_max_iters=3, verbose_names=True, stop_word="0"):
        agent1 = self.agents[0]
        agent2 = self.agents[1]

        for _ in range(num_max_iters):
            if verbose_names: print("Agent 1 : ")
            agent1_response = agent1.loop()
            if verbose_names: print("\n\nAgent 2 : ")
            agent2.prompt.prompt += agent1_response
            agent2_response = agent2.loop()
            agent1.prompt.prompt += agent2_response
            if verbose_names: print("\n")

            if agent2_response == stop_word:
                ## stop word must be implemented in the prompt
                break

        return agent1_response, agent2_response

    @property
    def agent1(self):
        return self.agents[0]

    @property
    def agent2(self):
        return self.agents[1]
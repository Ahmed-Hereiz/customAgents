class AgentLLMMeta(type):
    def __repr__(cls):
        return "<class 'customAgents.LLM'>"

    def __str__(cls):
        return "<class 'customAgents.LLM'>"

def agent_llm_type(cls):
    return AgentLLMMeta(cls.__name__, cls.__bases__, dict(cls.__dict__))

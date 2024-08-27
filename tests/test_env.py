from customAgents.agent_llm import SimpleStreamLLM
from customAgents.agent_prompt import PlaceHoldersPrompt
from customAgents.agent_tools import SearchTool


from common.utils import load_config, parse_safety_settings
config = load_config(f"../config/llm.json")
safety_settings = parse_safety_settings(config['safety_settings'])


query_prompt_string = """
You are search Assistant llm, your task is to help user where you reformat his query 

user_query : {query}
output : 
"""

query_llm = SimpleStreamLLM(api_key=config['api_key'],model='gemini-1.5-flash',temperature=0.7,safety_settings=safety_settings)

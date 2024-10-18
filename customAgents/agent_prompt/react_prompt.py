from customAgents.agent_prompt import BasePrompt
from typing import Union
from PIL import Image


class ReActPrompt(BasePrompt):
    def __init__(self, question: str, example_workflow: str = "", prompt_string: str = "", img: Union[str, Image.Image, None] = None):
        
        self.example_workflow = example_workflow
        self.question = question

        super().__init__(prompt_string, img)

        self.prompt = self._generate_prompt()
        self.img = self._load_image(img)
        

    def _generate_prompt(self):
        react_prompt = """
{prompt_string}
You are an AI agent designed to answer questions through an iterative process. You have access to the following tools:
{tools_and_role}

IMPORTANT: This is an ITERATIVE PROCESS. You will go through multiple steps before reaching a final answer. Do not try to answer the question immediately.

Follow this format EXACTLY for each iteration:
Thought: [Your reasoning about the current state and what to do next]
Action: [One of: {tool_names}]
Action Input: [Python list for the action (you make one action Input each iteration)]

CRITICAL RULES:
1. You operate in a loop. Each iteration, you provide ONLY Thought, Action, and Action Input.
2. DO NOT generate "Observation" text. Observations will be provided to you after each action (DON'T EVER GENERATE OBSERVATION, JUST USE IT).
3. After each observation, start a new iteration with a new Thought.
4. Use ONLY information from observations. Do not use external knowledge or assumptions.
5. You may need multiple iterations to gather enough information. Be patient and thorough.
6. Do NOT try to provide a final answer until you are absolutely certain you have all necessary information.
7. You should have good reasoning ability while thinking, so if there is an indirect question, you can use math to solve for it.
8. If an image is provided, consider using visual analysis tools if they might be relevant to the task.

When you are CERTAIN you have ALL information needed to answer the original question:
Thought: I now have all the information to answer the question
Action: finish
Final Answer: [Your detailed answer, referencing specific observations]

Remember:
- You CANNOT provide a final answer without using the "finish" action.
- Always wait for an observation after each action before starting a new iteration.
- If an observation is unclear or insufficient, use your next action to clarify or gather more information.
- Your goal is to be thorough and accurate, not quick. Take as many iterations as needed and use tools as much time as you need to get the best result.

Example workflow:
{example_workflow}

Let's begin!

Question: {question}
"""

        react_prompt = react_prompt.replace("{example_workflow}", self.example_workflow)
        react_prompt = react_prompt.replace("{prompt_string}", self.prompt_string)
        react_prompt = react_prompt.replace("{question}", self.question)

        if self.img:
            react_prompt += "\n\nNote: An image is provided with this prompt. Consider using visual analysis tools if they might be relevant to the task."

        return react_prompt

    def set_tools(self, tools: str, tool_names: str):
        """
        Set the available tools after initialization.
        
        :param tools: A string containing the list of available tools and their roles.
        :param tool_names: A string containing the names of the tools.
        """
        self.prompt = self.prompt.replace("{tools_and_role}", tools)
        self.prompt = self.prompt.replace("{tool_names}", tool_names)

# React prompt example : 

# """
# Question: What is the date today ?

# [you in iteration 1]
# Thought: I have to search for the day today using the internet to get a good resault.
# Action: search tool
# Action Input: today's date

# [you then STOP the first iteration after this]


# ... (not generated by AI it comes as from a software code) Observation: [the tool will return the today's date to you so you have to read the observation carefully to answer in the next step using it (you don't generate observation it just comes to you)]

# [you in iteration 2]
# Thought: from the previous Observation I can find good and specific information that can answer the user original question which is "What is the date today ?"
# Action: finish
# Final Answer: Today's date is... [if there is more to describe to make chat more user friendly do it]

# """
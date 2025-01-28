from src.council.agents.base import BaseAgent


# Add system prompts here
class GPTAgent(BaseAgent):
    def __init__(self, system_prompt: str = "You are an experienced React developer."):
        super().__init__(model_name="openai/gpt-4o-mini", system_prompt=system_prompt)

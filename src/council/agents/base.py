import logfire
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv
import os


class BaseAgent:
    def __init__(self, model_name: str, system_prompt: str):
        self._load_environment()
        self.model = OpenAIModel(model_name)
        self.agent = Agent(model=self.model, system_prompt=system_prompt)

    def _load_environment(self):
        load_dotenv()
        required_vars = [
            "OPENAI_API_KEY",
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )

    def run(self, query: str):
        logfire.configure()
        result = self.agent.run_sync(query)
        logfire.notice("Output from LLM: {result}", result=str(result.data))
        return result.data

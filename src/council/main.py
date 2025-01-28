import logfire
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

logfire.configure()


def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()

    required_vars = [
        "OPENAI_API_KEY",
    ]

    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )


def main():
    # Load environment first
    load_environment()

    # Then create model and agent
    model = OpenAIModel("deepseek/deepseek-r1")
    agent = Agent(model=model)

    result = agent.run_sync(
        "Say gmgm to the github deep divers. I hope y'all are ready to meet the council...."
    )

    print(result.data)


if __name__ == "__main__":
    main()

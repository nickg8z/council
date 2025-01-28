from src.council.agents.gpt import GPTAgent


def main():
    # demo of agent run
    agent = GPTAgent()
    response = agent.run("What are the key features of React?")
    print(response)


if __name__ == "__main__":
    main()

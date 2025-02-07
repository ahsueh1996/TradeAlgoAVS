# Autonome Framework: CDP Agentkit LangChain + Trading on Wealthsimple
This is our main contribution on the AI agent side of the project.
The innovation is in replacing traditional invesment funds by allowing profitable traders to share their strategies trustlessly with other investors. 
This custom framework outlines a generic operator node and its capabilities to become a validated service operator that sits between strategy providers (the profitable traders wishing to share their strategy and earn additional rewards) and strategy users (investors).

## Ask the chatbot to engage in the deFAI ecosystem!
The agentic portion of this project is not strictly necessary. In explicit, you do not need a LLM and a natural language interface to implement the core functionalities of this framework. But LLM is necessary for some of the more interesting features that will help more beginners engage in the deFAI ecosystem.

| **Investor**                                                                                                         | Needs LLM?         |
| ---------------------------------------------------------------------------------------------------------------- | ------------------ |
| Sign up and pay subscription to activate their account                                                           | no                 |
| Give their WS credentials and never have to do it again unless it's wrong                                        | no                 |
| Ask about strategies and which one is best for their goals                                                       | Yes                |
| Request for a strategy to start running and give the symbol they want to use it with                             | no                 |
| Ask about how their portfolio is doing including how many trades have been done, p&L                             | Could be dashboard |
| Ask about anything else they want about the stock market news etc etc                                            | yes                |
| **Strategy Provider**                                                                                                |                    |
| ---------------------------------------------------------------------------------------------------------------- | ------------------ |
| Sign up and upload the strategy                                                                                  | No                 |
| Ask about how their strategy is doing including how profitable it has been, how many investors have used it etc. | Could be dashboard |
| Ask for feedback on the strength and weaknesses of that strategy                                                 | yes                |

## Autonome Uploading Framework

Docker build and upload.

```bash
docker buildx build --no-cache --platform linux/amd64 --push -t {your username}/tradealgoavs .
```

## Local Testing

Create a new environment. I like to use Anaconda but you can use whatever you want. venv is great too. 

```bash
pip install poetry
poetry install
```

Setup your .env file to look like the following.
```bash
CDP_API_KEY_NAME= "organizations/.../apiKeys/..."
CDP_API_KEY_PRIVATE_KEY= "-----BEGIN EC PRIVATE KEY-----\n...............\n-----END EC PRIVATE KEY-----\n"
OPENAI_API_KEY= "sk-...."
```


Open two terminals using the same environment and run each of the python file in their own terminal.
```bash
python main.py
python local_user_test.py
```

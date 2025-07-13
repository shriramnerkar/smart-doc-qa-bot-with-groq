from langchain.chat_models import ChatOpenAI

def get_llm(model_name="gpt-3.5-turbo"):
    return ChatOpenAI(model=model_name)

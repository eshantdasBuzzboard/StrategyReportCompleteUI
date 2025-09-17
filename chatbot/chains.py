from chatbot.prompts import chat_bot_prompt
from chatbot.constants import junk_text, pumpkin_porters_transcript
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel


load_dotenv()
llm = ChatOpenAI(model="gpt-4.1")


class ChatBotResponse(BaseModel):
    chatbot_response: str


async def chatbot_reply_chain(query, chat_history=[]):
    llmr = llm.with_structured_output(ChatBotResponse)
    input_data = {
        "junk_data": junk_text,
        "ai_data": pumpkin_porters_transcript,
        "query": query,
        "chat_history": chat_history,
    }
    chatbot_chain = chat_bot_prompt | llmr
    response = await chatbot_chain.ainvoke(input_data)
    return response.chatbot_response

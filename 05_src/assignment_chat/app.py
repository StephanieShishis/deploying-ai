from .main import get_graph
from langchain_core.messages import HumanMessage, AIMessage
import gradio as gr
from .guardrails import check_message
import os

llm = get_graph()
 
def travel_chat(message: str, history: list[dict]) -> str:
    refusal = check_message(message)
    if refusal is not None:
        return refusal
 
    langchain_messages = []
    for msg in history:
        if msg['role'] == 'user':
            langchain_messages.append(HumanMessage(content=msg['content']))
        elif msg['role'] == 'assistant':
            langchain_messages.append(AIMessage(content=msg['content']))
    langchain_messages.append(HumanMessage(content=message))
 
    state = {
        "messages": langchain_messages
    }
 
    response = llm.invoke(state)
    return response['messages'][len(response['messages']) - 1].content
 
 
chat = gr.ChatInterface(
    fn=travel_chat,
    type="messages"
)
 
if __name__ == "__main__":
    chat.launch()

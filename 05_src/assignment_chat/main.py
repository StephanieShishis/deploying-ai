import os
 
from dotenv import load_dotenv
 
load_dotenv(".env")
load_dotenv(".secrets")
 
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
 
from .prompts import return_instructions
from .tools_weather import get_weather
from .tools_travel_search import search_city_guides
from .tools_itinerary import build_itinerary
 
chat_agent = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_key="any",
    default_headers={
        "x-api-key": os.getenv("API_GATEWAY_KEY")
    }
)
 
tools = [get_weather, search_city_guides, build_itinerary]
 
instructions = return_instructions()
 
def call_model(state: MessagesState):
    """LLM decides whether to call a tool or not"""
    response = chat_agent.bind_tools(tools).invoke([SystemMessage(content=instructions)] + state["messages"])
    return {
        "messages": [response]
    }
 
def get_graph():
 
    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    return graph
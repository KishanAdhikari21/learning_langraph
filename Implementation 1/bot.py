from typing import TypedDict, List
from langgraph.graph import StateGraph, START,END
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage, AIMessage]

llm= ChatOpenAI(model="gpt-4o")

def process(state: AgentState) -> AgentState:
    response= llm.invoke(state['messages'])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    return state

graph=StateGraph(AgentState)
graph.add_node("process",process)
graph.add_edge(START,"process")
graph.add_edge("process",END)
agent= graph.compile()

conversation_history=result["messages"]

user_input=input("message: ")
agent.invoke({"messages":[HumanMessage(content=user_input)]})

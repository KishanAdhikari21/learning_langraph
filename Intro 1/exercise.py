from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message: str

def entry_node(state: AgentState) -> AgentState:
    state["message"]=f"{state["message"]}, you're doing an amazing job learning LangGraph"
    return state

graph=StateGraph(AgentState)
graph.add_node("Compliment",entry_node)
app=graph.set_entry_point("Compliment")
app=graph.set_finish_point("Compliment")
app=graph.compile()
result=app.invoke({"message":"Bob"})
print(result)

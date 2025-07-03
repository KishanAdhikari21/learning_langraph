### building hello world graph

from typing import  TypedDict
from langgraph.graph import StateGraph  #framework that help in design and manage the flow of task using graph

class AgentState(TypedDict):
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """ Simple node that adds a greeting message to the state"""
    state['message']= f"Hey {state['message']}, how are you?"
    return state

def farewell_node(state: AgentState) -> AgentState:
    state['message']=f"Bye {state['message']}, have a good day!"
    return state


graph=StateGraph(AgentState)
graph.add_node("greeter",greeting_node)
graph.add_node("farewell",farewell_node)
app=graph.add_edge("greeter","farewell")
graph.set_entry_point("greeter")
app=graph.set_finish_point("farewell")
app=graph.compile()
result=app.invoke({"message":"Bob"})
print(result)    

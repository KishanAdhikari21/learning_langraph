from typing import TypedDict, List , Dict
import random
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    name: str
    number: list[int]
    counter: int

def greeting_node(state: AgentState) -> AgentState:
    """Greeting Node which says hi to the person"""
    state["name"]=f"Hi there, {state["name"]}"
    state["counter"]=0
    return state

def random_node(state: AgentState) -> AgentState: 
    """Generate a random number from 0 to 100"""
    state["number"].append(random.randint(0,10))
    state["counter"] +=1
    return state

def should_continue(state: AgentState) -> AgentState:
    """Function to decide what to do next"""
    if state["counter"] < 5:
        print("ENTERING LOOP",state['counter'])
        return "loop"
    else:
        return "exit"


graph=StateGraph(AgentState)
graph.add_node("greeting",greeting_node)
graph.add_node("random",random_node)
graph.add_edge("greeting","random")



graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop":"random",
        "exit":END
    }
)
graph.set_entry_point("greeting")
app=graph.compile()
result=app.invoke({"name":"Vaibhav", "number":[], "counter":-100})

print(result)





from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    skills: list
    result: str

def first_node(state: StateGraph) -> StateGraph:
    """ This is the first node of our graph"""
    state['result'] = f"Hi, {state["name"]}."
    return state
def second_node(state: StateGraph) -> StateGraph:
    """ This is the second node of our graph"""
    state["result"]=state["result"] + f" You are {state['age']} years old."
    return state

def third_node(state: StateGraph)-> StateGraph:
    """This is the third node of our graph"""
    state['result']= state['result']+ f" You know these skills: {', '.join(skill for skill in state["skills"])}"
    return state


graph=StateGraph(AgentState)
graph.add_node("first_node",first_node)
graph.add_node("second_node",second_node)
graph.add_node("third_node",third_node)
graph.add_edge("first_node","second_node")
graph.add_edge("second_node","third_node")
graph.set_entry_point("first_node")
graph.set_finish_point("third_node")
app=graph.compile()
result=app.invoke({"name":"Bob","age":22,"skills":["python","c++","Go"]})
print(result['result'])

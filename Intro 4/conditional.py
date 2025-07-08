from typing import TypedDict
from langgraph.Graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    finalNumber: int

def adder(state: AgentState) -> AgentState:
    """This node adds the 2 number"""
    state['finalNumber']= state["number1"]+state["number2"]
    return state

def subtractor(state: AgentState) -> AgentState:
    """This node substract the 2 number"""
    state["finalNumber"]=state["number1"]-state["number2"]
    return state

def decide_next_node(state: AgentState) -> AgentState:
    """This node will select the next node of the graph"""
    if state["operation"] == "+":
        return "addition" # string is returned as AgentState
    elif state['operation']=="-":
        return "substraction"
    
graph=StateGraph(AgentState)
graph.add_node("add_node",adder)
graph.add_node("subtract_node",subtractor)
graph.add_node("router",lambda state:state) #passthrough function
graph.add_edge(START, "router")
graph.add_conditional_edges("router",
                           decide_next_node,
                           {
                               "addition":"add_node",
                               "substraction":"substract_node"
                           }
                             )

graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app=graph.compile()





from typing import TypedDict
from langgraph.Graph import StateGraph, START, END


class AgentState(TypedDict):
    number1: int 
    operation: str
    number2: int
    finalnumber: int
    number3: int
    operation2: str
    number4: int
    finalnumber2: int

def calculate(state: AgentState, key1: str, key2: str, out_key: str, op: str) -> AgentState:
    a= state[key1]
    b= state[key2]
    if op =="+":
        state['out_key']=a+b
    elif op == "-":
        state['out_key']=a-b
    return state

def
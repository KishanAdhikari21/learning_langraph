from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    list: int
    name: str
    operation: str
    result: str

def process_values(state: AgentState) -> AgentState:
    """ This node process values and based on operation it perform it."""
    if state['operation'] == '+':
        state['result']= f"Hi {state['name']}, your answer is: {sum(state['list'])}"
    elif state['operation'] == '*':
        ans=1
        for num in state['list']:
            ans*=num
        state['result']=f"Hi {state['name']}, your answer is: {ans}"
    return state

graph=StateGraph(AgentState)
graph.add_node("Processor",process_values)
graph.set_entry_point("Processor")
graph.set_finish_point("Processor")
app=graph.compile()
answer1= app.invoke({"list":[1,2,3,4],"name":"Jack Sparrow","operation":"+"})
print(answer1)
answer2= app.invoke({"list":[1,2,3,4],"name":"Jack Sparrow","operation":"*"})
print(answer2)







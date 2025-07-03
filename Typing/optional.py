from typing import Optional

def nice_message(name: Optional[str])-> None:
    """ name can be either string or none"""
    if name is None:
        print("Hello, stranger!")

    else: 
        print(f"Hi there, {name}")
    
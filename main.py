import random 
from typing import List
from fastmcp import FastMCP
from starlette.routing import Host

mcp = FastMCP(name="demo-mcp-server")

@mcp.tool()
def roll_dice(n_dice: int = 1) -> List[int]:
    """Roll N number of dice with 6 sides"""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    # for local server 
    # mcp.run()
    
    # for remote server 
    mcp.run(transport="http",host="0.0.0.0",port=8000)

import random 
from typing import List
from fastmcp import FastMCP

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
    mcp.run()

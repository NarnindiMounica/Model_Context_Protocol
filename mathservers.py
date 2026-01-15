import mcp
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b:int)->int:
    """Add two numbers together"""
    return a+b


@mcp.tool()
def multiply(a:int, b:int)->int:
    """Multiply two numbers together"""
    return a * b


if __name__=="__main__":
    mcp.run(transport="stdio")

#The transport="stdio" argument tells the server to:
# Use standard input/output (stdiin and stdout) to receuve and respond to tool
# function calls



        
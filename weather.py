from mcp.server.fastmcp import FastMCP

mcp =FastMCP("Weather")

@mcp.tool()
def get_weather()->str:
    """Get the weather for a given city"""
    return f"The weather is always rainy"
    
if __name__=="__main__":
    mcp.run(transport="streamable-http")
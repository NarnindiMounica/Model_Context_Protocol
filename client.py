from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()
import asyncio

async def main():
    client = MultiServerMCPClient(
        {"math":{
            "command":"python",
            "args":["mathservers.py"], # ensure correct path is provided
            "transport":"stdio",
        },
        "Weather":{
            "url":"http://127.0.0.1:8000/mcp", #ensure server is running here
             "transport": "streamable-http"     
                }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_agent(model=model,
                        tools=tools,
                        )

    math_response = await agent.ainvoke({"messages":{"role":"user",
    "content": "what is 1 + 2 * 3?"}})

    print(f"Math response:\n {math_response['messages'][-1].content}")

    weather_response = await agent.ainvoke({"messages":{"role":"user",
    "content": "how is weather ?"}})

    print(f"Weather response:\n {weather_response['messages'][-1].content}")
                    
asyncio.run(main())


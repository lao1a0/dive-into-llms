from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
#echo "https://api.developer.iata.org/duffel-duffel-default/api/duffel/details" | smithery run Fabien-desablens-mcp-webpage-timestamps.mcpb --key "b9dff0dc-7046-4ad2-88b0-cef602f99011"

# Construct server URL with authentication
from urllib.parse import urlencode

base_url = "https://server.smithery.ai/@DeniseLewis200081/rail/mcp"
params = {"api_key": ""}
url = f"{base_url}?{urlencode(params)}"


async def main():
    # Connect to the server using HTTP client
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print(f"Available tools: {', '.join([t.name for t in tools_result.tools])}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
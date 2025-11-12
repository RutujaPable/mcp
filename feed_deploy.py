from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FreeCodeCamp Feed Searcher")

@mcp.tool()
def fcc_news_search(query:str, max_results:int=3):
    """Search FreeCodeCamp news feed via RSS by title/description"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break #unlikely to occur

    return results or [{"message":"No results found"}]

@mcp.tool()
def ms_youtube_search(query:str, max_results:int=3):
    """Search Meta Sensing Youtube channnel via RSS by title"""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCSXbhujyE1nz1YNd9l92xhw")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break #unlikely to occur
    return results or [{"message":"No videos found"}]

if __name__ == "__main__":
    mcp.run(transport="http") 

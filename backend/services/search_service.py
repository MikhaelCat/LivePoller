from elasticsearch import AsyncElasticsearch

es = AsyncElasticsearch(hosts=["http://elasticsearch:9200"])

async def search_polls(query: str):
    result = await es.search(
        index="polls",
        body={"query": {"match": {"question": query}}}
    )
    return result["hits"]["hits"]
import requests
import json
from app.services.redis_cache import redis_client
from app.core.config import settings

# TODO move later to configs for global
BASE_URL = "https://api.github.com/search/repositories"

def search_repositories(language, created_after):
    """
    main logic to call github url & search for repos based on params
    :param language: str
    :param created_after: str
    :return: json obj

    TODO input format & validtions for future
    """
    cache_key = f"search:{language}:{created_after}"
    cached = redis_client.get(cache_key)

    if cached:
        print("found cache")
        return json.loads(cached)
    else:
        print("cache didnt worked")

    headers = {}
    if settings.GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

    query = []
    if language:
        query.append(f"language:{language}")
    if created_after:
        query.append(f"created:>={created_after}")

    response = requests.get(
        BASE_URL,
        headers=headers,
        params={
            "q": " ".join(query),
            "sort": "stars",
            "order": "desc",
            "per_page": 50 #TODO set global
        },
        timeout=10
    )
    response.raise_for_status()

    items = response.json()["items"]
    # print(items)
    redis_client.setex(
        cache_key,
        settings.CACHE_TTL_SECONDS,
        json.dumps(items)
    )
    return items

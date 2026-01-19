import redis
from app.core.config import settings

# redis client object
redis_client = redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)

import math
from datetime import datetime

def compute_score(repo: dict) -> float:
    """util function to perform calculation of popularity
    :param repo: dict obj
    :return: number
    """
    stars = repo["stargazers_count"]
    forks = repo["forks_count"]
    updated_at = datetime.fromisoformat(repo["updated_at"].replace("Z", ""))

    days = (datetime.utcnow() - updated_at).days
    recency = math.exp(-days / 90)
    # below can be made configurable & above recency too
    return round(
        0.5 * math.log(stars + 1) + 0.3 * math.log(forks + 1) + 0.2 * recency,
        2
    )

from typing import List


def parse_cors(origins: str) -> List[str]:
    if not origins:
        return []
    return [origin.strip() for origin in origins.split(",") if origin.strip()]

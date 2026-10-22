PROFILES = {
    "balanced": {"price": 0.5, "rating": 0.5},
    "best_value": {"price": 0.7, "rating": 0.3},
    "best_quality": {"price": 0.3, "rating": 0.7},
}

def price_score(price, lowest, highest):
    total = highest + lowest
    if total == 0:
        raise ValueError("Lowest and highest prices cannot both be zero.")
    score = (1 - (price / total)) * 10
    return round(score, 1)

def final_score(price_value, platform_score, profile):
    if profile not in PROFILES:
        raise ValueError(f"Profile '{profile}' is not defined.")    
    if platform_score is None:
        return None
    platform_score = platform_score * 2
    weights = PROFILES[profile]
    final = (price_value * weights["price"]) + (platform_score * weights["rating"])
    return round(final, 1)
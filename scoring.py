def price_score(price, lowest, highest):
    total = highest + lowest
    if total == 0:
        raise ValueError("Lowest and highest prices cannot both be zero.")
    score = (1 - (price / total)) * 10
    return round(score, 1)
def kids_with_candies(candies: list[int], extraCandies: int) -> list(bool):
    max_candies = max(candies)
    sol = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_candies:
            sol.append(True)
        else:
            sol.append(False)
    return sol


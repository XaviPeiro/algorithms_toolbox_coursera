from typing import List


def max_ad_revenue(prices: List[int], avg_clicks_per_slot: List[int]) -> int:
    sorted_prices = sorted(prices, reverse=True)
    sorted_avg_clicks_per_slot = sorted(avg_clicks_per_slot, reverse=True)

    adds_revenue = sum([a*b for a, b in zip(sorted_avg_clicks_per_slot, sorted_prices)])

    return adds_revenue


if __name__ == "__main__":
    n_of_vals = int(input())
    prices = list(map(int, input().split()))
    avg_clicks = list(map(int, input().split()))
    res = max_ad_revenue(prices=prices, avg_clicks_per_slot=avg_clicks)
    print(res)

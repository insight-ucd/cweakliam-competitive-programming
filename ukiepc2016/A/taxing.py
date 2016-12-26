n_bands = int(raw_input())
bands = [raw_input().split() for _ in range(n_bands)]
band_sizes = [float(band[0]) for band in bands]
band_rates = [float(band[1]) / 100 for band in bands]
final_rate = float(raw_input()) / 100
band_rates.append(final_rate)
band_sizes.append(float("inf"))
n_friends = int(raw_input())
friends = [raw_input().split() for _ in range(n_friends)]
friend_incomes = [float(friend[0]) for friend in friends]
friend_profits = [float(friend[1]) for friend in friends]

def solve(band_sizes, band_rates, income, target_profit):
    """How much you need to give in order for the person to recieve
    target_profit"""
    # based on income, find out: 1. which band the person is in, 2. how much of
    # that band is left
    remaining_income = income
    for i in range(len(band_sizes)):
        size, rate = band_sizes[i], band_rates[i]
        if remaining_income <= size:
            left_in_band = size - remaining_income
            band = i
            break
        remaining_income -= size

    # now that we know what tax band the person is in, calculate how much more
    # money we need to give for the person to receive target_profit
    sizes = [left_in_band] + band_sizes[band+1:]
    rates = band_rates[band:]
    gift = 0
    left_to_get = target_profit
    for size, rate in zip(sizes, rates):
        if rate != 1: # prevent division by zero
            need_to_give = left_to_get / (1 - rate)
            if need_to_give < size:
                gift += need_to_give
                return gift
        gift += size
        left_to_get -= size * (1 - rate)

for income, profit in zip(friend_incomes, friend_profits):
    print solve(band_sizes, band_rates, income, profit)

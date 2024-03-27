import sys
from decimal import Decimal

def calculate_coin_breakdown(value):
    coins = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
    coin_values = {'quarters': Decimal('0.25'), 'dimes': Decimal('0.10'), 'nickels': Decimal('0.05'), 'pennies': Decimal('0.01')}

    remaining_value = Decimal(str(value))

    for coin in coin_values:
        while remaining_value >= coin_values[coin]:
            coins[coin] += 1
            remaining_value -= coin_values[coin]

    return coins

if len(sys.argv) != 2:
    print("Usage: python new_greedy_coin.py <value>")
else:
    value = float(sys.argv[1])
    coin_breakdown = calculate_coin_breakdown(value)
    print(coin_breakdown)
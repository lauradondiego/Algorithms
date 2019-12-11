#!/usr/bin/python

import argparse


def find_max_profit(prices):
    right_prices = prices[1:]  # starts looking at index[1] until the end
    max_price = max(right_prices)  # find the max_price after first index
    # if max_price is at index[0], find next largest price

    # find index of largest price
    # this returns the index of the largest value
    max_price_idx = prices.index(max_price)
    # slice the list to the left of largest price [0:max_price [-1]
    # starts at 0, slices up to index of max_price
    left_prices = prices[:max_price_idx]
    print("left prices", left_prices)
    min_price = min(left_prices)  # built in python method
    print("min price", min_price)
    calc_profit = max_price - min_price
    print(max_price, max_price_idx)
    return calc_profit


# print(find_max_profit([100, 90, 80, 50, 20, 10]))  # test

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

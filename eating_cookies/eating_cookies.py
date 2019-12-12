#!/usr/bin/python

import sys
# @functools import lru_cache
# ^ import the cache library instead of having to write it all out below
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# @lru_cache(maxsize=500)
def eating_cookies(n, cache={}):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    else:
        # print(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
        if n not in cache:
            print(cache)
            cache[n] = eating_cookies(
                n-1) + eating_cookies(n-2) + eating_cookies(n-3)

        return cache[n]


print(eating_cookies(5))  # test


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
# else:
# print('Usage: eating_cookies.py [num_cookies]')

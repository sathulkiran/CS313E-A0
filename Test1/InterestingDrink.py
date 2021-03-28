#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of coffee in each store, and a list of integers named money that contains the amount of money
#               Peter will spend in a given day, returns a list of integers representing how many different shops
#               Peter can buy a cup of coffee.

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

import sys


# Input: prices a list of integers containing the price of coffee in each store
#        money  a list of integers containing the amount of money Peter will spend in a given day
# Returns: a list of integers representing how many different shops Peter can buy a cup of coffee.
def find_purchase_options(prices, money):
    leng = len(prices)
    if leng < 20:
        templist = []
        for i in money:
            count = 0
            for k in prices:
                if k <= i:
                    count += 1
            templist.append(count)
        return templist
    else:

        srtd = prices.copy()
        srtd = sorted(srtd)
        n = len(srtd)
        newlist = []
        for key in money:
            lo = 0
            hi = n-1
            mid = 0
            while lo < hi:
                mid = (lo+hi)//2
                if (srtd[mid]==key):
                    while (mid + 1<n and srtd[mid + 1] == key):
                        mid += 1
                    break
                elif (srtd[mid] > key):
                    hi = mid
                else:
                    lo = mid+1
            newlist.append(mid)
        return newlist




#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()




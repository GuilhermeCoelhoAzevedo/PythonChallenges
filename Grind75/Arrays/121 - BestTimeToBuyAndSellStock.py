#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        if price < min_price:
            min_price = price
            continue

        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))

#Optimized solution:
"""
def maxProfit(prices):
    buy_price = prices[0]
    profit = 0
    
    for p in prices[1:]:
        if buy_price > p:
            buy_price = p
    
        profit = max(profit, z
    
    return profit
"""
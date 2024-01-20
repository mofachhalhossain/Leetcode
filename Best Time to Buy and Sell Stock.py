def maxProfit(prices):
    buy, sell = 0, 1
    profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            p = prices[sell] - prices[buy]
            profit = max(profit, p)
        else:
            buy = sell
        sell+=1
    return profit







prices = [7,1,5,3,6,4]
print(maxProfit(prices))
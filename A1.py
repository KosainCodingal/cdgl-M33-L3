def profitCalc(stocks):
    p = 0
    l = 0
    for i in range(1, len(stocks)):
        if stocks[i] > stocks[i-1]: p += stocks[i] - stocks[i-1]
        if stocks[i] < stocks[i-1]: l += stocks[i] - stocks[i-1]
    return (p, l)

prices = [
    635, 864, 176, 985, 300, 300, 582, 20
]

prices = [
    1000, 800, 600, 500, 400, 200, 100, 100
]


profit = profitCalc(prices)
print("Max profit:", profit[0])
print("Max loss:", profit[1])
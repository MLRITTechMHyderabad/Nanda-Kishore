import numpy as np

np.random.seed(42)
stock_prices = np.random.randint(100, 501, size=(30, 5))

avg_prices = np.mean(stock_prices, axis=0)

max_price = np.max(stock_prices)
day, company = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)

min_price = np.min(stock_prices)
max_price = np.max(stock_prices)
normalized_prices = (stock_prices - min_price) / (max_price - min_price)

risky_days = np.where(stock_prices < 200)

print(f"Stock Prices:\n{stock_prices}\n")
print(f"Average Stock Prices: {avg_prices}\n")
print(f"Highest Price Recorded: {max_price} at Day {day+1}, Company {company+1}\n")
print(f"Normalized Prices:\n{normalized_prices}\n")

if risky_days[0].size == 0:
    print("No risky investment days detected.")
else:
    print("Risky Investment Days:")
    for i in np.unique(risky_days[0]):
        risky_values = stock_prices[i, stock_prices[i] < 200]
        print(f"Day {i+1}: {list(risky_values)}")

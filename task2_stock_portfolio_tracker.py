# Stock Portfolio Tracker
# These are sample prices for this beginner project, not live market prices.

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks and sample prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price} per share")

portfolio = {}
total_investment = 0

while True:
    stock = input("\nEnter stock symbol (or type DONE to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock symbol not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a whole number for quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n=== YOUR PORTFOLIO ===")
if not portfolio:
    print("No stocks were added.")
else:
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")

    print(f"\nTotal investment value: ${total_investment}")

    # Save the result to a text file.
    with open("portfolio_result.txt", "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares = ${value}\n")
        file.write(f"\nTotal investment value: ${total_investment}\n")

    print("Summary saved to portfolio_result.txt")

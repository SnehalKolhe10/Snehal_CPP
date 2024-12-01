# Import the sorting function from your package
from sort_prices import sort_prices_low_to_high

# Test data (some example flight prices)
prices = [1200, 850, 1000, 1500]

# Call the sorting function
sorted_prices = sort_prices_low_to_high(prices)

# Print the sorted prices
print(sorted_prices)
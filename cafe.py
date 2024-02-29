# List with menu items in cafe
menu = ['Drip Coffee', 'Aeropress', 'Americano', 'Cappuccino', 'Latte',]
# Dictionary with stock value of menu items
stock = {'Drip Coffee': 10, 
         'Aeropress': 10, 
         'Americano': 10, 
         'Cappuccino': 10, 
         'Latte': 10

}
# Dictionary with prices for menu items
price = {'Drip Coffee': 2.95, 
         'Aeropress': 3.10, 
         'Americano': 3.50, 
         'Cappuccino': 3.60, 
         'Latte': 3.60
}

# Find total stock worth of each item on menu
item_value = (  stock['Drip Coffee'] * price['Drip Coffee'], 
                stock['Aeropress'] * price['Aeropress'],
                stock['Americano'] * price['Americano'],
                stock['Cappuccino'] * price['Cappuccino'],
                stock['Latte'] * price['Latte']
                )
# Set sum of all item_value as a variable 
total_stock_worth = sum(item_value)
# Print total_stock_Worth in a string 
print(f"The total of all your stock items amount to £{total_stock_worth}")



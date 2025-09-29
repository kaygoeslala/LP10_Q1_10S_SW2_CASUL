from pyscript import display
#Restaurant order system (python datatypes)

#string
restaurant_name = "Santi's"
owner_name = "Mckayla Casul"

#integer
year_since = 2024

#float
tax_rate = 0.08

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#list
product_names = ["Tiramisu", "Pasta", "Cream Cheese Ham Sandwich"]
beverages = ["Water", "Juice", "Water"]

#tuple
business_hours = ("12:00 PM", "4:00 AM")

#dictionary
menu = {
    "Tiramisu": 550.00,
    "Pasta": 150.00,
    "Cream Cheese Ham Sandwich": 100.00,
    "Coke": 20.00,
    "Water": 50.00,
}

#set
common_allergens = {"Gluten", "Dairy", "Nuts"}

#display restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

#display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Tiramisu']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Pasta']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Cream Cheese Ham Sandwich']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"₱{menu['Coke']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Water']:.2f}", target="price5")

#display additional info
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#display order type
display(f"Dine-in Available", target="orderType")
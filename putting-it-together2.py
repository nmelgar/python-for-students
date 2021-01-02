#Expected output
#welcome to julie's pizza
#our available toppings are:
#Cheese (free)
#Pepperoni ($1 extra)

pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1 extra)"

def print_menu(toppings):
    print("Welcome to julie's pizzeria")
    print("Are available toppings are:")
    for topping in toppings:
        print(format_topping(topping))

print_menu(pizza_toppings)
#these 2 lines are to make sure it works right
#print(format_topping("cheese") == "Cheese (Free)")
#print(format_topping("pepperoni") == "Pepperoni ($1 extra)")


pizza_toppings = ["cheese", "pepperoni", "mushrooms", "pineapple"]
print("we have the following toppings: ")
for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping} (free)")

    else:
        print(f"{topping} ($1.00)")

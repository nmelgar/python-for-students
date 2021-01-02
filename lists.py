numbers = [1, 2, 3]
pizza_toppings = ["cheese", "tomatoes", "pepperoni"]
mixed_list = [1, "cheese", 2, "pepperoni"] 
list_of_lists = [[1, 2], [2, 3]]

#print(pizza_toppings[-1])
print(len(pizza_toppings))

pizza_toppings.append("pineapple")
pizza_toppings.insert(0, "mushrooms") #to insert at the beginning

print(pizza_toppings)
del pizza_toppings[0]
print(pizza_toppings)

pizza_toppings.pop() #removes temporarily an element from the list
print(pizza_toppings)

pizza_toppings.remove("cheese")
print(pizza_toppings)

pizza_toppings = ["cheese", "cheese", "tomatoes", "pepperoni"]
pizza_toppings.remove("cheese")
print(pizza_toppings)

print(f"\nThe first part of lists is over")

places = ["culiacan", "tijuana", "veracruz", "cancun"]
del places[2] #deletes element permanently
print(places)

places.insert(2, "merida")
print(places)

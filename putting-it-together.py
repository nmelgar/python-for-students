def pizza_name(topping):
    return f"{topping.title()} Pizza"

pizza = pizza_name("cheese")
print(pizza)

#another function to return the value of a number times 2
def times_two(num):
    return num * 2

print(times_two(2))


#function to accept name and age and return both
def person_information(name, age):
    return f"This person is {name} and he is {age} years old"

#you can use a variable to store the information too
person = person_information("john", 6)
print(person)
#or you can use the next line to dont use a variable
#print(person_information("john", 6))

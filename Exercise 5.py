# # Question 1: Creating and Modifying Lists

# # TODO: Create a list of fruits

# fruits =  ["watermalon","apple", "banana", "orange", "strawberry", "blueberry", "mango"]

# # TODO: Add a fruit to the end of the list

# fruits.append("kiwi")
# print(fruits)

# # TODO: Insert a fruit at the beginning of the list

# fruits.insert(0,"avocado")
# print(fruits)

# # TODO: Remove a fruit from the list

# fruits.remove("banana")
# print(fruits)
# # TODO: Print the modified list

# fruits.sort()
# print(fruits)
# #-------------------------------------------------------------------------
# # Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5

list_number = [1,2,3,4,5]

# TODO: Create a new list with each number squared
def square(list_number):
    return list_number ** 2

sqaured_list = []
for number in list_number:
    (number ** 2)
    sqaured_list.append(square(number))
print(sqaured_list)

# sqaured_list = []
# for number in list_number:
#     print(number ** 2)
#     sqaured_list.append(number ** 2)
# print(sqaured_list)

# TODO: Find the sum and average of the original numbers

total_sum = sum(list_number)
average = sum(list_number) // len(list_number)

# TODO: Print the results
print(f'The total sum is : {total_sum}')
print(f'The average sum is : {average}')

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals

countries = {
    "France" : "Paris",
    "South Africa" : "Cape Town",
    "Russia" : "Moscow",
    "Japan" : "Beijing",
    "Canada" : "Ottawa",
    "Germany" : "Berlin",
    "India" : "New Delhi",
    "Australia" : "Canberra"
}

# TODO: Add a new country-capital pair

countries.update({"Turkey" : "Ankara"})

# TODO: Update the capital of an existing country

countries.update({"Japan" : "Tokyo"})

# TODO: Remove a country-capital pair

countries.pop("Germany")
 
# TODO: Print the modified dictionary

print(countries) 

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors

fruit_colors = {
    "Strawberries" : "Red Fruit",
    "Cantaloupe" : "Orange Fruit",
    "Pineapples" : "Yellow Fruit",
    "Avocados" :  "Green Fruit",
    "Blueberries" :"Blue  Fruit" 
}

# TODO: Print all the fruits (keys)

for key in fruit_colors:
    print(key)

# TODO: Print all the colors (values) 

for value in fruit_colors.values():
    print(value)

# TODO: Print each fruit and its color

for key, value in fruit_colors.items():
    print(key,value)

# TODO: Check if a fruit is in the dictionary and print its color

for key in fruit_colors:
    if key == "Strawberries":
     print(fruit_colors[key])

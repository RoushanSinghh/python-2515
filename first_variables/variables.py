# Syntax
# variable_name = value
# = --> Assignment operator

# Immutable Data (numbers, decimals, simple text)
value_num = 10
value_rating = 4.2
value_name = "Ravi"

new_rating = 4.2
new_name = "Ravi"

print(id(value_num)) # unique identity i.e memory address
print(id(value_rating)) # unique identity i.e memory address
print(id(value_name)) # unique identity i.e memory address

print(id(new_rating)) # unique identity i.e memory address
print(id(new_name)) # unique identity i.e memory address

# Lists in python are Mutable 
list1 = [1,2,3]
list2 = [1,2,3]
list3 = [4,5,6]

print(id(list1)) # unique identity i.e memory address
print(id(list2)) # unique identity i.e memory address
print(id(list3)) # unique identity i.e memory address

# type function defines what data types is being assigned for variable

print(type(value_num)) 
print(type(value_rating)) 
print(type(value_name)) 

# Output Variables
msg = "Python is Awesome"
print(msg)

x = "Python "
y = "Is "
z = "Awesome"

print(x+y+z)

version = 3.14 
version_old = 2
print(x+y+z)
print(version+version_old)

# print Python is Awesome 3

print(version,msg)

# many values to multiple variables
# no of variables must be equal to no of values
x,y,z = "Python", "Is", "Awesome"
print(x)
print(x,y,z)

# one value to multiple variables
x = y = z = "Python"
print(x,y,z)

# ProductName --> Pascal Case (ClassNames)

# productName --> CamelCase (objectNames)

# product_name --> SnakeCase (When using variables & functions)

product_brand = "Levis"
product_rating = 4.2
product_price = 1600
air_bag_present = True 

# prepare variables for this -> car_dekho.py 
# https://www.cardekho.com/hyundai/creta/specs

# Seating Capacity 5 --> seating_capacity = 5 # int type of data

# Simple Data Types --> int, float, String, Boolean, 
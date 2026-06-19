# Given;
x = ("samsung", "iphone", "tecno", "redmi")
# print my favorate phone
print(x[1])

# Negative indexing to print the 2nd last item in the tuple
print(x[-2])

# Update "iphone" to to "itel"
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

# Add Huawei to the tuple
x =list(x)
x.append("Huawei")
x = tuple(x)
print(x)

# Loop through the tuple
for phone in x:
    print(phone)
    
# Remove/delete the first item in the tuple
x = list(x)
x.remove(x[0])
# or x.pop(0)
x = tuple(x)
print(x)

# Use a consrtuctor to create a tuple of cities
cities = tuple(["Lagos", "Abuja", "Port Harcourt", "Kano"])
print(cities)   

# Program to unpack the tuple of cities
city1, city2, city3, city4 = cities
print(city1)
print(city2)
print(city3)
print(city4)

# Use range to print 2nd, 3rd and 4th item in the tuple
for i in range(1, 4):
    print(x[i])

# 2 tuples, one for first name and the other for last name. Join the 2.
first_name = ("John", "Jane", "Doe")
last_name = ("Smith", "Johnson", "Williams")
full_names = first_name + last_name
print(full_names)
# or full_names = tuple(zip(first_name, last_name))

# Create a color of tuples and multiply by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

# return how many times 8 appears in the tuple below
thistuple =(1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))
# or count = 0
# for num in thistuple:
#     if num == 8:
#         count += 1
# print(count)

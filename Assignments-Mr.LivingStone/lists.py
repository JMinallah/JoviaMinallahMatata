# List of 5 names of people and output the 2nd
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])

# Change the value of the first item to a new one
names[0] = "Alex"

# Add a new name to the end of the list
names.append("Frank")

# Add "Bathel" as the 3rd item in the list
names.insert(2, "Bathel")

# Remove the 4th item from the list
del names[3]

# Use negative indexing to output the last item in the list
print(names[-1])

# Create a new list of 7 items and use range to output the 3rd, 4th and 5th items
new_names = ["Grace", "Henry", "Ivy", "Jack", "Kate", "Liam", "Mia"]
print(new_names[2:5])

# List of countries and make a copy of the list
countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
countries_copy = countries.copy()
print(countries_copy)

# Program to loop through the list of countries and output each one
for country in countries:
    print(country)
    
# List of animals and arrange in both ascending and descending order
animals = ["Dog", "Cat", "Bird", "Fish", "Horse"]
animals.sort()  # Ascending order
print(animals)
animals.sort(reverse=True)  # Descending order
print(animals)

# Program to output animals with "a" in their name
for animal in animals:
    if "a" in animal.lower():
        print(animal)
        
# 2 lists, first of my first names and second of my last names, then combine them into a new list of full names
first_names = ["John"]
last_names = ["Doe"]
full_names = [f"{first} {last}" for first, last in zip(first_names, last_names)]
print(full_names)
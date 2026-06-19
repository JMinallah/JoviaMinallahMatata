# use set() to create a set of 3 beverages
beverages = set(["coffee", "tea", "juice"])

# add 2 more beverages to the set
beverages.add("soda")
beverages.add("water")
print(beverages)

# checking if microwave i present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

# remove kettle
mySet.remove("kettle")
print(mySet)

# Loop through the set
for item in mySet:
    print(item)
    
# set of 4 items and a list of 2. add list items to the set
mySet = {"apple", "banana", "orange", "grape"}
myList = ["grape", "melon"]
mySet.update(myList)
print(mySet)

# 2 sets. one for ages, and another firstnames. join the 2 sets
ages = {25, 30, 35, 40}
firstnames = {"Alice", "Bob", "Charlie", "David"}
combined_set = ages.union(firstnames)
print(combined_set)
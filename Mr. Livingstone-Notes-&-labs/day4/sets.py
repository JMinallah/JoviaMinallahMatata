#used to store collection of unique items
#unordered, mutable, iterable
#support fast search

#example
Cars = {"Toyota", "Honda", "Ford", "BMW"}
print(Cars)
print(type(Cars))

# #adding, removing and clearing items
# Cars.add("Nissan") #adding item
# print(Cars)
# Cars.remove("Ford") #removing item ....can also use discard() which does not raise an error if item is not found
# print(Cars)
# Cars.clear() #clearing all items
# print(Cars) #output: set()
# updating set means adding multiple items at once
Cars.update(["Nissan", "Mazda", "Hyundai"])
print(Cars)

#Demonstrate data uniqueness
Cars.add("Toyota") #adding duplicate item
print(Cars) #Toyota will not be added again

#Demonstrate data duplication
Names = {"John", "Alice", "Bob", "John"} #duplicate item
print(Names) #John will not be added again

#Accessing set items
for car in Cars:
    print(car)
    
#operations on sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
#union
C = A.union(B)
print(C) #output: {1, 2, 3, 4, 5, 6, 7, 8}
#intersection
D = A.intersection(B)
print(D) #output: {4, 5}
#difference
E = A.difference(B)
print(E) #output: {1, 2, 3} 


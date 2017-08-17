people = ["John", "Anna", "Mary"]

person = input("Enter a name: ")

if person in people:
    print("{} is in my list!".format(person))
else:
    print("{} is NOT in my list!".format(person))

print("Done")

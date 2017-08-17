#known_people = ["John", "Anna", "Mary"]

#person = input("Enter the person you know: ")

#if person in known_people:
#    print("You know {}!".format(person))
#else:
#    print("You don't know {}!".format(person))    


def who_do_you_know():
    people_string = input("Enter the names of people you know, separated by commas: ")

    people_list = []
    person_name = ""
    for i in people_string:
        if i == ",":
            if person_name != "":
                people_list.append(person_name)
                person_name = ""        
        else:
            if i != " ":
                person_name = person_name + i
    if person_name != "":
        people_list.append(person_name)
    return people_list
   

def ask_user(person_list):
    name = input("Enter a name: ")
    if name in person_list:
        print("You know {}!".format(name))
    else:
        print("You don't know {}!".format(name))    

user_list = who_do_you_know()
for person in user_list:
    print(person)

should_continue = "y"
while should_continue == "y":
    should_continue = input("Do you want to continue? (y/n) ")
    if should_continue == "y":
        ask_user(user_list)

print ("Done")    
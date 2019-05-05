import os

clear_vers = 'cls'
mydirectory = []

class Person():

    def __init__(self, fname, lname, email, pnum, address, city, state):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pnum = pnum
        self.address = address
        self.city = city
        self.state = state

    def __str__(self):
        return self.lname + ", " + self.fname + " | " + self.email + " | " + self.pnum + " | " + self.address + ", " + self.city + ", " + self.state

mydirectory.append(Person("Krystal", "House", "kryshouse@geekmail.com", "214-345-2835", "78 Meadowlark Court", "Austin", "TX"))
mydirectory.append(Person("Jack", "Whisky", "jwhisky@gmail.com", "978-876-7121", "7804 FM 2862", "Jersey", "OH"))
mydirectory.append(Person("Joe", "Smith", "jsmith@gmail.com", "234-456-5673", "123 Samson Ln", "Plano", "TX"))
mydirectory.append(Person("Zane", "Hollow", "zaneh@yahoo.com", "123-345-1466", "253 Quail St", "Allen", "TX"))

def find_index(email):
    for index, people in enumerate(mydirectory):
        if email == people.email:
            return index

def create_person():
    os.system(clear_vers)
    fname = input("What is the first name? ")
    lname = input("What is the last name? ")
    while True:
        email = input("What is the email? ")
        found = False
        for people in mydirectory:
            if email == people.email:
                print("Email already being used.")
                found = True
            else:
                pass
        if found:
            continue
        else:
            break
    pnum = input("What is the phone number? ")
    address = input("What is the street address? ")
    city = input("What is the city? ")
    state = input("What is the state? ")

    mydirectory.append(Person(fname, lname, email, pnum, address, city, state))
    mydirectory.sort(key=lambda x: (x.lname, x.fname, x.email))
    #mydirectory.sort(key=operator.itemgetter('lname', 'fname'))

    print(f"\n{fname} {lname} has been added to the directory.\n")

def remove_person():
    os.system(clear_vers)
    email = input("Enter the email of the user you want to remove: ")
    index = find_index(email)
    if index:
        print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been removed from the directory.")
        mydirectory.pop(index)

def edit_person():
    os.system(clear_vers)
    email = input("Enter the email of the user you want to edit: ")
    index = find_index(email)
    if index:
        edit = input("What would you like to edit? (firstname, lastname, phone, address, city, state) ")
        if edit == 'firstname':
            mydirectory[index].fname = input("What is the new first name? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
        if edit == 'lastname':
            mydirectory[index].lname = input("What is the new last name? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
        if edit == 'phone':
            mydirectory[index].pnum = input("What is the new phone number? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
        if edit == 'address':
            mydirectory[index].address = input("What is the new street address? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
        if edit == 'city':
            mydirectory[index].city = input("What is the new city? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
        if edit == 'state':
            mydirectory[index].state = input("What is the new state? ")
            print(f"{mydirectory[index].fname} {mydirectory[index].lname} has been modified.")
    else:
        print(f"{email} was not found in the directory.")

def sort_directory():
    os.system(clear_vers)
    while True:
        menu_choice = input("What do you want to sort by? (name, email, city, state) ")

        if menu_choice == "name":
            mydirectory.sort(key=lambda x: (x.lname, x.fname, x.email))
            break
        elif menu_choice == "email":
            mydirectory.sort(key=lambda x: x.email)
            break
        elif menu_choice == "city":
            mydirectory.sort(key=lambda x: (x.city, x.lname, x.lname, x.fname, x.email))
            break
        elif menu_choice == "state":
            mydirectory.sort(key=lambda x: (x.state, x.city, x.lname, x.fname, x.email))
            break
        else:
            continue

def list_directory():
    os.system(clear_vers)
    for people in mydirectory:
        print("{:<20}{:<25}{:<15}{:<25}{:<}".format(people.lname + ', ' + people.fname, people.email, people.pnum, people.address, people.city +', '+ people.state))
    print('\n')

def main_menu():
    return input("What would you like to do? (list, add, remove, edit, sort, quit) ")



while True:

    menu_choice = main_menu()

    if menu_choice == "list":
        list_directory()
    elif menu_choice == "add":
        create_person()
    elif menu_choice == "remove":
        remove_person()
    elif menu_choice == "edit":
        edit_person()
    elif menu_choice == "sort":
        sort_directory()
    elif menu_choice == "quit":
        break
    else:
        continue

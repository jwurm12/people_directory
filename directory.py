import os

clear_vers = 'cls'
mydirectory = []

class Person():

    def __init__(self, fname, lname, email, pnum="", address="", city="", state=""):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pnum = pnum
        self.address = address
        self.city = city
        self.state = state

    def __str__(self):
        return self.lname + ", " + self.fname + " | " + self.email + " | " + self.pnum + " | " + self.address + ", " + self.city + ", " + self.state

    def print_lfname(self):
        return self.lname + ", " + self.fname
    def print_flname(self):
        return self.fname + " " + self.lname
    def print_citystate(self):
        if self.city and self.state:
            return self.city + ", " + self.state
        elif self.city:
            return self.city
        elif self.state:
            return self.state
        else:
            return ""

    def edit_fname(self, fname):
        self.fname = fname.capitalize()
    def edit_lname(self, lname):
        self.lname = lname
    def edit_email(self, email):
        self.email = email
    def edit_pnum(self, pnum):
        self.pnum = pnum
    def edit_address(self, address):
        self.address = address
    def edit_city(self, city):
        self.city = city
    def edit_state(self, state):
        self.state = state

mydirectory.append(Person("Krystal", "House", "kryshouse@geekmail.com", "214-345-2835", "78 Meadowlark Court", "Austin", "TX"))
mydirectory.append(Person("Jack", "Whisky", "jwhisky@gmail.com", "978-876-7121", "7804 FM 2862", "Jersey", "OH"))
mydirectory.append(Person("Joe", "Smith", "jsmith@gmail.com", "234-456-5673", "123 Samson Ln", "Plano", "TX"))
mydirectory.append(Person("Zane", "Hollow", "zaneh@yahoo.com", "123-345-1466", "253 Quail St", "Allen", "TX"))

def find_lengths():
    lengths = [0,0,0]
    for index, people in enumerate(mydirectory):
        if len(people.fname) + len(people.lname) + 4 > lengths[0]:
            lengths[0] = len(people.fname) + len(people.lname) + 4
        if len(people.email) + 2 > lengths[1]:
            lengths[1] = len(people.email) + 2
        if len(people.address) + 2 > lengths[2]:
            lengths[2] = len(people.address) + 2
    return lengths

def find_index(email):
    for index, people in enumerate(mydirectory):
        if email == people.email:
            return index

def create_person():
    os.system(clear_vers)
    while True:
        fname = input("What is the first name? ")
        lname = input("What is the last name? ")
        if fname and lname:
            break
        else:
            print("\nFull name is mandatory.\n")
    while True:
        email = input("What is the email? ")
        if email:
            pass
        else:
            print("\nEmail is mandatory.\n")
            continue
        found = False
        for people in mydirectory:
            if email == people.email:
                print("\nEmail already being used.\n")
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

    mydirectory.append(Person(fname.capitalize(), lname.capitalize(), email.lower(), pnum, address, city.capitalize(), state.upper()))
    mydirectory.sort(key=lambda x: (x.lname, x.fname, x.email))
    #mydirectory.sort(key=operator.itemgetter('lname', 'fname'))

    print(f"\n{fname.capitalize()} {lname.capitalize()} has been added to the directory.\n")

def remove_person():
    os.system(clear_vers)
    email = input("Enter the email of the user you want to remove: ")
    index = find_index(email)
    if index:
        print(f"{mydirectory[index].print_flname()} has been removed from the directory.")
        mydirectory.pop(index)
    else:
        print(f"{email} was not found in the directory.")

def edit_person():
    os.system(clear_vers)
    email = input("Enter the email of the user you want to edit: ")
    index = find_index(email)
    if index:
        edit = input("What would you like to edit? (firstname, lastname, phone, address, city, state) ")
        if edit == 'firstname':
            fname = input("What is the new first name? ")
            mydirectory[index].edit_fname(fname)
        if edit == 'lastname':
            lname = input("What is the new last name? ")
            mydirectory[index].edit_lname(lname)
        if edit == 'phone':
            pnum = input("What is the new phone number? ")
            mydirectory[index].edit_pnum(pnum)
        if edit == 'address':
            address = input("What is the new street address? ")
            mydirectory[index].edit_address(address)
        if edit == 'city':
            city = input("What is the new city? ")
            mydirectory[index].edit_city(city)
        if edit == 'state':
            state = input("What is the new state? ")
            mydirectory[index].edit_state(state)

        print(f"{mydirectory[index].print_flname()} has been modified.")
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
    lengths = find_lengths()
    for people in mydirectory:
        #print("{:<lenghts[0]}{:<lengths[1]}{:<15}{:<lengths[2]}{:<}".format(people.print_lfname(), people.email, people.pnum, people.address, people.print_citystate()))
        print(f"{people.print_lfname():<{lengths[0]}}{people.email:<{lengths[1]}}{people.pnum:<14}{people.address:<{lengths[2]}}{people.print_citystate():<}")
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

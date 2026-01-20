# Command-Line contact book Application

# Adding Contacts
def add_contact():    
    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email: ")
    with open("contacts.txt","a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added Successful")


# View Contacts
def view_contact():
    try:
        with open("contacts.txt","r") as file:
            contacts=file.readlines()
        if not contacts:
            print("No Contact Found.")
            return
        
        print("\n---Saved contacts---")
        for contact in contacts:
            name, phone, email= contact.strip().split(",",2)
            print(f"Name: {name} | Phone: {phone} | Email: {email}")
    except FileNotFoundError:
        print("No Contact file Found,Add Contacts first")
    
#Search contacts
def search_contact():    
    search_name=input("Enter name to search:").lower()
    found=False
    try:
        with open("contacts.txt","r") as file:
            for contact in file:
                name, phone, email=contact.strip().split(",",2)
                if name.lower() == search_name:
                    print(f"Found -> Name:{name},Phone: {phone},Email: {email}")
                    found=True
                    break
        if not found:
            print("contact not Found")
    except FileNotFoundError:
        print("No contact file found.Please Add the Contact First")
    pass

#Contact book Main menu list    
def menu_list():
    while True:
        print(" --------------------")
        print(" |---CONTACT BOOK---|")
        print(" |1. Add Contact    |")
        print(" |2. View Contacts  |")
        print(" |3. Search Contact |")
        print(" |4. Exit           |")
        print(" --------------------")
    
        choice=input("Enter Your Choice from 1 To 4: ")
        
        if choice=="1":
            add_contact()
        elif choice=="2":
            view_contact()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            
            print("****Thanks you for using Contact Book!****")
            break
        else:
            print("****Invalid choice! Please enter a number between 1 and 4****")
menu_list()
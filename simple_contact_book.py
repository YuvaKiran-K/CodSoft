contact ={}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice=int(input(" 1. Add new contact\n 2. Search Contant \n 3. Display Contact \n 4.Edit Contact\n 5. Delete Contact\n 6.Exit\n Enter Your Choice"))
    if choice==1:
        name=input("Enter the Contact Name:")
        phone=input("Enter the Mobile Number:")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter the Contact Name:")
        if search_name in contact:
            print(search_name,"S contact number is ",contact[search_name])
        else:
            print("Name is not found in Contact book")

    elif choice==3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()

    elif choice==4:
        edit_contact =input("Enter the contact to be edited")
        if edit_contact in contact:
            phone=input("Enter Mobile Number")
            contact[edit_contact]=phone
            print("Contact Updated")
            display_contact()

        else:
            print("Name is not found in contact book")

    elif choice==5:
        del_contact=input("Enter the Contact to be deleted")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm=="y" or confirm=="Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in Contact Book")
    else:
        break
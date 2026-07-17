def contact_menu(contacts):
    while True:
        name=input("enter name or (type exit to quit)").strip()
        if name.lower()=="exit":
            print("Goodbye")
            break

        if name in contacts:
            print(f"phone number:{contacts[name]}")
        else:
            print("contact not found")

contacts={
    "alice": 67456668346374,
    "bob":7837777788847,
    "cedric":64644674646
}
contact_menu(contacts)
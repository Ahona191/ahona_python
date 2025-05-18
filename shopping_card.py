shopping_card=[]


while True:
    print("--------Shopping Card Menu--------")
    print("1. Add item")
    print("2. Remove item")
    print("3. View Cart")
    print("4. Checkout and exit")

    choice = input("Enter your choice(1-4):")

    if choice == "1":
        item = input("Enter item to add: ")
        if item in shopping_card:
            print(f"{item} in already added.")
        else:
            shopping_card.append(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_card:
            shopping_card.remove(item)
            print(f"{item} is successfully removed")
        else:
            print(f"{item} not in shopping card")

    elif choice == "3":
        if shopping_card:
            for i in range(len(shopping_card)):
                print(f"{i + 1}  ->{shopping_card[i]}")

        else:
            print("Your shopping card empty!")

    elif choice == "4":
        print("Final card items:", shopping_card)
        print("Thank you!Checking out....")
        break

    else:
        print("Wrong choice!")



print("Happy Shopping!")

shoppingList = []
finished = False
while finished == False:
    aor = input("Would you like to add or remove items, or view the list? ")
    if "ADD" in aor.upper():
        item = input("What would you like to add? ")
        shoppingList.append(item.upper())
        print(item, "was added to the shopping list! ")
    elif "REMOVE" in aor.upper():
        take = input("What would you like to remove? ")
        if take.upper() in shoppingList:
            shoppingList.remove(str(take.upper()))
            print(take, "was successfully removed!")
        else:
            print(take, "is not in your shopping list. ")
    elif "VIEW" in aor.upper():
        i = 1
        print("Shopping list: ")
        for listItem in shoppingList:
            print(str(i) + ":" + listItem)
            i += 1
    elif "FINISH" in aor.upper() or "DONE" in aor.upper():
        finished = True

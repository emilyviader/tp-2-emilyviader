def change():
    expense = 23.75
    money = 100
    
    returned = money - expense
    
    dollars = int(returned)
    cents = int((returned - dollars) * 100)

    print("\nReturned\n")
    print(f"Dollars:\n{dollars}")
    print(f"Cents:\n{cents}")

change()

def get_item(Argument):
    menu = ''
    if Argument == 1:
        menu = '🍔 Cheeseburger'
    elif Argument == 2:
        menu = '🍟 Fries'
    elif Argument == 2:
        menu = '🥤 Soda'
    elif Argument == 2:
        menu = '🍦 Ice Cream'
    else:
        menu = '🍪 Cookie'
    return print(menu + 'complited!, Here you go!')

def welcome():
    print("We have 5 menus!!")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")
    return

if __name__ == "__main__":
    welcome()
    order_number = int(input("Would you like to order? : "))
    get_item(order_number)

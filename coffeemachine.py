from coffee_machine_menu import menu, resources

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def pick_drink():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice




# TODO Print report.
def print_report():
    print(f"Water: {water_remaining}ml")
    print(f"Milk: {milk_remaining}ml")
    print(f"Coffee: {coffee_remaining}g")
    print(f"Money: ${profit}")


# TODO Check resources sufficient?
def check_resources(drink):
    #check resources
    resources_available = True  # default to True, then check each one
    #if not enough resources print
    if water_remaining < menu[drink]['ingredients']['water']: #water_required
        print("Sorry there is not enought water")
        resources_available = False
    if milk_remaining < menu[drink]['ingredients']['milk']: # milk_required:
        print("Sorry there is not enought milk")
        resources_available = False
    if coffee_remaining < menu[drink]['ingredients']['coffee']: #coffee_required:
        print("Sorry there is not enought coffee")
        resources_available = False
    return resources_available



# TODO Process Coins
def process_coins():
    #process coins
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    total = round((quarters * 0.25 + dimes * 0.10 + nickels * 0.05),2)
    return total


# TODO Check Transaction successful
def check_transaction(coins, selection):
    #check transaction
    if coins >= menu[selection]['cost']:
        change_due = round((coins - menu[selection]['cost']),2)
        if change_due > 0:
            print(f"Here is ${change_due} in change.")
        make_coffee = True
    else:
        print("Sorry that's not enough money. Money refunded.")
        make_coffee = False
    return make_coffee



# TODO Make Coffee
def make_coffee(selection):
    print(f"Here is your {selection}. Enjoy!")
    

turn_off = False
selection = ''

resources_list = resources
water_remaining = resources_list['water']
milk_remaining = resources['milk']
coffee_remaining = resources['coffee']
profit = 0

#print(resources_list)
#print(water_remaining)
#print(milk_remaining)
#print(coffee_remaining)
#print(profit)
#print(menu['latte']['ingredients']['water'])

while not turn_off:
    #print(menu['espresso'])
    selection = pick_drink()

    if selection == 'off':
        turn_off = True
    elif selection == 'report':
        print_report()
    else:
        if check_resources(selection):
            coins = process_coins()
            if check_transaction(coins, selection):
                profit += menu[selection]['cost']
                water_remaining -= menu[selection]['ingredients']['water']
                milk_remaining -= menu[selection]['ingredients']['milk']
                coffee_remaining -= menu[selection]['ingredients']['coffee']
                make_coffee(selection)



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    """Prints out all the current ingredient quantities."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def process_coin(quarters, dimes, nickles, pennies):
    """Calculates the total amount collected from the coins."""
    total = 0
    total += (0.25 * quarters)
    total += (0.1 * dimes)
    total += (0.05 * nickles)
    total += (0.01 * pennies)
    return total

def is_resources_sufficient(coffee_kind):
    """Checks if the coffee machine has enough resources, return True if yes, otherwise False."""
    for item in MENU[coffee_kind]["ingredients"]:
        if MENU[coffee_kind]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item} to make {coffee_kind}.")
            return False
        else:
            return True

def check_transaction(coffee_kind, money_collected):
    """Checks if transactions successful or not, return True if yes, otherwise False."""
    cost = MENU[coffee_kind]["cost"]
    if cost <= money_collected:
        if cost < money_collected:
            change = round(money_collected - cost, 2)
            print(f"Here is ${change} in change.")
        return True
    else:
        return False

is_on = True
global profit
profit = 0

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #check if the user input is valid:
    while user_choice not in ["report", "off", "espresso", "latte", "cappuccino"]:
        user_choice = input("Sorry, this is invalid input. Please try again(espresso/latte/cappuccino): ")

    if user_choice == "report":
        print_report()
        print("\n" * 3)
    elif user_choice == "off":
        is_on = False
    else:
        if is_resources_sufficient(user_choice):
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))
            total = process_coin(quarter, dime, nickle, penny)

            if check_transaction(user_choice,total):
                profit += MENU[user_choice]['cost']

                for item in MENU[user_choice]['ingredients']:
                    resources[item] -= MENU[user_choice]['ingredients'][item]
                print(f"Here is your {user_choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        print("\n" * 3)
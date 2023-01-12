import decimal

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def ask_user():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == list(MENU.keys())[0] or user_input == list(MENU.keys())[1] or user_input == list(MENU.keys())[2] or user_input == 'off' or user_input == 'report':
            return user_input
        else:
            print("Incorrect. Try again.")
            return False


def print_report(water, milk, coffee, money):
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money}')


def check_resources(drink, water, milk, coffee):
    drink_needs = (MENU[drink]['ingredients'])
    if water < drink_needs['water']:
        print("Sorry there is not enough water.")
    elif milk < drink_needs['milk']:
        print("Sorry there is not enough milk.")
    elif coffee < drink_needs['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        return True


def ask_for_coins(coin, multiplier):
    while True:
        coin_quantity = input(f'How many {coin}?: ')
        if coin_quantity.isnumeric():
            return int(coin_quantity) * multiplier
        else:
            print("Incorrect number. Try again")
            continue


def process_coins(drink):
    drink_price = MENU[drink]['cost']
    print('Please insert the coins.')
    quarters = ask_for_coins('quarters', 0.25)
    dimes = ask_for_coins('dimes', 0.10)
    nickles = ask_for_coins('nickles', 0.05)
    pennies = ask_for_coins('pennies', 0.01)
    print(round((quarters + dimes + nickles + pennies), 2))


process_coins('latte')


def main():
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while True:
        user_input = ask_user()
        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            pass
        elif user_input == 'off':
            break
        elif user_input == 'report':
            print_report(water, milk, coffee, money)


if __name__ == "__main__":
    pass
    # main()

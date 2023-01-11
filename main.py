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
    pass



print(check_resources('latte', 300, 200, 100))

def main():
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while True:
        user_input = ask_user()
        if user_input == 'espresso':
            pass
        elif user_input == 'latte':
            pass
        elif user_input == 'cappuccino':
            pass
        elif user_input == 'off':
            break
        elif user_input == 'report':
            print_report(water, milk, coffee, money)


if __name__ == "__main__":
    # main()

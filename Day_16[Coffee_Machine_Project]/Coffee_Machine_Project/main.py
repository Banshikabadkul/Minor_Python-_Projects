print("Hello World!")
from resource_file import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def drink_enough(drink) :
    for item in drink:
        if drink[item] > resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True


def display_report():
    print(f"Water : {resources['water']} ml")
    print(f"Milk : {resources['milk']} ml")
    print(f"Coffee : {resources['coffee']} gm")
    print(f"Money : ${profit} ")

def pay_process():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.50
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transac(pay,drink):
    drink_cost = drink['cost']
    if drink_cost > pay:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(pay - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True

def make_coffee(coffee, material):
    for item in material:
        resources[item] -= material[item]
    print(f"Here is your {coffee} ☕️. Enjoy!")

is_on = True
while(is_on):
    choice = input("🙂 What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        display_report()

    elif choice == "off":
        is_on = False
        break
    else:
        drink = MENU[choice]
        if drink_enough(drink['ingredients']):
            # check drink and ask for coin input
            pay = pay_process()

            if transac(pay, drink):
                make_coffee(choice, drink['ingredients'])


#  ##Create a new repository on the command line

#  git init
#  git add README.md
#  git commit -m "first commit"


# // git remote remove origin
# // remote -v   
# // git branch -M main  
# // git remote add origin https://github.com/Banshikabadkul/Hotels.git
# // git push -u origin main
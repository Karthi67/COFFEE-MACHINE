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
def reduce():
    resources["water"] -= MENU[a]["ingredients"]["water"]
    resources["milk"] -= MENU[a]["ingredients"]["milk"]
    resources["coffee"] -= MENU[a]["ingredients"]["coffee"]
def another():
        resources["water"] -= MENU[a]["ingredients"]["water"]
        resources["coffee"] -= MENU[a]["ingredients"]["coffee"]
def money():
    b=int(input("enter penny"))
    b=b*0.01
    c=int(input("enter nickel"))
    c=c*0.05
    d=int(input("enter dime"))
    d=d*0.10
    e=int(input("enter quarter"))
    e=e*0.25
    f=b+c+d+e
    change=MENU[a]["cost"] 
    if change > f:
        print("NO")
    else:
        global left
        left=f-change
        print(f"Here is your {a} ☕️. Enjoy!")
    print(float(left))
   
def possible():
    change=MENU[a]["cost"] 
    if change > left:
        print("NO")
    else:
        change=left-change
        print(f"Here is your {a} ☕️. Enjoy!")
    
    
    
def ask():   
    global a
    a=input("What would you like? (espresso/latte/cappuccino)")
ask()
if a=="report":
    print(resources)
elif a=="espresso":
    money() 
    another()
    print(resources)
elif a=="latte" or "cappuccino":
    money()
    reduce()
    print(resources)
ask()
if a=="report":
    print(resources)
elif a=="espresso":
    possible()
    another()
elif a=="latte" or "cappuccino":
    possible()
    reduce()
    

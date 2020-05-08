# creates a function that displays information when a user doesn't select any of the given options
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# this function is where we prompt the user for information on what size drink they want
def get_size():
    # input function is how we get user information and store that value in a variable
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    # create a set of conditionals that return a string when a user selects a drink option
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    elif res == "d":
        return "x-large"
    elif res == "e":
        return "xx-large"
    # if a user doesnt select any of the given option, the else conditional will return
    # the print_message() function will run and then we follow it up with redirecting them back to the get_size() function 
    else:
        print_message()
        return get_size()

# create a function to get the type of drink the user wants 
def get_drink_type():
    res = input("What type of drink would you like?  \n[a] Brewed coffee \n[b] Mocha \n[c] Latte \n>")
    if res == "a":
        return "brewed coffee"
    elif res == "b":
        return "mocha"
    # if they select option[c] latte then we will return a special function that inquiries about additional options to add to their latte
    elif res == "c":
        return order_latte()
    # this conditional runs if the user didnt select any of the available options
    else:
        print_message()
        return get_drink_type()

# if the user selects latte, then we will direct them to this function that inquiries about what type of milk they want added!
def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")
    if res == "a":
        return "latte"
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print_message()
        return order_latte()

def type_of_cup():
    res = input("Would you like a plastic cup or your own reusable cup? \n[a] plastic \n[b] reusable \n>")
    if res == "a":
        return "plastic"
    elif res == "b":
        return "reusable"
    else:
        print_message()
        return type_of_cup()

def type_of_order():
    res = input("Is this order for here to go? \n[a] in-store \n[b] to-go \n>")
    if res == "a":
        return "in-store"
    elif res == "b":
        return "to go"
    else:
        print_message()
        return type_of_order()

def get_donation_amount():
    res = input("How much would you like to donate? \n[a] $2 \n[b] $5 \n[c] $10 \n>")
    if res == "a":
        return 2
    elif res == "b":
        return 5
    elif res == "c":
        return 10
    else:
        print_message()
        return get_donation_amount()

# this function runs to prompt the user if they would like to donate
def ask_for_donation():
    res = input("Would you like to donate today? \n[a] Yes \n[b] No \n>")
    # if the user selects when asked to donate, we will return a special function to retrieve more information (how much they want to donate)
    if res == "a":
        return get_donation_amount()
        # if the user chooses to not donate, we will set the donation amount to be zero
    else:
        return 0

def hot_or_iced():
    res = input("Do you want your drink iced or hot? \n[a] hot \n[b] iced \n>")
    if res == "a":
        return "hot"
    if res == "b":
        return "iced"
    else:
        print_message()
        return hot_or_iced()

def pastry_option():
    res = input("What type of pastry would you like? \n[a] stroopwaffel \n[b] coffeecake \n[c] scones \n[d] bagel \n>")
    if res == "a":
        return "stroopwaffels! my fave!"
    elif res == "b":
        return "provide a function to ask if they want coffeecake to be warmed up or not"
    elif res == "c":
        return "scone"
    elif res == "d":
        return "bagel"
    else:
        print_message()
        return pastry_option()

#this function runs to retrieve information on whether the user wants a pastry
def offer_pastry():
    res = input("Would you like a pastry? \n[a] yes \n[b] no \n>")
    # if user selects yes then the pastry_option() will run to present them with pastry menu options to select
    if res == "a":
        return pastry_option()
    elif res == "b":
        return "None. What do you mean you're not hungry?"
    else:
        print_message()
        return offer_pastry()

def payment_method():
    res = input("How would you like to pay? \n[a] VISA/MASTERCARD \n[b] apple pay \n[c] google pay \n>")
    if res == "a":
        return "VISA/MASTERCARD"
    elif res == "b":
        return "apple pay"
    elif res == "c":
        return "google pay"
    else:
        print_message()
        return payment_method()

# this function calculates the total including sales tax and donation
def total_amount(donation_choice):
    # calculate the total amount = total amount + 1.08 (sales tax) + donation
    subtotal = 13
    # rounds the total
    total = round((subtotal * 1.08) + donation_choice,2)
    return total

# this is the main function
def coffee_bot():
    # This is where the bot makes the introduction and summarizes the order
    print("Welcome to the cafe!")
    print("Can I take your order?")
    # we set the user responses to variables that we can use for when we summarize the order 
    size = get_size()
    drink_type = get_drink_type()
    cup = type_of_cup()
    order = type_of_order()
    temp = hot_or_iced()
    donation_choice = ask_for_donation()
    pastry = offer_pastry()
    total = total_amount(donation_choice)
    payment = payment_method()
# what our chatbot returns after taking the order
    print(f"Alright, that's a {size} {drink_type}! You chose to use a {cup} and that you want your drink served {temp}.")
    name = input("Can I get your name please? ")
    print(f"Your order is set to: {order}")
    print(f"Donation Choice: ${donation_choice}")
    print(f"Payment Method: {payment}")
    print(f"Did you choose a pastry?: {pastry}")
    print(f"Your total is: ${total}")
    print(f"Thanks, {name}! Your drink will be ready shortly.")
    

coffee_bot()


 

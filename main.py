from re import S


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if(size == "S"):
    bill = bill + 25
    
    if(add_pepperoni == "Y"):
        bill = bill + 2
    else:
        bill = bill + 0

    if(extra_cheese == "Y"):
        bill = bill + 1 
    else:
        bill = bill + 0

elif(size == "M"):
    bill = bill + 20
    
    if(add_pepperoni == "Y"):
        bill = bill + 3
    else:
        bill = bill + 0

    if(extra_cheese == "Y"):
        bill = bill + 1 
    else:
        bill = bill + 0

elif(size == "L"):
    bill = bill + 25
    
    if(add_pepperoni == "Y"):
        bill = bill + 3
    else:
        bill = bill + 0

    if(extra_cheese == "Y"):
        bill = bill + 1 
    else:
        bill = bill + 0
        
print("Your final bill is: $" + str(bill))
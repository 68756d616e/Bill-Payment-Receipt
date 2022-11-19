# Pizza Bill Generator
print("Welcome to Python Moon Pizza!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza = 0

if size == "S":
    pizza = 15
    print("Small pizza will cost $15")
elif size == "M":
    pizza = 20
    print("Medium pizza will cost $20")
else:
    pizza = 25
    print("Large pizza will cost $25")

if add_pepperoni == "Y":
    pizza = pizza + 3
    print("Pepperoni will cost $3 additionaly")
else:
    pizza = pizza + 0
    print("No Pepperoni, no additional charge")

if extra_cheese == "Y":
    pizza = pizza + 3
    print("Extra cheese is an additional charge of $3")
else:
    pizza = pizza + 0
    print("no extra cheese, no additional charge")

    #if size == "S":
#    pizza += 15
#    print("A small pizza will cost $15")
#elif size == "M":
#    pizza += 20
#    print("A small pizza will cost $20")
# You dont have to finish with a else, you could finish with a elif
#elif size == "M":
#    pizza += 20
#    print("A small pizza will cost $20")
#else:
#    pizza += 25
#    print("A small pizza will cost $25")


#if add_pepperoni == "Y":
#    if size == "S":
#        pizza += 2
#    else:
#        pizza += 3
# else:
#    pizza += 0

#if extra_cheese == "Y":
#    pizza += 1


print(f"Your total bill is ${pizza}")

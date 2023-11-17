petrol=True
petrol_per_litre=220
diesel_per_litre=190

if petrol:
    print("petrol is sold at Ksh.",petrol_per_litre)
    quanitity=input('How many litres do you want? ')
    result=int(quanitity) * int(petrol_per_litre)
    print('You have orderd',quanitity,'litres of','PETROL','and you are to pay a total of Ksh.',result)

else:
    print('diesel is sold at Ksh.',diesel_per_litre)
    quanitity=input('How many litres do you want? ')
    result=int(quanitity) * int(diesel_per_litre)
    print('you have ordered',quanitity,'litres of diesel @ Ksh.',diesel_per_litre,"you are to pay A TOTAL OF Ksh.",result)
# в следующих трех строчках определен диапазон лет разных периодов в виде списков
young = list(range(17, 70, 1)) 
old = list(range(70, 91, 1))
too_old = list(range(91, 121, 1))

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: ")
               
if user_age == 16:
    print(user_name, ", you need to wait one year")
elif user_age in young:
    print("Welcome,", user_name, ", on our website!")
elif user_age in old:
    print("You are lucky,", user_name, ", and welcome!")
elif user_age in too_old:
    print(user_name, ", are you sure?")
elif user_age >= 121:
    print("You are not real,", user_name, ".")
else:
    print("I'm sorry,", user_name, ", you are too young!")

    

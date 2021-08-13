import random
    
letters = ['a', 'b', 'c' , 'd', 'e' , 'f' , 'g', 'h', 'i' ,'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_number = random.choices(letters, k = 10)
print("You Password is: ")
print(random_number)


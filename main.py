# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
input_len = len(names)

final_name = random.randint(0,input_len-1)

print(f"{names[final_name]} is going to buy the meal today")

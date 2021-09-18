######## Method 1 ########
userinput = input("What is you name ")

count = 0

for i in userinput:
    count = count + 1

print(f"You have {count} letters in your name")
############################
######## Method 2 ##########

print(f"You have {len(userinput)} letters in your name")
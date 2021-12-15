# Write a program to print pattern just like below
# *
# * *
# * * *
# * * * *
# * * * * *


character = "*"

# i = 1
# while i<=5:
#     j=1
#     while j<=i:
#         print(character,end=" ")
#         j+=1
#     print()
#     i+=1

#Assignment :
# Write a program to print pattern just like below
# * * * * * 
# * * * * 
# * * *
# * * 
# * 

# i = 1
# while i<=5:
#     j=1
#     while j <= 6-i:
#         print(character,end=" ")
#         j+=1
    
#     print()
#     i+=1

i = 1
while i <= 5 :
    j = 5
    while j >= i:
        print(character, end = " ")
        j -= 1
    print()
    i += 1











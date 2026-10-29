import random

list1 = [
    "What is your name",
    "What are you doing",
    "How can this be possible",
    "What a joke",
    "I think you can level up"
]
ra = random.randint(1, 4)
char = list1[ra]
# char = input("Enter: ")
# print(type(char))
lst = list(char.lower())
lst[3], lst[7] = lst[7], lst[3]
lst.append(lst[1])
lst.append(lst[2])
lst.insert(0,lst[3])
lst.reverse()
# print(lst2)
char1 = "".join(lst)
print("Guess the sentence:")
print(char1)
inp = input("")
if (inp == char or inp == char.lower()):
    print("You guessed it right!!!")
    exit()
else:
    print("Ohh no... your guess was wrong")
a = input("Want to decode? (Type Yes or No): ")
if(a=="Yes" or a=="yes"):
    lst.reverse()
    lst1 = lst[1:-2]
    lst1[7], lst1[3] = lst1[3], lst1[7]
    # print(lst1)
    char2 = "".join(lst1)
    print(char2)
else:
    exit()
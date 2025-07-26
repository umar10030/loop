n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n + 1):
    sum = sum+i
    print("\nsum =", sum)

    # Activity 2
    # reverse a string
string = input("Enter a word to reverse: ")

string2 = ('')
for i in string:
    string2 = i + string2
print("\norignal string:", string)
print("reversed string:", string2) 

# Activity 3
# reverse oder
n = int(input("Enter the value of n: "))
print("numbers from{0}to{1} are:".format(n, 1))

for i in range(n, 0, -1):
    print(i)
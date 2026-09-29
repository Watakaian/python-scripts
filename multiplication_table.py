prompt = input("Enter a valid whole number: ")

while not prompt.isdigit() or prompt == "0":
    print("Invalid input, please enter a value above 0")
    prompt = input("Enter a valid whole number: ")

num = int(prompt)

for o in range(1, num + 1):
    for i in range(1, num + 1):
        print(f"{o * i:4}", end=" ")
    print()

# using while loop
"""
o = 1
while o <= num:
    i = 1
    while i <= num:
        print(f"{o * i:4}", end=" ")
        i += 1

    print()
    o += 1

"""

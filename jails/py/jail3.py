from string import ascii_letters

x = input()

for chr in x:
    if chr in ascii_letters:
        print("Not allowed")
        exit(1)

print(eval(x))
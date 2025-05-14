#No danger function,no chr,Try to hack me!!!!
#Try to read file ./flag
BANLIST = ['__loader__', '__import__', 'compile', 'eval', 'exec', 'chr']
eval_func = eval
for m in BANLIST:
    del __builtins__.__dict__[m]
del __loader__, __builtins__
def filter(s):
    not_allowed = set('"\'`')
    print(not_allowed)
    return any(c in not_allowed for c in s)
WELCOME = '''
  _                _                           _       _ _   _                _ _  _   
 | |              (_)                         (_)     (_) | | |              | | || |  
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| | || |_ 
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ |__   _|
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |  | |  
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|  |_|  
              __/ |                          _/ |                                      
             |___/                          |__/                                                                                                                                             
'''
print(WELCOME)
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
while True:
    try:
        input_data = input("> ")
        if filter(input_data):
            print("Oh hacker!")
        print('Answer: {}'.format(eval_func(input_data)))
    except Exception as e:
        print(e)

# open(bytes([102, 108, 97, 103, 46, 116, 120, 116]).decode()).read()
# used str2i tool to convert "flag.txt" into int
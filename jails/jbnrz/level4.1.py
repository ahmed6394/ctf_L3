# Answer: #No danger function,no chr,Try to hack me!!!!
#Try to read file ./flag
BANLIST = ['__loader__', '__import__', 'compile', 'eval', 'exec', 'chr','input','locals','globals','bytes']
my_eval_func_ABDC8732 = eval
my_input_func_001EC9GP = input
for m in BANLIST:
    del __builtins__.__dict__[m]
del __loader__, __builtins__
def filter(s):
    not_allowed = set('"\'`')
    return any(c in not_allowed for c in s)
WELCOME = '''
  _                _                           _       _ _   _                _ _  _  __
 | |              (_)                         (_)     (_) | | |              | | || |/_ |
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| | || |_| |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ |__   _| |
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |  | |_| |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|  |_(_)_|
              __/ |                          _/ |
             |___/                          |__/                                                                        
'''
print(WELCOME)
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
print("Banned __loader__,__import__,compile,eval,exec,chr,input,locals,globals,bytes and `,\",' Good luck!")
input_data = my_input_func_001EC9GP("> ")
if filter(input_data):
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(my_eval_func_ABDC8732(input_data)))
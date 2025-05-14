WELCOME = '''
  _                _                           _       _ _   _                _ ____  
 | |              (_)                         (_)     (_) | | |              | |___ \ 
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| | __) |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ ||__ < 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|____/ 
              __/ |                          _/ |                                     
             |___/                          |__/                                                                                       
'''
 
print(WELCOME)
#the length is be limited less than 7
#it seems banned some payload 
#Can u escape it?Good luck!
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if len(input_data)>7:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))


# help() --> +
# !/bin/sh --> cat "flag.txt"
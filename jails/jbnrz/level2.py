WELCOME = '''
  _                _                           _       _ _   _                _ ___  
 | |              (_)                         (_)     (_) | | |              | |__ \ 
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| |  ) |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ | / / 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |/ /_ 
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|____|
              __/ |                          _/ |                                    
             |___/                          |__/                                                                            
'''
 
print(WELCOME)
 
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if len(input_data)>13:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

# breakpoint()
# import os
# os.system("bash")
#---------------------------
# eval(input())
# __import__("os").system("cat flag")

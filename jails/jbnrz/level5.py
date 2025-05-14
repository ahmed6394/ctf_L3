#It's an challenge for jaillevel5 let's read your flag!
import load_flag
flag = load_flag.get_flag()
def main():
    WELCOME = '''
  _                _                           _       _ _ _                _ _____
 | |              (_)                         (_)     (_) | |              | | ____|
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | _____   _____| | |__
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | |/ _ \ \ / / _ \ |___ \
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | |  __/\ V /  __/ |___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_|_|\___| \_/ \___|_|____/
              __/ |                          _/ |
             |___/                          |__/                                                                        
'''
    print(WELCOME)
    print("It's so easy challenge!")
    print("Seems flag into the dir()")
    repl()
def repl():
    my_global_dict = dict()
    my_global_dict['my_flag'] = flag
    input_code = input("> ")
    complie_code = compile(input_code, '<string>', 'single')
    exec(complie_code, my_global_dict)
if __name__ == '__main__':
    main()

# breakpoint()
# import os
# os.system("cat flag.tx")
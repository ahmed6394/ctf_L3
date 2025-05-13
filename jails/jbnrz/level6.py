import sys
 
def my_audit_hook(my_event, _):
    WHITED_EVENTS = set({'builtins.input', 'builtins.input/result', 'exec', 'compile'})
    if my_event not in WHITED_EVENTS:
        raise RuntimeError('Operation not permitted: {}'.format(my_event))
 
def my_input():
    dict_global = dict()
    while True:
      try:
          input_data = input("> ")
      except EOFError:
          print()
          break
      except KeyboardInterrupt:
          print('bye~~')
          continue
      if input_data == '':
          continue
      try:
          complie_code = compile(input_data, '<string>', 'single')
      except SyntaxError as err:
          print(err)
          continue
      try:
          exec(complie_code, dict_global)
      except Exception as err:
          print(err)
 
 
def main():
  WELCOME = '''
  _                _                           _       _ _   _                _   __
 | |              (_)                         (_)     (_) | | |              | | / /
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| |/ /_
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ | '_ \
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ | (_) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|\___/
              __/ |                          _/ |
             |___/                          |__/                                                                        
  '''
 
  CODE = '''
  dict_global = dict()
    while True:
      try:
          input_data = input("> ")
      except EOFError:
          print()
          break
      except KeyboardInterrupt:
          print('bye~~')
          continue
      if input_data == '':
          continue
      try:
          complie_code = compile(input_data, '<string>', 'single')
      except SyntaxError as err:
          print(err)
          continue
      try:
          exec(complie_code, dict_global)
      except Exception as err:
          print(err)
  '''
 
  print(WELCOME)
 
  print("Welcome to the python jail")
  print("Let's have an beginner jail of calc")
  print("Enter your expression and I will evaluate it for you.")
  print("White list of audit hook ===> builtins.input,builtins.input/result,exec,compile")
  print("Some code of python jail:")
  print(CODE)
  my_input()
 
if __name__ == "__main__":
  sys.addaudithook(my_audit_hook)
  main()
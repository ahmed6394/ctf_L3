import ast
import sys
import os
 
WELCOME = '''
 
    _       _ _   _                _                         _                _ ______
   (_)     (_) | | |              (_)                       | |              | |____  |
    _  __ _ _| | | |__   ___  __ _ _ _ __  _ __   ___ _ __  | | _____   _____| |   / /
   | |/ _` | | | | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__| | |/ _ \ \ / / _ \ |  / /
   | | (_| | | | | |_) |  __/ (_| | | | | | | | |  __/ |    | |  __/\ V /  __/ | / /
   | |\__,_|_|_| |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|    |_|\___| \_/ \___|_|/_/
  _/ |                        __/ |
 |__/                        |___/
 
'''
 
def verify_ast_secure(m):
  for x in ast.walk(m):
    match type(x):
      case (ast.Import|ast.ImportFrom|ast.Call|ast.Expr|ast.Add|ast.Lambda|ast.FunctionDef|ast.AsyncFunctionDef|ast.Sub|ast.Mult|ast.Div|ast.Del):
        print(f"ERROR: Banned statement {x}")
        return False
  return True
 
 
def exexute_code(my_source_code):
  print("Pls input your code: (last line must contain only --HNCTF)")
  while True:
    line = sys.stdin.readline()
    if line.startswith("--HNCTF"):
      break
    my_source_code += line
 
  tree_check = compile(my_source_code, "input_code.py", 'exec', flags=ast.PyCF_ONLY_AST)
  if verify_ast_secure(tree_check):
    print("check is passed!now the result is:")
    compiled_code = compile(my_source_code, "input_code.py", 'exec')
    exec(compiled_code)
  print("Press any key to continue")
  sys.stdin.readline()
 
 
while True:
  os.system("clear")
  print(WELCOME)
  print("=================================================================================================")
  print("==           Welcome to the calc jail beginner level7,It's AST challenge                       ==")
  print("==           Menu list:                                                                        ==")
  print("==             [G]et the blacklist AST                                                         ==")
  print("==             [E]xecute the python code                                                       ==")
  print("==             [Q]uit jail challenge                                                           ==")
  print("=================================================================================================")
  ans = (sys.stdin.readline().strip()).lower()
  if ans == 'g':
     print("=================================================================================================")
     print("==        Black List AST:                                                                      ==")
     print("==                       'Import,ImportFrom,Call,Expr,Add,Lambda,FunctionDef,AsyncFunctionDef  ==")
     print("==                        Sub,Mult,Div,Del'                                                    ==")
     print("=================================================================================================")
     print("Press any key to continue")
     sys.stdin.readline()
  elif ans == 'e':
    my_source_code = ""
    exexute_code(my_source_code)
  elif ans == 'q':
    print("Bye")
    quit()
  else:
    print("Unknown options!")
    quit()
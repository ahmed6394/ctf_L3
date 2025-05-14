clsss = "".__class__.__base__.__subclasses__()

for i, c in enumerate(clsss):
    try:
        if 'system' in c.__init__.__globals__:
            print(i, c)
    except:
        pass

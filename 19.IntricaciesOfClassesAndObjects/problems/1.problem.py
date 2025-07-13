def fun():
    print("Everthing is an object")    
print(dir(55))
print(dir(fun))
print((5).__add__(6))
print((-5.67).__abs__())
d=globals()
print(d)
d['fun'].__call__()
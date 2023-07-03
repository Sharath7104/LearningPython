intvariable = 10
floatvariable = 10.15
stringvariable = "Hello world"
booleanvariable = True
listvariable = [1,2,3]
tuplevariable = (4,5,6)
dictionaryvariable = {"name" : "Sharath", "age" : 26}
setvariable =  {7,8,9}


variables = [intvariable, floatvariable, stringvariable, booleanvariable, listvariable, tuplevariable,dictionaryvariable,setvariable]

for var in variables:
     print(f"Type of {var}: {type(var)}, value: {var}")




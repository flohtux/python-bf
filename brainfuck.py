code=[]

# Read program file character by character
file = open("helloworld.bf", 'r')
while True:
    char = file.read(1)          
    if not char: 
        break
    code.append(char)
file.close()

print(code)

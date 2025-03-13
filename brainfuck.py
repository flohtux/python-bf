code=[]
data=[0]
pointer=0
output=""

# Read program file character by character
file = open("helloworld.bf", 'r')
while True:
    char = file.read(1)          
    if not char: 
        break
    if char in ['+', '-', '.', '>', '<']:
        code.append(char)
file.close()

def run_bf(listOfChars):
    global code, data, pointer, output
    for char in code:
        match char:
            case '+':
                data[pointer]=data[pointer]+1
            case '-':
                data[pointer]=data[pointer]-1
            case '>':
                pointer+=1
                if (pointer >= len(data)):
                    data.append(0)
            case '>':
                pointer-=1
            case '.':
                output += chr(data[pointer])

run_bf(code)
print(data)
print(pointer)
print(output)

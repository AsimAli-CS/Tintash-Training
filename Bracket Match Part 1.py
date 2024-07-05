
file_path = 'input.txt'


lines = []
with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())


    print(type(lines[4]))

def check(a):
    if a==")" : return 3
    elif a == "]" : return 57
    elif a == "}" : return 1197
    elif a == ">" : return 25137

file_line=2
while(lines[file_line]!=""):
    stack=[]
    a=lines[file_line]
    i=0
    sum=0
    check1=0
    count=0
    while i<len(a):
        if a[i]=="{" or a[i]=="[" or a[i]=="(" or a[i]=="<":
            stack.append(a[i])

        elif a[i] == "}" or a[i] == "]" or a[i] == ")" or a[i] == ">":
            if stack:
                top_stack = stack[-1]
                if a[i] == "}" and top_stack == "{":
                    stack.pop()
                elif a[i] == "]" and top_stack == "[":
                    stack.pop()
                elif a[i] == ")" and top_stack == "(":
                    stack.pop()
                elif a[i] == ">" and top_stack == "<":
                    stack.pop()
                else:
                    val = check(a[i])
                    if val is not None:
                        check1 += val
                        count=1
        i+=1
    if stack:
        print(f"{a} is Corrupted lines")
    if not stack:
        if count == 1:
            print(f"{a} is Corrupted lines {check1}")
        else:
            print(f"{a} is Valid lines")

    file_line+=1


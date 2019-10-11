def validity(para):
    d={'(':')','[':']','{':'}'}
    stack=[]
    for i in para:
        if i in d:
            stack.append(i)
        elif(len(stack)==0 or d[stack.pop()]!=i):
             return False
    return len(stack)==0

str=input()
print(validity(str))

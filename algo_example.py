def multipleOrNumber(i):
    output = ""
    if(i%3==0):
        output = 'Hello '
    if(i%5==0):
        output += 'World '
    if(i%7==0):
        output += 'Yoo'
    if output:
        return output
    return i

def getSequence(n):
    for i in range(1, n+1):
        print(multipleOrNumber(i))
    
if __name__ == "__main__":
    getSequence(100)
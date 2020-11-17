'''

Powers of Two
HIDE QUESTION
Have the function PowersofTwo(num) take the num parameter being passed which will be an integer and return the string true if it's a power of two. If it's not return the string false. For example if the input is 16 then your program should return the string true but if the input is 22 then the output should be the string false.

Use the Parameter Testing feature in the box below to test your code with different arguments.


"2"

'''

def PowersofTwo(num): 
    i = 0
    while 2**(i)<=num:
        if 2**i == num:
            return 'true'
        i +=1
    return 'false'   

    
# keep this function call here  
print PowersofTwo(raw_input())
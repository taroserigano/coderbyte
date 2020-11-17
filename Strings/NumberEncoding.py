'''

Number Encoding
HIDE QUESTION
Have the function NumberEncoding(str) take the str parameter and encode the message according to the following rule: encode every letter into its corresponding numbered position in the alphabet. Symbols and spaces will also be used in the input. For example: if str is "af5c a#!" then your program should return 1653 1#!.

Use the Parameter Testing feature in the box below to test your code with different arguments.



"abc"

'''

def NumberEncoding(astr): 
    a_pos = ord('a')
    z_pos = ord('z')
    A_pos = ord('A')
    Z_pos = ord('Z')
    
    print(a_pos, z_pos,A_pos,Z_pos)


    ret_str = ''
    for i in astr:
        i_pos = ord(i)
        if i_pos in range(a_pos,z_pos+1):
            print(i_pos ,  a_pos +1)
            ret_str += str(i_pos - a_pos +1) + " "
        elif i_pos in range(A_pos,Z_pos+1):
            ret_str += str(i_pos-A_pos+1)
        else:
            ret_str += i
    return ret_str
    
# keep this function call here  
print NumberEncoding(raw_input())
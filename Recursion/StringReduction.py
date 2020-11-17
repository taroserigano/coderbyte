'''

String Reduction
HIDE QUESTION
Have the function StringReduction(str) take the str parameter being passed and return the smallest number you can get through the following reduction method. The method is: Only the letters a, b, and c will be given in str and you must take two different adjacent characters and replace it with the third. For example "ac" can be replaced with "b" but "aa" cannot be replaced with anything. This method is done repeatedly until the string cannot be further reduced, and the length of the resulting string is to be outputted.

For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc"). The reduction is done so the output should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final string "ac" is reduced to "b" so the output should be 1.

Use the Parameter Testing feature in the box below to test your code with different arguments.


"[abcabc]"

'''




def StringReduction(str): 
    str = list(str)
    cSet = set(['a','b','c'])
    repeat = True
    while repeat:
      i = 0
      repeat = False
      print(len(str))
      while i < len(str)-1: 
        print(i)
        if str[i] != str[i+1]: # if next char is not THE SAME
          print(list(cSet-set([str[i],str[i+1]])) )
          str[i:i+2] = list(cSet-set([str[i],str[i+1]])) 
          repeat = True
        else:
          i += 1
    return len(str)
    
print(StringReduction("cccc"))
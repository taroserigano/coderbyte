'''

Remove Brackets
HIDE QUESTION
Have the function RemoveBrackets(str) take the str parameter being passed, which will contain only the characters "(" and ")", and determine the minimum number of brackets that need to be removed to create a string of correctly matched brackets. For example: if str is "(()))" then your program should return the number 1. The answer could potentially be 0, and there will always be at least one set of matching brackets in the string.

Use the Parameter Testing feature in the box below to test your code with different arguments.



"(()))"



'''

def RemoveBrackets(str):
    count = 0
    noright = 0 
     
    for i in str:
      if i == '(':
        count += 1
      elif i == ')':
        if count == 0:
          noright += 1  
        else:
          count -= 1
    noright = noright + count

    return noright
      # code goes here 
    # return str
    
# keep this function call here  
print RemoveBrackets(raw_input())
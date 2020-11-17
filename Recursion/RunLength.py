'''

Run Length
HIDE QUESTION
Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.

Use the Parameter Testing feature in the box below to test your code with different arguments.





"aabbcc"

'''



def RunLength(str):
  
  cur_letter = str[0]
  compressed =''
  count = 0

  for s in str:
    if s == cur_letter:
      count += 1
    else:
      compressed += "%s%s" % (count, cur_letter)
      cur_letter = s
      count = 1
  compressed += "%s%s" % (count, cur_letter)    


  # code goes here
  return compressed 

# keep this function call here 
print RunLength(raw_input())
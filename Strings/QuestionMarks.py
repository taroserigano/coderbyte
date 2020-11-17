'''
Questions Marks
HIDE QUESTION
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Use the Parameter Testing feature in the box below to test your code with different arguments.
""arrb6???4xxbl5???eee5""

'''
def QuestionsMarks(str): 

  nums = []
  pos = []
  countThree = False
  
  for char in range(0,len(str)): 
    
    if str[char].isdigit(): # check if digit or not
      nums.append(str[char])  # store characters
      pos.append(char)    # store numbers
  print(nums) 
  print(pos) 

  for x in range(0, len(nums)): 
    if int(nums[x]) + int(nums[x-1]) == 10: # calculate 10
      if str[pos[x-1]+1 : pos[x]].count('?') == 3: # count THREE ?
        countThree = True
      else: return 'false'  
  
  if countThree == True:
    return 'true'
  else:
    return 'false'  

print QuestionsMarks(raw_input())
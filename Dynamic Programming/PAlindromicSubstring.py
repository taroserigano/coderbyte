'''


Palindromic Substring
Have the function PalindromicSubstring(str) take the str parameter being passed and find the longest palindromic substring, which means the longest substring which is read the same forwards as it is backwards. For example: if str is "abracecars" then your program should return the string racecar because it is the longest palindrome within the input string.

The input will only contain lowercase alphabetic characters. The longest palindromic substring will always be unique, but if there is none that is longer than 2 characters, return the string none.
Examples
Input: "hellosannasmith"
Output: sannas
Input: "abcdefgg"
Output: none


["(1,2)", "(2,4)", "(7,2)"]



'''

def PalindromicSubstring(str):

  x = len(str)

  for i in range(0, x-2):
    for j in range(0, i+1):
      test = str[j: x+j -i]
      
      if test == test[::-1]:
        return test

  # code goes here
  return 'none'

# keep this function call here 
print PalindromicSubstring(raw_input())
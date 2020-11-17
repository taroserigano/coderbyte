'''


Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.

Use the Parameter Testing feature in the box below to test your code with different arguments.

'''
def MinWindowSubstring(strArr):

  n = strArr[0] 
  k = strArr[1]
  substring_list = []

  for i in range(len(n) - len(k)):   #12
     
    for j in range(i+len(k), len(n)):
      substring = n[i:j]
      tmp_k = list(k) # words between i loop and j loop
      

      for letter in substring:
        if letter in tmp_k:
          tmp_k.remove(letter)
      if len(tmp_k)==0:
        substring_list.append(substring)
        break
  
  final_substring = strArr[0]
  for substring in substring_list:
    if len(substring)< len(final_substring):
      final_substring = substring

  # code goes here
  return final_substring

# keep this function call here 
print MinWindowSubstring(raw_input())
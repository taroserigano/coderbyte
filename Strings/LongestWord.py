'''
Longest Word
HIDE QUESTION
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

Use the Parameter Testing feature in the box below to test your code with different arguments.

"hello world"

'''
def LongestWord(sen):

  # code goes here

  arr = ""
  container =[]
  
  for word in sen:
    if not word.isalpha():
      word = ' '
    container.append(word)
  longest = ''
  return ''.join(container).split()
  for word in ''.join(container).split():
    if len(word) > len(longest):
      longest = word  
  return longest  



'''

String Periods
HIDE QUESTION
Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, your program should return the string -1.

Use the Parameter Testing feature in the box below to test your code with different arguments.


"abcababcababcab"



'''


def StringPeriods(strParam):

  # code goes here
  new_string = strParam

  for i in range(len(strParam)-1):
    new_string = new_string[:-1]

    if len(strParam) % len(new_string) == 0:
      if new_string * int(len(strParam) / len(new_string)) == strParam:
        return new_string


    

  return -1

# keep this function call here 
print StringPeriods(raw_input())
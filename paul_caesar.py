#!/usr/bin/env

import string
import sys

string.ascii_lowercase

def caesar_decipher (rotation, text):
  answer = ''
  for t in text:
      t = t.lower()
      if t in string.ascii_lowercase:
          string.ascii_lowercase.index(t)
          index += 13
#          if index >= 26:
#              index = index - 26

          answer += string.ascii_lowercase[index]
      else:
          answer += t

  return answer

if __name__ == '__main__':
    rotation = int(sys.argv[1])
    text = sys.argv[2]
    answer = caesar_decipher(rotation, text)
    print("answer: {}".format(answer))

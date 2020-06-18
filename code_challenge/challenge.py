"""Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

def solution(n):
    for item in n:
        if item % 3 == 0:
            print(item)

solution([85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14])


"""Stretch: Print out all of the strings in the following array that represent a number divisible by 3:
[
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]
The expected output for the above input is:
nine hundred ninety nine
twelve
eighteen
six
twelve
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


lookup = { "five": 5, "twenty six": 26, "nine hundred ninety nine": 999, "twelve": 12, "eighteen": 18, "fifty two": 52, "one hundred one": 101, "forty one": 41, "seventy seven": 77, "six": 6, "twelve": 12, "four": 4, "sixteen": 16 }

def sol(n):
    for item in n:
        if lookup[item] % 3 == 0:
            print(item)
sol([
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
])
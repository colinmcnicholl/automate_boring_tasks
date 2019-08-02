import re

"""How would you write a regex that matches a sentence where the first word
is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive."""

firstWordRegex = re.compile(r'^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\s*.$', re.IGNORECASE)
print(firstWordRegex.search('Alice eats apples.'))
print(firstWordRegex.search('Bob pets cats.'))
print(firstWordRegex.search('Carol throws baseballs.'))
print(firstWordRegex.search('Alice throws Apples.'))
print(firstWordRegex.search('BOB EATS CATS.'))
print(firstWordRegex.search('Robocop eats apples.'))
print(firstWordRegex.search('ALICE THROWS FOOTBALLS.'))
print(firstWordRegex.search('Carol eats 7 cats.'))
#Patrick Atwater
#Just a super simple script that does the trick. Note the top 20 != 20 b/c of equivalent counts. See you thurs. Cheers, PA

import collections

with open('C:\users\patwater\documents\github\DS-LA-03\src\lesson01\whispers.csv') as f:
	print collections.Counter(line.split()[-1] for line in f)

# Which returns 

"""
Counter({'"': 354, ':)"': 22, ';)"': 18, '<3"': 8, ':("': 8, 'lol"': 7, 'you."': 5, 'you"': 5, 'me"': 4, 'me?"': 4, 'me.
"': 4, 'out"': 4, ':D"': 4, 'her"': 3, 'shit"': 3, 'it."': 3, 'them"': 3, '!"': 3, '."': 3, 'guys."': 2, 'saying."': 2,
'here"': 2, 'yourself"': 2, 'that..."': 2, 'guy"': 2, 'it"': 2, ':/"': 2, 'it!"': 2, 'you?"': 2, 'book?"': 2, 'too"': 2,
 'up!"': 2, 'do"': 2, 'alone"': 2, 'not"': 2, 'too."': 2, 'true"': 2, 'leave"': 2, 'attractiveness)."': 2, ':P"': 2, '</
3"': 2, 'M23"': 2, 'stfu"': 2, ':c"': 2, 'happen"': 2, 'for"': 2, 'it?"': 2, '..."': 2, 'this"': 2, 'app"': 2, 'real."':1....
"""
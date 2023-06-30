#!/usr/bin/python3

import argparse, re
from itertools import permutations as perms

charsLower = 'qwertyuipasdfghjkzxcvbnm'
dict_file = './5letterwords'

# This positional character analysis was performed against the dictionary included with Ubuntu.
# For each nth character in a word, the likelihood of the nth character pX_precedence[n] is shown below, most to least likely.
p1_precedence='sbctpamldfgrhwenkojviyuqz'
p2_precedence='aoeiurlhntpymcwdsbvkgxzfq'
p3_precedence='arinolesutmdcgbpvkywfzxhj'
p4_precedence='eantliorsdckgmpuhybfvwzxj'
p5_precedence='seydtrnalhkoipmgcfxwzubvj'

separator = '-='

def custom_sort():
    return ( p1_precedence, p2_precedence, p3_precedence, p4_precedence, p5_precedence )

try:
    with open(dict_file, 'r') as f:
        five_letter_words = f.read()
except Exception as e:
    print(f"The '{dict_file}' dictionary file doesn't exist.")
    raise
    exit(1)
else:
    five_letter_words = set(five_letter_words.rstrip().split(';'))
    # print(five_letter_words)
finally:
    pass

parser = argparse.ArgumentParser(
		description="Suggest words for wordle. pX can be a single char, char class/range, or negated char class/range.",
		epilog = ""
		)

parser.add_argument(
	"--p1",
	type=str,
	default = charsLower, # p1_precedence,
	help="Position 1 character set."
	)

parser.add_argument(
	"--p2",
	type=str,
	default = charsLower, #p2_precedence,
	help="Position 2 character set."
	)

parser.add_argument(
	"--p3",
	type=str,
	default = charsLower, #p3_precedence,
	help="Position 3 character set."
	)

parser.add_argument(
	"--p4",
	type=str,
	default = charsLower, #p4_precedence,
	help="Position 4 character set."
	)

parser.add_argument(
	"--p5",
	type=str,
	default = charsLower, #p5_precedence,
	help="Position 5 character set."
	)

parser.add_argument(
	"-c",
	"--contains",
	type=str,
	default = '',
	help="Optional. Char(s) that must appear in guess."
	)

args = parser.parse_args()

the_match_regex = rf"[{args.p1}][{args.p2}][{args.p3}][{args.p4}][{args.p5}]"
the_match_regex = re.compile(the_match_regex)
# print(the_match_regex)

print(f"\n{separator * 10} GUESSES {separator[::-1] * 10}")

sorted_word_list = \
        sorted(\
            list(filter(the_match_regex.match, five_letter_words)), \
            key = lambda e: (e[0],e[1],e[2],e[3],e[4]) #(p1_precedence, p2_precedence, p3_precedence, p4_precedence, p5_precedence)
        )

if len(args.contains) > 0:
	the_contains_regex = []
	for _ in perms(args.contains):
		the_contains_regex.append(f".*{'.*'.join(_)}.*")

	the_contains_regex = rf"{'|'.join(the_contains_regex)}"
	the_contains_regex = re.compile(the_contains_regex)
	# print(the_contains_regex)
	word_list_with_contains = \
        sorted(\
            list(filter(the_contains_regex.match, sorted_word_list)), \
            key = lambda e: (e[0],e[1],e[2],e[3],e[4]) #(p1_precedence, p2_precedence, p3_precedence, p4_precedence, p5_precedence)
        )
	sorted_word_list = word_list_with_contains

for eachMatch in sorted_word_list:
	print(eachMatch)
	pass

print(f"{separator * 12} {separator[::-1] * 12}")

exit(0)


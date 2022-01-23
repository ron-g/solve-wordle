#!/usr/bin/python3

import argparse, re

charsLower = 'qwertyuipasdfghjkzxcvbnm'
charsUpper = 'QWERTYUOPASDFGHJKLZXCVBNM'
dict_file = './5letterwords'

# This positional character analysis was performed against the dictionary included with Ubuntu.
# For each nth character in a word, the likelihood of the nth character pX_precedence[n] is shown below, most to least likely.
p1_precedence='sbctpamldfgrhwenkojviyuqz'
p2_precedence='aoeiurlhntpymcwdsbvkgxzfq'
p3_precedence='arinolesutmdcgbpvkywfzxhj'
p4_precedence='eantliorsdckgmpuhybfvwzxj'
p5_precedence='seydtrnalhkoipmgcfxwzubvj'

separator = '-='

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

parser = argparse.ArgumentParser(description="Suggest words for wordle. pX can be a single char, char class/range, or negated char class/range.")

parser.add_argument(
	"--p1",
	type=str,
	default = p1_precedence,
	help="Position 1 character set."
	)

parser.add_argument(
	"--p2",
	type=str,
	default = p2_precedence,
	help="Position 2 character set."
	)

parser.add_argument(
	"--p3",
	type=str,
	default = p3_precedence,
	help="Position 3 character set."
	)

parser.add_argument(
	"--p4",
	type=str,
	default = p4_precedence,
	help="Position 4 character set."
	)

parser.add_argument(
	"--p5",
	type=str,
	default = p5_precedence,
	help="Position 5 character set."
	)

args = parser.parse_args()

the_regex = rf"[{args.p1}][{args.p2}][{args.p3}][{args.p4}][{args.p5}]"
the_regex = re.compile(the_regex)
# print(the_regex)

print(f"\n{separator * 10} GUESSES {separator[::-1] * 10}")

for match in sorted(list(filter(the_regex.match, five_letter_words)), key = lambda e: (p1_precedence, p2_precedence, p3_precedence, p4_precedence, p5_precedence)):
    print(match)

print(f"{separator * 12} {separator[::-1] * 12}")

exit(0)

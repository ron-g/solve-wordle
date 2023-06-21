#!/usr/bin/python3

import argparse, re
from tkinter import *
from tkinter import scrolledtext

charsLower = 'qwertyuipasdfghjkzxcvbnm'
charsUpper = 'QWERTYUOPASDFGHJKLZXCVBNM'
dict_file = './5letterwords'
charsLower = 'a-z'
separator = '-='

# This positional character analysis was performed against the dictionary included with Ubuntu.
# For each nth character in a word, the likelihood of the nth character pX_precedence[n] is shown below, most to least likely.
p1_precedence='sbctpamldfgrhwenkojviyuqz'
p2_precedence='aoeiurlhntpymcwdsbvkgxzfq'
p3_precedence='arinolesutmdcgbpvkywfzxhj'
p4_precedence='eantliorsdckgmpuhybfvwzxj'
p5_precedence='seydtrnalhkoipmgcfxwzubvj'

guess_num = 1
pad = 10
input_width = 40

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


def getGuesses():
	global ch1_input
	global ch2_input
	global ch3_input
	global ch4_input
	global ch5_input
	global guess_num

	# guesses_label['text'] = f"{ch1_input.get()},{ch2_input.get()},{ch3_input.get()},{ch4_input.get()},{ch5_input.get()}"


	the_regex = rf"[{ch1_input.get()}][{ch2_input.get()}][{ch3_input.get()}][{ch4_input.get()}][{ch5_input.get()}]"
	guesses = f"{separator * 3} «GUESS #{guess_num}» {separator[::-1] * 3}\n«{the_regex}»\n"
	print(f"RegEx:'{the_regex}' \U0001F449 ", end='')
	the_regex = re.compile(the_regex)
	guess_num += 1

	sorted_word_list = \
		sorted(\
			list(filter(the_regex.match, five_letter_words)), \
			key = lambda e: (e[0],e[1],e[2],e[3],e[4]) #(p1_precedence, p2_precedence, p3_precedence, p4_precedence, p5_precedence)
		)

	for match in sorted_word_list:
		guesses += f"{match}\n"

	if len(sorted_word_list) == 1:
		isPlural = ''
	else:
		isPlural = 'es'

	print(f"{len(sorted_word_list)} match{isPlural}")
	guesses += f"\n«{len(sorted_word_list)} match{isPlural}»\n{separator * 6}{separator[::-1] * 6}\n\n"

	# guesses_label['text'] = guesses
	# text_area.delete(0,END)
	text_area.insert(END, guesses)

def resetAll(event):
	# .bind('<Control-x>', quit_program)
	global guess_num
	global ch1_input
	global ch2_input
	global ch3_input
	global ch4_input
	global ch5_input

	guess_num = 1

	ch1_input.delete(0, END)
	ch1_input.insert(END, charsLower)

	ch2_input.delete(0, END)
	ch2_input.insert(END, charsLower)

	ch3_input.delete(0, END)
	ch3_input.insert(END, charsLower)

	ch4_input.delete(0, END)
	ch4_input.insert(END, charsLower)

	ch5_input.delete(0, END)
	ch5_input.insert(END, charsLower)

	# guesses_label['text'] = ''

	text_area.delete(0.0, END)

	ch1_input.focus()

def clearGuesses():
	guesses_label['text'] = ''

def quitApp(event):
	canvas.destroy()


canvas = Tk()
canvas.title("Solve Wordle")
# canvas.iconbitmap('./solve_wordle.bmp')
canvas.iconphoto(False, PhotoImage(file='./solve_wordle.png'))

canvas.bind('<Control-r>', resetAll)
canvas.bind('<Control-q>', quitApp)
# root.geometry('500x400')

input_frame = LabelFrame(
	canvas, 
	text = 'RegEx Inputs', 
	padx = pad, 
	pady = pad, 
	font = ("Arial Black", 14)
	)
input_frame.pack(
	padx = pad, 
	pady = pad,
	fill = "both",
	expand = "yes"
	)

guess_frame = LabelFrame(
	canvas, 
	text = 'Guesses', 
	padx = pad, 
	pady = pad, 
	font = ("Arial Black", 14)
	)
guess_frame.pack(
	padx = pad, 
	pady = pad,
	fill = "both",
	expand = "yes"
	)

ch1_label = Label(
	input_frame, 
	text = "Character 1:", 
	padx = pad, 
	pady = pad
	)

ch1_label.grid(column=1, row=1)
ch1_input = Entry(input_frame, width = input_width)
ch1_input.insert(END, charsLower)
ch1_input.grid(column=2, row=1)
ch1_input.focus()

ch2_label = Label(
	input_frame, 
	text = "Character 2:", 
	padx = pad, 
	pady = pad
	)
ch2_label.grid(column=1, row=2)
ch2_input = Entry(input_frame, width = input_width)
ch2_input.insert(END, charsLower)
ch2_input.grid(column=2, row=2)

ch3_label = Label(
	input_frame, 
	text = "Character 3:", 
	padx = pad, 
	pady = pad
	)
ch3_label.grid(column=1, row=3)
ch3_input = Entry(input_frame, width = input_width)
ch3_input.insert(END, charsLower)
ch3_input.grid(column=2, row=3)

ch4_label = Label(
	input_frame, 
	text = "Character 4:", 
	padx = pad, 
	pady = pad
	)
ch4_label.grid(column=1, row=4)
ch4_input = Entry(input_frame, width = input_width)
ch4_input.insert(END, charsLower)
ch4_input.grid(column=2, row=4)

ch5_label = Label(
	input_frame, 
	text = "Character 5:", 
	padx = pad, 
	pady = pad
	)
ch5_label.grid(column=1, row=5)
ch5_input = Entry(input_frame, width = input_width)
ch5_input.insert(END, charsLower)
ch5_input.grid(column=2, row=5)

guesses_button = Button(
	input_frame, 
	text = "Get Wordle guesses.", 
	command = getGuesses, 
	padx = pad, 
	pady = pad
	)
guesses_button.bind('<Control-g>', getGuesses)
guesses_button.grid(
	column = 1, 
	row = 6, 
	columnspan = 2, 
	padx = pad, 
	pady = pad
	)

text_area = scrolledtext.ScrolledText(guess_frame, 
									  wrap = WORD, 
									  width = 30, 
									  height = 20, 
									  font = ("Courier New",12)
									  )

# text_area.insert(END, 'Guesses will appear here.')
text_area.grid(
	column = 1,
	row = 8,
	padx = 10,
	pady = 10,
	columnspan = 2
	)

canvas.mainloop()
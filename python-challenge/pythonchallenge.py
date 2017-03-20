#Question 0
def question_1():
	print "q1: " + str(2**38)

#Question 2
#http://www.pythonchallenge.com/pc/def/map.html
def question_1():
	string_2 = "map"
	alphabet_2 = "abcdefghijklmnopqrstuvwxyzab.(.)')  "
	alphabet_2 = list(alphabet_2)
	list_2 = string_2.split()

	output_2 = []

	for word in list_2:
		new_word = []
		word_list_2 = list(word)
		for letter in word_list_2:
			index = alphabet_2.index(letter) + 2
			new_word.append(alphabet_2[index])
		print new_word
		output_2.append("".join(new_word))
	print " ".join(output_2)

def question_2():
	replace = "%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++"

	f = open("q2_input.txt","r")
	text = f.read()
	text = text.replace("\n","")

	text_list = list(text)
	i = 0
	for letter in text_list:
		if letter in replace:
			text_list[i] = ""
		i += 1
	print "".join(text_list)

#http://www.pythonchallenge.com/pc/def/equality.html
def question_3():
	f = open("q3_input.txt","r")
	text = f.read()
	text = text.replace("\n","")

	text_list = list(text)

	i = 0
	small_letters = []
	while i < len(text_list) - 9:
		substring = text_list[i:i+9]
		i += 1
		l1 = substring[0]
		l2 = substring[1]
		l3 = substring[2]
		l4 = substring[3]
		l5 = substring[4]
		l6 = substring[5]
		l7 = substring[6]
		l8 = substring[7]
		l9 = substring[8]

		if l1.islower() and l2.isupper() and l3.isupper() and l4.isupper() and l5.islower() and l6.isupper() and l7.isupper() and l8.isupper() and l9.islower():
			small_letters.append(l5)
			print "".join(substring)
		else:
			substring = []

	print "".join(small_letters)

	# big_start = 0
	# little = 0
	# big_finish = 0
	# letters = []
	# for letter in text_list:
	# 	if big_start == 3 and big_finish == 3 and little == 1:
	# 		print "finish"
	# 		print "".join(letters)
	# 	elif letter.isupper and big_start < 3:
	# 		big_start += 1
	# 		letters.append(letter)
	# 		print "add to start"
	# 	elif big_start == 3 and letter.islower and big_finish == 0 and little == 0:
	# 		little = 1
	# 		letters.append(letter)
	# 		print "add little"
	# 	elif big_start == 3 and little == 1 and letter.isupper and big_finish < 3:
	# 		big_finish += 1
	# 		letters.append(letter)
	# 	if big_start > 3 or little > 1 or big_finish > 3:
	# 		big_start = 0
	# 		little = 0
	# 		big_finish = 0
	# 		letters = []
	# 		print "reset"


#http://www.pythonchallenge.com/pc/def/linkedlist.php
def question_4():
	pass





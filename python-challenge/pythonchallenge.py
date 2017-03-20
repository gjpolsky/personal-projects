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

	text_list = split(text)

	big_start = 0
	little = 0
	big_finish
	for letter in text_list:
		if big_start > 3:
			big_start = 0
		if !letter.islittle and big_start < 3:
			big_start += 1
		if big_start == 3 and letter.islittle and big_finish == 0:
			little = 1
		if big_start == 3 and little == 1:
			big_finish += 1
		if big_start == 3 and big_finish == 3 and little == 1:
			

question_3()






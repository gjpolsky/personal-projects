import urllib
import lxml.html
import re
import pickle
import pickletools

#Question 0
def question_0():
	print "q1: " + str(2**38)


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
	replace = ("%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@$*^@$^!+]!&_#)_*}{}}!}_]"
				"$[%}@[{_@#_^{*@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$"
				"[**$&^{$!@#$%)!@(&+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*"
				"&@%$+]!*__(#!*){%&@++")

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

		if (l1.islower() and l2.isupper() and l3.isupper() 
			and l4.isupper() and l5.islower() and l6.isupper() 
			and l7.isupper() and l8.isupper() and l9.islower()):
			small_letters.append(l5)
			# print "".join(substring)
		else:
			substring = []

	print "".join(small_letters)


#http://www.pythonchallenge.com/pc/def/linkedlist.php
def question_4():
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
	
	key = 8022
	while urllib.urlopen(url):
		url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(key)
		f = urllib.urlopen(url)
		f = f.read()
		
		try:
			subindex = f.index("and the next nothing is")
			substring = f[subindex:]
		except ValueError, e:
			print f
			print key
			break

		try:
			key = re.search(r"\d+",substring).group(0)
		except AttributeError, e:
			print key
			break


#http://www.pythonchallenge.com/pc/def/peak.html
def question_5():
	f = open("banner.p", "rb")
	unpickled_file = pickle.load(f)

	for row in unpickled_file:
		print "".join([key * value for key, value in row])


#http://www.pythonchallenge.com/pc/def/channel.html
def question_6():
	pass

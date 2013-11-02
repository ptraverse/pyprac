from subprocess import call
import re
import requests

def letternames(letter,num_names):
	r = requests.get('http://deron.meranda.us/data/census-dist-female-first.txt')
	data = r.text
	patt = re.compile(r"""[A-Z]  # First letter capital
			      \w +   # As many letters lowercase""", re.X)			
	names = re.findall(patt,  data)
	ret_list = []
	i = 0;	
	for name in names:
		if name.startswith(letter.upper()):
			if (i<=num_names):
 				ret_list.append(name)
				i += 1
	return ret_list

a_names = letternames('a',4)
for name in a_names:
 	print name

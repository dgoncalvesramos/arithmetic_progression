import requests
from bs4 import BeautifulSoup
import re

def extract_arithmetic_progression(html): 
	soup = BeautifulSoup(html.text, 'html.parser')
	regex =  '\[ \-?\d+ (\+|\-) Un \] (\+|\-) \[ n \* \-?\d+ \]'
	text = soup.get_text()
	print(text)
	match = re.search(regex,text)
	return match.group()

def extract_u0(html):
	soup = BeautifulSoup(html.text, 'html.parser')
	regex =  '-?\d+\n'
	text = soup.get_text()
	match = re.search(regex,text)
	return match.group()

def extract_u_to_find(html):
	soup = BeautifulSoup(html.text, 'html.parser')
	regex =  'U[1-9]\d+'
	text = soup.get_text()
	match = re.search(regex,text)
	return match.group()

def calculate_solution(arithmetic_progression,u0,u_to_find):
	Un=u0
	n='0'
	iteration=u_to_find[1:len(u_to_find)]
	iteration=int(iteration)
	ar_without_brackets=re.sub('\[','(',arithmetic_progression)
	ar_without_brackets_res=re.sub('\]',')',ar_without_brackets)
	while(iteration != 0) :
		Un=str(Un)
		n=str(n)
		res_str=re.sub('Un',Un,ar_without_brackets_res)
		res_str2=re.sub('n',n,res_str)
		Un=eval(res_str2)
		n=int(n)
		n+=1
		iteration-=1
	print('The result is ' + str(Un))	
	return Un

def send_result(result,session):
	url = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='
	r = requests.get(url+str(result),cookies=session)
	print(r.text)

url = 'http://challenge01.root-me.org/programmation/ch1/'
r = requests.get(url)
session = r.cookies	
result = calculate_solution(extract_arithmetic_progression(r),
extract_u0(r), 
extract_u_to_find(r)
)
send_result(result,session)

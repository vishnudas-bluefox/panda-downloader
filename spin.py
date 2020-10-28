from time import sleep

def spin(a):
	for x in range(a):
 	   for frame in r'-\|/-\|/':
 	   	print('\b', frame, sep='', end='', flush=True)
 	   	sleep(0.2)
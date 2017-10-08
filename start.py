import mp
import time
def print_nilai(lista):
	print lista
	time.sleep(1)
	mp.End()
		

args = []
for i in range(0,10):
	args.append([i,'hallo','s'])

mp.Task(print_nilai,args)
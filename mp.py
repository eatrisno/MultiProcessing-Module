import multiprocessing as mp
import time
#Eko Aprili Trisno
#2017 10 07
#work at ADSKOM INDONESIA
#variable add __variable (problem incase same variable)

#to use
#you need create array of args
#ex : args = [[var1,str1,var3],[var2,str2,var3]]
#
#Task(function,args_arr,max_processor,wait_max_process_time)
#
#for i in range(0,10):
#	args.append([i,'hallo','s'])
#mp.Task(print_nilai,args)
#NB, you need add .End_Tag at bottom your function
#def a(args):
#	print(args[0])
#	mp.End()

__max_process = mp.cpu_count()
__mgr = mp.Manager()
__var = __mgr.dict()
__var['process']=0
__task_list = []
__wait_time = 0.1

def Task(function,args_arr,max_process=__max_process,wait_time=__wait_time):
	print('Max Processor : {0}'.format(__max_process))	
	for args in args_arr:
		__var['process']+=1
		#hold if process reach max limit
		while(__var['process'] > __max_process):
			time.sleep(__wait_time)
		#run process
		p = mp.Process(target=function , args=[args])
		__task_list.append(p)
		p.start()
		#join job process
	for task in __task_list:
		task.join()

def End():
	__var['process']-=1
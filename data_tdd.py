import datetime
from plyer import notification as nn
import webbrowser
from test_not import *
from win10toast_click import ToastNotifier
tt=ToastNotifier()

def notifiction_rem(title,msg,d,t):
	tt.show_toast("Click here to turn off reminder",title+" on "+d+" at "+t+'\n'+"message :"+'"'+msg+'"',icon_path="bell.ico",duration=25,threaded=False,callback_on_click=test)
	
def notifiction_rem_not(title,msg):
	tt.show_toast("Click here to turn off reminder",title+" : "+'"'+msg+'"',icon_path="bell.ico",duration=25,threaded=False,callback_on_click=test)
def time_compare(l,l1,file_time,current_time):
	n=0
	if int(file_time[0])<int(current_time[0]) or (l[2][-2:]=='AM' and l1[-1][-2:]=='PM') or ((int(file_time[0])==int(current_time[0])) and (int(file_time[1])<int(current_time[1]))):
		return 0
	for i in range(0,len(l[2])):
		if l[2][i]!=l1[1][i]:
			n=1
			break
	if n==0:
		return 1

	return 2
def date_time_compare(file_date,current_date,l,l1,file_time,current_time):
	title="You missed a reminder"
	tt="Reminder"
	n=0
	if int(file_date[-1])<int(current_date[-1]):
		notifiction_rem(title,l[0],l[1],l[2])
	elif (int(file_date[-1]) == int(current_date[-1])) and (int(file_date[1]) < int(current_date[1])):
		notifiction_rem(title,l[0],l[1],l[2])
	elif (int(file_date[-1]) == int(current_date[-1])) and (int(file_date[1]) == int(current_date[1])) and (int(file_date[0]) < int(current_date[0])):
		notifiction_rem(title,l[0],l[1],l[2])
	elif (int(file_date[-1]) == int(current_date[-1]))  and (int(file_date[1]) == int(current_date[1])) and (int(file_date[0]) == int(current_date[0])):
		if time_compare(l,l1,file_time,current_time)==1:	
			notifiction_rem_not(tt,l[0])
		elif time_compare(l,l1,file_time,current_time)==2:
			pass
		else:
			notifiction_rem(title,l[0],l[1],l[2])
def call_help1(l):
	ik=[]
	kk=""
	for i in range(0,len(l)):
		if l[i]!=":":
			kk=kk+l[i]

		if  l[i]==":" or i==len(l)-4 :
			ik.append(kk)
			kk=""
	return ik

def call_help(l):
	ik=[]
	kk=""
	for i in range(0,len(l)):
		if l[i]!="-":
			kk=kk+l[i]

		if  l[i]=="-" or i==len(l)-1 :
			ik.append(kk)
			kk=""
	return ik
def data_t():		
	f=open("data_rem.txt","r")
	l=[]
	c=0
	k='Hello'
	while k!='':
		l.append(k)
		k=f.readline()
		if k=="" and c==0:
			exit()
		c=c+1	
	f.close()
	l=l[1:len(l)]
	for i in range(0,2):
		l[i]=l[i][0:len(l[i])-1]
	n=datetime.datetime.now()
	l1=[]
	l[2]=l[2].upper()
	l[-1]=l[-1].replace(".","")
	l1.append(n.strftime("%d-%m-%y"))
	l1.append(n.strftime("%I:%M %p"))
	if l1[-1][0]=='0':
		l1[-1]=l1[-1][1:]
	file_date=call_help(l[1])
	current_date=call_help(l1[0])
	file_time=call_help1(l[-1])
	current_time=call_help1(l1[-1])
	date_time_compare(file_date,current_date,l,l1,file_time,current_time)
while True:
	data_t()
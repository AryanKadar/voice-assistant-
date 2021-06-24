import pyttsx3 as pyy
import datetime as dt
import pytz as pz
import time
import webbrowser as wy
import speech_recognition as sr
import wikipedia as wiki
from tkinter import *
en=pyy.init("sapi5")
v=en.getProperty('voices')
en.setProperty("rate",130)
import smtplib
import os
import datetime
from email.message import EmailMessage
from threading import *
class r_n(Thread):
	def run(self):
		import subprocess
		subprocess.call([r'C:\Users\Om\Desktop\fyp\start_rem.bat'])
Email=os.environ.get("My_Email")
Pass=os.environ.get("Password")
msgg=EmailMessage()
msgg['from']=Email
def hf(name1,name,text,rt):
	printt(f"{name1} = Hello {name}, How can i help you ?\n",text,rt)
	spe(f"Hello {name}, How can i help you")
def printt(s,text,rt):
		text.configure(state="normal")
		text.insert(END,"\n"+str(s)+"\n")
		text.see(END)
		rt.update()
		text.configure(state="disabled")	
def printt1(s,text,rt):
		text.configure(state="normal")
		text.insert(END,"\n  "+str(s))
		text.see(END)
		rt.update()
		text.configure(state="disabled")
def too(adu):
	aduu=adu.lower()
	s=""
	aduu=aduu.split(" ")
	for i in aduu:
		s=s+i.lower()
	if "@gmail.com" in s:
		return s
	else:
		return s+"@gmail.com"

def mainn(name1,text,rt,name,l1):
	adu=""
	z=0
	while "bye"!=adu:
			adu=spr(name1,text,rt)
			aduu=adu.lower()
			url='https://www.google.com/search?q='
			url2='&rlz=1C1SQJL_enIN857IN857&oq=python&aqs=chrome..69i57j35i39l2j69i60l5.4395j0j7&sourceid=chrome&ie=UTF-8'

			if "bye" in adu:
				text.configure(state="normal")
				rt.mainloop()
			if "bye" not in adu and "send mail" not in aduu and "pause" not in adu:
				printt(f"{name} = {adu}",text,rt)
			if "change" in adu and "voice" in adu and "assistant" in adu:
				if z==0:
					name1=assi(name1,text,rt)
					z=z+1
				if name1=="David":
					p1 = PhotoImage(file="zara.png")
					l2=Label(rt,image=p1,width=305,height=300)
					l2.place(x=70,y=0)
					rt.update()
					en.setProperty('voice',v[1].id)
					name1="Zara"
					printt(f"{name1} = My name is {name1} and i am your new assistant\n",text,rt)
					spe(f"My name is {name1} and i am your new assistant")
					hf(name1,name,text,rt)
				elif name1=="Zara" :
					p1 = PhotoImage(file="david.png")
					l1=Label(rt,image=p1,width=305,height=300).place(x=70,y=0)
					rt.update()
					en.setProperty('voice',v[0].id)
					name1="David"
					printt(f"{name1} = My name is {name1} and i am your new assistant\n",text,rt)
					spe(f"My name is {name1} and i am your new assistant")
					hf(name1,name,text,rt)
			if "wikipedia"  in aduu:
				aduu=aduu.replace("wikipedia","")
				re=wiki.summary(adu,sentences=2)
				printt(f"{name1} = {re}\n",text,rt)
				spe(re)
			elif "pause" in aduu:
				rt.attributes("-alpha",0.8)
				#h_rt = rt.winfo_height()//2
				#w_rt = rt.winfo_width()//2
				#Label(rt,bg="white",text="Paused").place(x=w_rt-30,y=h_rt-20)
				aww=spr("",text,rt)
				rt.attributes("-alpha",1.0)
			elif "open" in aduu and "youtube" in aduu:
				urll="https://www.youtube.com/results?search_query="
				printt(f"{name1} = What would you like to search ?",text,rt)
				spe("What would you like to search")				
				adu=spr(name1,text,rt)
				printt(f"{name} = {adu}",text,rt)
				wy.get().open_new(urll+adu)
			elif "set" in aduu and "reminder" in aduu:
					mssg=""
					date=""
					time=""
					printt(f"{name1} = What reminder you want to save ?\n",text,rt)
					spe("What reminder you want to save")
					aduu="no"
					while "no" in aduu:	
						mssg=spr(name1,text,rt)
						printt(f"{name} = {mssg}\n",text,rt)	
				
						printt(f"{name1} = Is the reminder message correct ?\n",text,rt)
						spe("Is the reminder message correct")
						adu=spr(name1,text,rt)
						printt(f"{name} = {adu}\n",text,rt)
						aduu=adu.lower()
					
						if "no" in aduu:

							printt(f"{name1} = Then what is the correct message ?\n",text,rt)
							spe("Then what is the correct message")
					aduu="no"
	
					printt(f"{name1} = On what day i should remind you this message ?\n",text,rt)
					spe("On what day i should remind you this message")
					while "no" in aduu:	
						date=spr(name1,text,rt)
					
						printt(f"{name} = {date}\n",text,rt)	
			
			
			
						printt(f"{name1} = Is the date of the reminder is correct ?\n",text,rt)
						spe("Is the date of the reminder is correct")
						adu=spr(name1,text,rt)
						printt(f"{name} = {adu}\n",text,rt)
						aduu=adu.lower()
					
						if "no" in aduu:
					
							printt(f"{name1} = Then what is the correct date ?\n",text,rt)
							spe("Then what is the correct date")
						else:	
							date=datetime.datetime.strptime(date,"%d %B %Y")
							date=date.strftime("%d-%m-%y")
					aduu="no"
		
					printt(f"{name1} = At what time i should remind you this message ?\n",text,rt)
					spe("At what time i should remind you this message")
					while "no" in aduu:	
						time=spr(name1,text,rt)
			
						printt(f"{name} = {time}\n",text,rt)
			
						printt(f"{name1} = Is the time of the reminder is correct ?\n",text,rt)
						spe("Is the time of the reminder is correct")
						adu=spr(name1,text,rt)
						printt(f"{name} = {adu}\n",text,rt)
						aduu=adu.lower()
					
						if "no" in aduu:
				
							printt(f"{name1} = Then what is the correct time ?\n",text,rt)
							spe("Then what is the correct time")

					f=open("data_rem.txt","w")
					f.write(f"{mssg}\n{date}\n{time}")
					f.close()
					t1=r_n()
					t1.start()
					
					#import subprocess
					#subprocess.call([r'C:\Users\Om\Desktop\fyp\start_rem.bat'])
					#printt(f"Reminer has been set. \n",text,rt)
					#spe(f"Reminer has been set")

			elif "open" in aduu and "gmail" in aduu:
				urll="https://www.gmail.com"				
				wy.get().open_new(urll)
			elif "change" in aduu and "name" in aduu:
					printt(f"{name1} = What should i call you ?\n",text,rt)
					spe("What should i call you")
					name=spr(name1,text,rt)
					f1= open("namee.txt", "w")
					f1.write(name)
					f1.close()
					printt(f"{name1} =Your name has been change.",text,rt)
					spe("your name has been change")
					hf(name1,name,text,rt)
					

			elif "open" in aduu and "google" in aduu:
				printt(f"{name1} = What would you like to search ?",text,rt)
				spe("What would you like to search")
				adu=spr(name1,text,rt)
				printt(f"{name} = {adu}",text,rt)
				wy.get().open_new(url+adu+url2)
			elif "time" in aduu:
				if "america" in aduu or "usa" in aduu:
					dtt=pz.timezone('America/Havana')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p"),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,USA"),text,rt)

					dtt=pz.timezone('America/Chicago')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Chicago"),text,rt)

					dtt=pz.timezone('America/Denver')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Denver"),text,rt)

					dtt=pz.timezone('America/Phoenix')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Phoenix"),text,rt)

					dtt=pz.timezone('America/Los_Angeles')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Los Angeles"),text,rt)
				elif "europe" in aduu:
					dtt=pz.timezone('Europe/Berlin')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p"),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Berlin"),text,rt)

					dtt=pz.timezone('Europe/Madrid')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Madrid,Paris,Berlin"),text,rt)


					dtt=pz.timezone('Europe/London')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	London"),text,rt)

					dtt=pz.timezone('Europe/Moscow')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Moscow"),text,rt)
				elif "australia" in aduu:
					dtt=pz.timezone('Australia/Queensland')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p"),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Australia"),text,rt)

					dtt=pz.timezone('Australia/Broken_Hill')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Broken Hill,South"),text,rt)

					dtt=pz.timezone('Australia/Queensland')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Queensland,Sydney"),text,rt)

					dtt=pz.timezone('Australia/West')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	West"),text,rt)
				elif "brazil" in aduu:
					dtt=pz.timezone('Brazil/East')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p"),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Brazil"),text,rt)

					dtt=pz.timezone('Brazil/West')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	West"),text,rt)

					dtt=pz.timezone('Brazil/DeNoronha')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	DeNoronha"),text,rt)

					dtt=pz.timezone('Brazil/East')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	East"),text,rt)
				elif "canada" in aduu :
					dtt=pz.timezone('Canada/Atlantic')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p"),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Canada,Atlantic"),text,rt)

					dtt=pz.timezone('Canada/Atlantic')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Atlantic"),text,rt)

					dtt=pz.timezone('Canada/Pacific')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Pacific"),text,rt)

					dtt=pz.timezone('Canada/Mountain')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Mountain"),text,rt)
				elif "egypt" in aduu:
					dtt=pz.timezone('Egypt')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Egypt"),text,rt)
				elif "hong kong" in aduu:
					dtt=pz.timezone('Hongkong')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Hongkong"),text,rt)
				elif "iceland" in aduu:
					dtt=pz.timezone('Iceland')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Iceland"),text,rt)
				elif "iran" in aduu:
					dtt=pz.timezone('Iran')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Iran"),text,rt)
				elif "israel" in aduu:
					dtt=pz.timezone('Israel')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Israel"),text,rt)
				elif "jamaica" in aduu:
					dtt=pz.timezone('Jamaica')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Jamaica"),text,rt)
				elif "japan" in aduu:
					dtt=pz.timezone('Japan')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Japan"),text,rt)
				elif "libya" in aduu:
					dtt=pz.timezone('Libya')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Libya"),text,rt)
				elif "mexico" in aduu:
					dtt=pz.timezone('Mexico/General')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Mexico"),text,rt)

					dtt=pz.timezone('Mexico/BajaSur')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	BajaSur"),text,rt)

					dtt=pz.timezone('Mexico/BajaNorte')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	BajaNorte"),text,rt)
				elif "singapore" in aduu:
					dtt=pz.timezone('Singapore')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Singapore"),text,rt)
				elif "turkey" in aduu:
					dtt=pz.timezone('Turkey')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Turkey"),text,rt)
				elif "atlantic" in aduu:
					dtt=pz.timezone('Atlantic/Bermuda')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Bermuda,Atlantic"),text,rt)
	
					dtt=pz.timezone('Atlantic/St_Helena')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	St_Helena"),text,rt)

					dtt=pz.timezone('Atlantic/South_Georgia')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	South_Georgia"),text,rt)
				
				elif "portugal" in aduu:
					dtt=pz.timezone('Portugal')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Portugal"),text,rt)

				elif "poland" in aduu:
					dtt=pz.timezone('Poland')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("     %I:%M  %p "),text,rt)
					printt1(rr.strftime("  %B , %d %Y ,Poland"),text,rt)

				elif "asia" in aduu:
					n=dt.datetime.now()
					printt1(n.strftime("     %I:%M %p"),text,rt)
					printt1(n.strftime("  %B , %d %Y ,Time in India"),text,rt)

					dtt=pz.timezone('Asia/Bangkok')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Bangkok"),text,rt)

					dtt=pz.timezone('Asia/Dubai')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Dubai"),text,rt)

					dtt=pz.timezone('Asia/Hong_Kong')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Hong Kong"),text,rt)

					dtt=pz.timezone('Asia/Calcutta')
					rr=dt.datetime.now(dtt)
					printt1(rr.strftime("%I:%M  %p	Calcutta"),text,rt)
				else:
					n=dt.datetime.now()
					printt1(n.strftime("     %I:%M %p"),text,rt)
					printt1(n.strftime("  %B , %d %Y ,Time in India"),text,rt)
				import time
				time.sleep(5)


			elif "send mail" in aduu:
					sub=""
					printt(f"{name} = {aduu}\n",text,rt)
					printt(f"{name1} = To whom do you want to sent mail ?",text,rt)
					spe('To whom do you want to sent mail')
					To=too(spr(name1,text,rt))	
					printt(f"{name} = {To}\n",text,rt)
					printt(f"{name1} = Is the email of person you want to send is correct ?",text,rt)
					spe(f"Is the email of person you want to send is correct")
					adu=spr(name1,text,rt).lower()
					if "no" not in adu:
						printt(f"{name} = {adu}",text,rt)
					while "no" in adu:
						printt(f"{name} = {adu}",text,rt)
						printt(f"{name1} = Then what is correct email ?",text,rt)
						spe(f"Then what is correct email")
						To=too(spr(name1,text,rt))
						printt(f"{name} = {To}\n",text,rt)
						printt(f"{name1} = Is the email you want to send is correct ?",text,rt)
						spe(f"Is the email you want to send is correct")	
						adu=spr(name1,text,rt)
					printt(f"{name} = {aduu}\n",text,rt)
					printt(f"{name1} = What do you want to send ?",text,rt)
					spe('What you want to send')
					aduu=spr(name1,text,rt)
					printt(f"{name} = {aduu}",text,rt)
					printt(f"{name1} = Is content you want to send is correct ?",text,rt)
					spe(f"Is content you want to send is correct")
					adu=spr(name1,text,rt).lower()
					if "no" not in adu:
						printt(f"{name} = {adu}",text,rt)
					while "no" in adu:
						printt(f"{name} = {adu}",text,rt)
						printt(f"{name1} = Then what is correct content ?",text,rt)
						spe(f"Then what is correct content")
						aduu=spr(name1,text,rt)
						printt(f"{name} = {aduu}\n",text,rt)
						printt(f"{name1} = Is content you want to send is correct ?",text,rt)
						spe(f"Is content you want to send is correct")	
						adu=spr(name1,text,rt)
					printt(f"{name1} = Do you want to add subject ?",text,rt)
					spe(f"Do you want to add subject")
					adu=spr(name1,text,rt)
					printt(f"{name} = {adu}",text,rt)
					if "yes" in adu:
						printt(f"{name1} = What is Subject ?",text,rt)
						spe(f"What is Subject")
						sub=spr(name1,text,rt)
						printt(f"{name} = {sub}",text,rt)
						printt(f"{name1} = Is the Subject you want to send is correct ?",text,rt)
						spe(f"Is the Subject you want to send is correct")
						adu=spr(name1,text,rt).lower()
						if "no" not in adu:
							printt(f"{name} = {adu}",text,rt)
						while "no" in adu:
							printt(f"{name} = {adu}",text,rt)
							printt(f"{name1} = Then what is correct a Subject ?",text,rt)
							spe(f"Then what is correct a Subject")
							sub=spr(name1,text,rt)
							printt(f"{name} = {sub}\n",text,rt)
							printt(f"{name1} = Is the Subject you want to send is correct ?",text,rt)
							spe(f"Is the Subject you want to send is correct")	
							adu=spr(name1,text,rt)
					elif "no" in adu:
						pass
					else:
						pass
			
					msgg["To"]=To
					msgg["Subject"]=sub
					msgg.set_content(aduu)
					with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
						smtp.login(Email,Pass)
						smtp.send_message(msgg)
					printt(f"\nEmail Sent to {To}",text,rt)

			
def spe(aud):
	en.say(aud)
	en.runAndWait()
def spr(name1,text,rt):
	if name1!="":
		at=None
		while at==None:
			r1=sr.Recognizer()
			with sr.Microphone() as srr:
				printt("\nListening...\n",text,rt)
				r1.adjust_for_ambient_noise(srr,duration=0.5)
				audio=r1.listen(srr)
			try:
				at=r1.recognize_google(audio,language='en-in')	
				return at
				
			except sr.UnknownValueError as e:
				printt(f"{name1} = I'm Sorry , i didn't catch that ,Can you say that again ?\n",text,rt)
				spe(" I'm Sorry , i didn't catch that ,Can you say that again ")
	else:
		while True:
			r1=sr.Recognizer()
			with sr.Microphone() as srr:

				audio=r1.listen(srr)
			try:
				at=r1.recognize_google(audio,language='en-in')	
				if at=="resume":
					break
				
			except sr.UnknownValueError as e:
				pass
def greet(text,rt,name1):
	name="Anonymous"
	hour=dt.datetime.now().hour
	f=open("namee.txt",'r')
	name=f.read()
	f.close()
	if name=="":	
		if hour>=0 and hour<12:
			printt(f"{name1} = Good Morning\n",text,rt)
			spe("Good Morning")
		elif hour>=12 and hour<18:
			printt(f"{name1} = Good Afternoon\n",text,rt)
			spe("Good Afternoon")
		elif hour>=18 and hour<19:
			printt(f"{name1} = Good Evening\n",text,rt)
			spe("Good Evening")
		else :
			printt(f"{name1} = Hope you had a nice day\n",text,rt)
			spe("Hope you had a nice day")
		printt(f"{name1} = My name is {name1} and i am your assistant\n",text,rt)
		spe(f"My name is {name1} and i am your assistant")
		printt(f"{name1} = What should i call you ?\n",text,rt)
		spe("What should i call you")
		name=spr(name1,text,rt)
		f1= open("namee.txt", "w")
		f1.write(name)
		f1.close()
	hf(name1,name,text,rt)
	return name
def assi(name1,text,rt):
	v1=en.getProperty('voice')
	if v1=='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0':
		printt(f"{name1} = We have Two Assistant Available.Current Assistant is David there is another assistant and that is Zara.Do you wish to change your assistant to Zara ?\n",text,rt)
		spe("We have Two Assistant Available")
		spe("Current Assistant is David")
		spe("there is another assistant and that is Zara")
		spe("Do you wish to change your assistant to Zara")
	else :
		printt(f"{name1} = We have Two Assistant Available.Current Assistant is Zara there is another assistant and that is David.Do you wish to change your assistant to David ?\n",text,rt)
		spe("We have Two Assistant Available")
		spe("Current Assistant is Zara")
		spe("there is another assistant and that is David")
		spe("Do you wish to change your assistant to David")
	while True:
		aduu=spr(name1,text,rt)	
		if "yes"==aduu and v1=='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0':
			return "David"
		elif "no"==aduu and v1=='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0':			
			return "Zara"
		elif "yes"==aduu:
			return "Zara"
		elif "no"==aduu:
			return "David"
		elif aduu!="yes" or aduu!="no":
			printt(f"{name1} = Say 'Yes' for if you want to change your assistant or 'NO' if you dont want to change your assistant\n",text,rt)
			spe("Say 'Yes' for if you want to change your assistant or 'NO' if you dont want to change your assistant ")
def vaa(text,rt,l1):
	v1=en.getProperty('voice')		
	if v1=='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0':
		name1="David"
	else :
		name1="Zara"
	name=greet(text,rt,name1)
	mainn(name1,text,rt,name,l1)
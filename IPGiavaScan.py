import tkinter as tk
from tkinter import ttk
from tkinter import *
import socket
import tcping
import time
import datetime
from tcping import Ping
from PIL import Image

def control(ipaddr1,ipaddr2):
	w.update()
	l=[22,80,135,443,445]
	hostname=""
	variable1=text_input1.get("1.0","end-1c")
	variable2=text_input2.get("1.0","end-1c")
	try:
		variable1=variable1.split(".")
		n1=int(variable1[0])
		n2=int(variable1[1])
		n3=int(variable1[2])
		n4=int(variable1[3])
		v2=variable2.split(".")
		m1=int(v2[0])
		m2=int(v2[1])
		m3=int(v2[2])
		m4=int(v2[3])
	except:
		text_output=tk.Label(w, text="Indirizzo IP non corretto", fg="red",bg="black", font=("Helvetica",12))
		text_output.grid(row=6,column=0)
		return 1
	ipaddr=""
	text_output=tk.Label(w, text="IP:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=0)
	text_output=tk.Label(w, text="Hostname:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=1)
	text_output=tk.Label(w, text="Stato:", fg="#4dd0e1", bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=2)
	x=8
	pb["value"]=20
	w.update()
	while ipaddr!=variable2:
		variable1[0]=str(n1)
		variable1[1]=str(n2)
		variable1[2]=str(n3)
		variable1[3]=str(n4)
		ipaddr=variable1[0]+"."+variable1[1]+"."+variable1[2]+"."+variable1[3]
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		try:
			hostname=socket.gethostbyaddr(ipaddr)
		except:
			hostname="Non disponibile"
		text_output=tk.Label(w, text=hostname, fg="green",bg="black", font=("Helvetica",12))
		text_output.grid(row=x,column=1)
		for n in l:
			result=s.connect_ex((ipaddr,n))
			text_output=tk.Label(w, text=ipaddr, fg="green",bg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=0)
			if result==0:
				break
		if result==0:
			text_output=tk.Label(w, text="Up", fg="green",bg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=2)
		else:
			text_output=tk.Label(w, text="Down", fg="green",bg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=2)
		x+=1
		n=0
		n4+=1
		if n4==256:
			n4=0
			n3+=1
		if n3==256:
			n3=0
			n2+=1
		if n2==256:
			n2=0
			n1+=1
		pb["value"]+=7
		w.update()
	pb["value"]=100
	w.update()

def userinput(variable1,variable2,variable3,variable4):
	w.update()
	l=[]
	variable1=text_input1.get("1.0","end-1c")
	variable2=text_input2.get("1.0","end-1c")
	variable3=text_input3.get()
	variable4=text_input4.get()
	try:
		x3=int(variable3)
		x4=int(variable4)
	except:
		text_output=tk.Label(w, text="Le porte devono essere numeri interi", fg="red",bg="black", font=("Helvetica",12))
		text_output.grid(row=6,column=1)
		return 1
	c=x3
	x4+=1
	d=x4-x3
	count=0
	try:
		variable1=variable1.split(".")
		n1=int(variable1[0])
		n2=int(variable1[1])
		n3=int(variable1[2])
		n4=int(variable1[3])
		v2=variable2.split(".")
		m1=int(v2[0])
		m2=int(v2[1])
		m3=int(v2[2])
		m4=int(v2[3])
	except:
		text_output=tk.Label(w, text="Indirizzo IP non corretto", fg="red",bg="black", font=("Helvetica",12))
		text_output.grid(row=6,column=0)
		return 1
	ipaddr=""
	text_output=tk.Label(w, text="IP:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=0)
	text_output=tk.Label(w, text="Hostname:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=1)
	text_output=tk.Label(w, text="Stato:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=2)
	text_output=tk.Label(w, text="Porta:", fg="#4dd0e1",bg="black", font=("Helvetica",12,"bold"))
	text_output.grid(row=7,column=3)
	x=8
	pb["value"]=20
	w.update()
	while ipaddr!=variable2:
		variable1[0]=str(n1)
		variable1[1]=str(n2)
		variable1[2]=str(n3)
		variable1[3]=str(n4)
		ipaddr=variable1[0]+"."+variable1[1]+"."+variable1[2]+"."+variable1[3]
		while x3!=x4:
			if ipaddr not in l:
				try:
					hostname=socket.gethostbyaddr(ipaddr)
					text_output=tk.Label(w, text="Hostname:", fg="green",bg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=1)
				except:
					hostname="Non disponibile"
				try:
					ping=Ping(ipaddr,x3,30)
					ping.ping(3)
					text_output=tk.Label(w, text=ipaddr, fg="green",bg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=0,padx=50)
					text_output=tk.Label(w, text=hostname, fg="green",bg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=1)
					text_output=tk.Label(w, text=x3, fg="green",bg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=3)
					text_output=tk.Label(w, text="Up", fg="green",bg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=2,padx=30)
					l.append(ipaddr)
				except:
					'''text_output=tk.Label(w, text="Indirizzo IP non raggiungibile", fg="black", font=("Helvetica",12))
					text_output.grid(row=x,column=4)'''
					count+=1
					if count==d:
						text_output=tk.Label(w, text=ipaddr, fg="green",bg="black", font=("Helvetica",12))
						text_output.grid(row=x,column=0,padx=50)
						text_output=tk.Label(w, text=hostname, fg="green",bg="black", font=("Helvetica",12))
						text_output.grid(row=x,column=1)
						text_output=tk.Label(w, text="Down", fg="green",bg="black", font=("Helvetica",12))
						text_output.grid(row=x,column=2,padx=30)
						count=0
			pb["value"]+=7
			w.update()
			x3+=1
			x+=2
		n4+=1
		if n4==256:
			n4=0
			n3+=1
		if n3==256:
			n3=0
			n2+=1
		if n2==256:
			n2=0
			n1+=1
		x3=c
	pb["value"]=100
	w.update()

w=tk.Tk()
w.geometry("1440x1024")
w.title("IP scan")
w.configure(background="black")

ipaddr1=""
ipaddr2=""
p1=0
p2=0

img = Image.open("icon_ipscan1.png")
img=tk.PhotoImage(file="icon_ipscan1.png")
panel=tk.Label(w,image=img,bg="black")
panel.grid(row=1,column=0,padx=40,pady=30)

text_output=tk.Label(w,text="IP iniziale",fg="#4dd0e1",bg="black",font=("Helvetica",12))
text_output.grid(row=1,column=2,padx=20)

text_output=tk.Label(w,text="IP finale",fg="#4dd0e1",bg="black",font=("Helvetica",12))
text_output.grid(row=1,column=4,padx=20)

text_output=tk.Label(w,text="Porta iniziale",fg="#4dd0e1",bg="black",font=("Helvetica",12))
text_output.grid(row=2,column=2,padx=20)

text_output=tk.Label(w,text="Porta finale",fg="#4dd0e1",bg="black",font=("Helvetica",12))
text_output.grid(row=2,column=4,padx=20)

text_input1=tk.Text(w,width=34,height=1)
text_input1.grid(row=1,column=3)

text_input2=tk.Text(w,width=34,height=1)
text_input2.grid(row=1,column=5)


text_input3=tk.Entry(w,width=30)
text_input3.grid(row=2,column=3)

text_input4=tk.Entry(w,width=30)
text_input4.grid(row=2,column=5)

enter_button=tk.Button(w,text="Scan",command=lambda:userinput(ipaddr1,ipaddr2,p1,p2))
enter_button.grid(row=3,column=5,padx=20,pady=20)

enter_button2=tk.Button(w,text="Ping",command=lambda:control(ipaddr1,ipaddr2))
enter_button2.grid(row=3,column=3,padx=20,pady=20)

pb=ttk.Progressbar(w, orient="horizontal", length=300, mode="determinate")
pb.grid(row=5,column=4)
pb["maximum"]=100

w.mainloop()
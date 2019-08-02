import tkinter as tk
from tkinter import *
import socket
import tcping
from tcping import Ping

def userinput(variable1,variable2):
	variable1=text_input1.get("1.0","end-1c")
	variable2=text_input2.get("1.0","end-1c")
	print(variable1)
	print(variable2)
	variable1=variable1.split(".")
	n1=int(variable1[0])
	n2=int(variable1[1])
	n3=int(variable1[2])
	n4=int(variable1[3])
	ipaddr=""
	text_output=tk.Label(w, text="IP:", fg="blue", font=("Helvetica",12))
	text_output.grid(row=4,column=0)
	text_output=tk.Label(w, text="Hostname:", fg="black", font=("Helvetica",12))
	text_output.grid(row=4,column=1)
	text_output=tk.Label(w, text="Stato:", fg="orange", font=("Helvetica",12))
	text_output.grid(row=4,column=2)
	x=5
	while ipaddr!=variable2:
		variable1[0]=str(n1)
		variable1[1]=str(n2)
		variable1[2]=str(n3)
		variable1[3]=str(n4)
		ipaddr=variable1[0]+"."+variable1[1]+"."+variable1[2]+"."+variable1[3]
		text_output=tk.Label(w, text=ipaddr, fg="blue", font=("Helvetica",12))
		text_output.grid(row=x,column=0,padx=50)
		try:
			hostname=socket.gethostbyaddr(ipaddr)
			text_output=tk.Label(w, text="Hostname:", fg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=1)
			text_output=tk.Label(w, text=hostname, fg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=1)
		except:
			text_output=tk.Label(w, text="Non disponibile", fg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=1)
		try:
			ping=Ping(ipaddr,80,60)
			ping.ping(3)
			text_output=tk.Label(w, text="Up", fg="green", font=("Helvetica",12))
			text_output.grid(row=x,column=2,padx=30)
		except:
			'''text_output=tk.Label(w, text="Indirizzo IP non raggiungibile", fg="black", font=("Helvetica",12))
			text_output.grid(row=x,column=4)'''
			text_output=tk.Label(w, text="Down", fg="red", font=("Helvetica",12))
			text_output.grid(row=x,column=2,padx=30)
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
		x+=2

w=tk.Tk()
w.geometry("1000x850")
w.title("IP scan")

ipaddr1=""
ipaddr2=""

text_output=tk.Label(w,text="Inserire IP iniziale",fg="black",font=("Helvetica",12))
text_output.grid(row=1,column=0,padx=50)

text_output=tk.Label(w,text="Inserire IP finale",fg="black",font=("Helvetica",12))
text_output.grid(row=2,column=0,padx=50)

text_input1=tk.Text(w,width=30,height=1)
text_input1.grid(row=1,column=1)


text_input2=tk.Text(w,width=30,height=1)
text_input2.grid(row=2,column=1)
enter_button=tk.Button(w,text="Conferma",command=lambda:userinput(ipaddr1,ipaddr2))
enter_button.grid(row=2,column=2,padx=20)

w.mainloop()
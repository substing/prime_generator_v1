#current issues:
#1. does not print errors for bad input
#2. cannot scroll through large output
def sieve_up_to(n):
	p_tf = [True]*n 
	primes = []
	p = 2
	p_tf[0], p_tf[1] = False, False
	while p**2 <= n:
		if p_tf[p] == True:
			for i in range(p*2, n, p):
				p_tf[i] = False
		p += 1
	for i in range(0,len(p_tf)):
		if p_tf[i] == True:
			primes.append(i)

	return primes


#Import the required Libraries
from tkinter import *
from tkinter import ttk


def show_output():
	global entry
	ent = entry.get()
	ent = int(ent)
	data = sieve_up_to(ent)
	i = 1
	for d in data:
		output.insert(i, d)
		i += 1

win = Tk()

#Set the geometry of Tkinter frame
win.geometry("750x650")

label=Label(win, text="Generate a list of prime numbers up to...", font=("Courier 22 bold"))
label.pack()


entry= Entry(win, width= 5)
entry.focus_set()
entry.pack()


#Create a Button to validate Entry Widget
ttk.Button(win, text= "Enter",
   command= show_output).pack()

output = Listbox(win)
output.pack(padx=10,pady=10,fill=BOTH,expand=True)

win.mainloop()
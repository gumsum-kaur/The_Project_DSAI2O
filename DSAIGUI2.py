from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import*


print("W E L C O M E	T O	D S A I 2.O !")

win1=Tk()

#w.geometry('427x250')

widthWindow=540
heightWindow=320

screenWidth=win1.winfo_screenwidth()
screenHeight=win1.winfo_screenheight()

x_coordinate=(screenWidth/2)-(widthWindow/2)
y_coordinate=(screenHeight/2)-(heightWindow/2)

win1.geometry("%dx%d+%d+%d"%(widthWindow,heightWindow,x_coordinate,y_coordinate))

win1.overrideredirect(1)


s=ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar",foreground='red',background='#2FB4CC')
progress=Progressbar(win1,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=540,mode='determinate')



def main_window():
	win2=Tk()
	win2.title("DSAI2.O")
	sb=Scrollbar(win2).pack(side=RIGHT,fill=Y)
	
	win2.geometry('820x520')
	win2.resizable(0,0)
	l5=Label(win2, text="WELCOME TO DSAI2.O", fg='purple', bg=None)
	l5.place(x=225,y=40)
	l=('Calibri (Body)',24,'bold')
	l5.configure(font=l)
	
	
	l2=Label(win2,text='The Data Science Artificial Intelligencei is \na project based on Artificial Intelligence\nalong with Data Science. Come and join here;\n and Discover and learn about AI Companies.\nTechnology and Case Studies in your industry.\n Helping companies and ...',fg='black',bg=None)
	lst2=('Sans (Body)',10)
	l2.configure(font=lst2)
	l2.place(x=60,y=190)
	
	
	l3=Label(win2,text='Begin your journey along with DSAI Project.\nDSAI allows you to quickly voice verify\nthe identities of your users via phone,\ncomputer or any other device medium based on\nmillions of comparisons on a  daily basis.\nAlso it helps you to encourage you to become\na creative in your surroundings... ',fg='black',bg=None)
	lst3=('Sans (Body)',10)
	l3.configure(font=lst3)
	l3.place(x=440,y=190)
	
	
	def  dest():
		win2.destroy()
		
	
	import webbrowser
	def openWeb():
		webbrowser.open('http://dsaiprograming.website2.me')
		webbrowser.open('https://gumsumasadboy.wixsite.com/redbox')
		
		
	
	b=Button(win2,width=50,height=1,text='Visit here for more details',command=openWeb,border=0,fg='blue',bg=None)
	b.place(x=230,y=340)
	
	b1=Button(win2,width=10,height=1,text='EXIT',command=dest,border=0,fg='purple',bg='skyblue')
	b1.place(x=310,y=490)
	
	b2=Button(win2,width=10,height=1,text='ACCEPT',command=dest,border=0,fg='purple',bg='skyblue')
	b2.place(x=410,y=490)
	
	win2.mainloop()

def bar():
	l4=Label(win1, text="L o a d i n g ...",fg='white', bg='#249794')
	lst4=('Calibri (Body)',10)
	l4.configure(font=lst4)
	l4.place(x=210,y=250)
	
	import time
	r=0
	for i in range(100):
		progress['value']=r
		win1.update_idletasks()
		time.sleep(0.03)
		r=r+1
	win1.destroy()
	main_window()
	
progress.place(x=0,y=301)

#frame
Frame(win1,width=540,height=300,bg='#249794').place(x=0,y=0)
b1=Button(win1,width=10,height=1,text='Get Started',command=bar,border=0,fg='#249794')
b1.place(x=210,y=200)


#Labels
l1=Label(win1,text='WELCOME TO DSAI2.O !',fg='white',bg='#249794')
lst1=('Calibri (Body)',22,'bold')
l1.configure(font=lst1)
l1.place(x=99,y=100)


	
#bar()
	
#main_window()

win1.mainloop()

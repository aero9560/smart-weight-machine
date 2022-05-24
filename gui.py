from tkinter import *
from HX711 import *
#import threading
from gpiozero import Button as gpiobutton
from escpos import printer
from time import *
from datetime import date
from datetime import datetime


#****************************global variables declaration **********************

global batch_code
global f0
global f1
global f2
global f3
global f4
global commodity_name
global total_weight
global w
global frame_no
global hx
global weight       
        
#************************* Global Variables assignment****************************

hx = AdvancedHX711(27, 17, 198227, 114496, Rate.HZ_80)
w = 0.0
total_weight = 0.0



def zero1():  # Reset current weight
    hx.zero()

#*************************** Horizontal Physical Button *************************
bth1 = gpiobutton(16)
bth2 = gpiobutton(21)
bth3 = gpiobutton(20)
bth4 = gpiobutton(13)
bth5 = gpiobutton(6)
#*************************** Vertical Physical Button ***************************
btv1 = gpiobutton(26)


def unsetbutton():           # Remove all button functions
    def none():
        print("")
    bth1.when_pressed= none
    bth2.when_pressed= none
    bth3.when_pressed= none
    bth4.when_pressed= none
    bth5.when_pressed= none
    btv1.when_pressed= none


#def raise_frame(frame):
    #frame.tkraise()



def total(a,b):
    global total_weight
    #print (type(total_weight)) 
    b = b + a
    b = float('{:.1f}'.format(b))
    total_weight = b
    #print(b)
    
    title = Label(f4, text='{:.1f}'.format(b), font=('', 40,'bold'),bg='white',fg='#000000')
    title.place(x=1500, y=210)


def addweight(com):
    global commodity_name
    global total_weight
    global w
    global f2
    global f3
    global f4
    global frame_no
    global weight
    
    commodity_name = com
    frame_no = 3
    
    f2.destroy()
    
    f3 = Frame(root, bg='#228A4F')
    f3.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
    
    
    
    bt_back = Button(f3,image= back,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=commo)
    bt_back.place(x=1635, y=100)
    
    bt_add = Button(f3,image= add, pady=20,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0,command=lambda:total(w,total_weight))
    bt_add.place(x=813, y=850)
    
    bt_print = Button(f3,image= Print, pady=20,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0)
    bt_print.place(x=1183, y=850)
    
    bt_save_exit = Button(f3,image= save,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0)
    bt_save_exit.place(x=1558, y=850)
    
    f4 = Frame(f3, bg='white', width = 1860 , height = 400 , highlightbackground='black', highlightthicknes=10)
    f4.place(x= 30 ,y= 330)
    
    if commodity_name == "Potato":
        potato_label=Label(f4, image = potato1 ,bd =0)
        potato_label.place(x=50,y=50)
    if commodity_name == "Onion":
        Onion_label=Label(f4, image = onion1,bd = 0)
        Onion_label.place(x=50,y=50)
    if commodity_name == "Eggplant":
        Eggplant_label=Label(f4, image = eggplant1,bd =0)
        Eggplant_label.place(x=50,y=50)
    if commodity_name == "Pumpkin":
        Pumpkin_label=Label(f4, image = pumpkin1,bd =0)
        Pumpkin_label.place(x=50,y=50)
    if commodity_name == "Ladyfinger":
        Ladyfinger_label=Label(f4, image = ladyfinger1 ,bd =0)
        Ladyfinger_label.place(x=50,y=50) 
    
    
    batch_no_label = Label(f4, text="BATCH NUMBER",font=('', 20), bg='white',fg='grey')
    batch_no_label.place(x=500, y= 50)
    
    
    
    commodity_label = Label(f4, text="COMMODITY", font=('', 20), bg='white',fg='grey')
    commodity_label.place(x=500, y=200)
    commodity_label1 = Label(f4, text=f"{commodity_name}", font=('', 40 ,'bold'), bg='white',fg='#000000')
    commodity_label1.place(x=500, y=250)
    
    weight_label = Label(f4, text="WEIGHT  (KG)", font=('', 20), bg='white',fg='grey')
    weight_label.place(x=1100, y=150)
    
    weight = Label(root,text=w,font = ('', 40,'bold'),bg='white',fg='#000000')
    weight.place(x=1135,y=550)
    
    #weight = Label(f4,text=w,font = ('', 40,'bold'), bg='white',fg='#000000')
    #weight.place(x=1100,y=225)
    
    total_weight_label = Label(f4, text="TOTAL WEIGHT  (KG)", font=('', 20), bg='white',fg='grey')
    total_weight_label.place(x=1500, y=150)
    
    
    
def commo():
    global f0
    global f1
    global f2
    global f3
    global frame_no
    global last
    if frame_no == 1 or frame_no == 0:
        last = frame_no
        
    frame_no = 2
    
    f0.destroy()
    f1.destroy()
    f3.destroy()
    
    def backfun():
        #pass
        global last
        if last == 1:
            batch()
        else:
            main()
    
    f2 = Frame(root, bg='#228A4F')
    f2.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
    
    batch_no_label = Label(f2, text="BATCH NUMBER : 11111",font=('', 40),bg='#228A4F',fg='#FFFFFF')
    batch_no_label.place(x=630, y= 50)
    
    commodity_label = Label(f2, text="SELECT COMMODITY", font=('', 80),bg='#228A4F',fg='#FFFFFF')
    commodity_label.place(x=520, y=300)
    
    backbtn = Button(f2,image= back,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=backfun)
    backbtn.place(x=1635, y=100)
    #btv1.when_pressed = batchcode
   
    potatobtn = Button(f2,image= potato,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: addweight("Potato"))
    potatobtn.place(x=25, y=500)
    #bth1.when_pressed = lambda: commo_dity("Potato")
        
    onionbtn = Button(f2, image= onion,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda:addweight("Onion"))
    onionbtn.place(x=410, y=500)
    #bth2.when_pressed = lambda: commo_dity("onion")
        
    eggplantbtn = Button(f2,image= eggplant,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0,command=lambda: addweight("Eggplant"))
    eggplantbtn.place(x=790, y=500)
    #bth3.when_pressed = lambda: commo_dity("eggplant")
        
    pumpkinbtn = Button(f2, image= pumpkin,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda:addweight("Pumpkin"))
    pumpkinbtn.place(x=1170, y=500)
    #bth4.when_pressed = lambda: commo_dity("pumpkin")
        
    ladyfingerbtn = Button(f2, image= ladyfinger,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: addweight("Ladyfinger"))
    ladyfingerbtn.place(x=1550, y=500)
    #bth5.when_pressed = lambda: commo_dity("ladyfinger")


def batch():
    global f0
    global f1
    global f2
    global f3
    global frame_no
    
    frame_no = 1
    
    f0.destroy()
    f2.destroy()
    f3.destroy()
    
    def click(number):
        pass
        '''current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))'''

    def delete():
        pass
        '''text = e.get()
        e.delete(0, END)
        text = text[:-1]
        e.insert(0, text)'''
    
    f1 = Frame(root, bg='#228A4F')
    f1.pack(side= 'top' ,fill='both', expand=True, padx=0, pady=0)
    
    #raise_frame(f1) 
     
    batch_no_label = Label(f1, text="ENTER BATCH NUMBER",font=('', 40),bg='#228A4F',fg='#FFFFFF')
    batch_no_label.place(x=675, y= 50)
    
    e = Entry(f1, width=18,font=('', 50), borderwidth=5)
    e.place(x=580, y=150)
    
    weight = Label(f1, text="PREVIOUS BATCH NO. :",font=('', 20),bg='#228A4F',fg='#FFFFFF')
    weight.place(x=810, y= 300)
    
    btn_del = Button(f1, image= backspace,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=delete)
    btn_del.place(x=725, y=775)
    btn_1 = Button(f1, image= one,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(1))
    btn_1.place(x=550, y=425)
    btn_2 = Button(f1, image= two,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(2))
    btn_2.place(x=725, y=425)
    btn_3 = Button(f1, image= three,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(3))
    btn_3.place(x=900, y=425)
    btn_4 = Button(f1, image= four,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(4))
    btn_4.place(x=1075, y=425)
    btn_5 = Button(f1, image= five,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(5))
    btn_5.place(x=1250, y=425)
    btn_6 = Button(f1, image= six,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0,command=lambda: click(6))
    btn_6.place(x=550, y=600)
    btn_7 = Button(f1, image= seven,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(7))
    btn_7.place(x=725, y=600)
    btn_8 = Button(f1, image= eight,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(8))
    btn_8.place(x=900, y=600)
    btn_9 = Button(f1, image= nine,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(9))
    btn_9.place(x=1075, y=600)
    btn_0 = Button(f1, image= zero,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=lambda: click(0))
    btn_0.place(x=1250, y=600)

    
    backbtn = Button(f1, image= back,bg ='#228A4F',activebackground='#228A4F',highlightthickness = 0, bd= 0, command=main)
    backbtn.place(x=1635, y=100)

    nextbtn = Button(f1,  image= Next,bg ='#228A4F',highlightthickness = 0, bd= 0,activebackground='#228A4F',command=commo)
    nextbtn.place(x=1558, y=850)
    

def main():
    global f0
    global f1
    global f2
    global f3
    global frame_no
    global w
    global weight
    
    
    frame_no = 0
    
    f1.destroy()
    f2.destroy()
    f3.destroy()
    
    f0= Frame(root,bg='#228A4F')
    f0.pack(fill='both', expand =True, padx=0, pady=0, side=TOP)
    
    #weight = Label(f0,text=w,font = ('', 100))
    #weight.place(x=300,y=200)
    weight = Label(root,text=w,font = ('', 150),bg='#228A4F',fg='white')
    weight.place(x=600,y=300)
    
    weight1 = Label(f0, text="WEIGHT SCALE : 100G-500KG",font=('', 30),bg='#228A4F',fg='white')
    weight1.place(x=630, y= 100)
    
    bt_reset = Button(f0,image= reset, pady=20,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0)
    bt_reset.place(x=48, y=850)
    
    bt_records = Button(f0,image= records, pady=20,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0)
    bt_records.place(x=813, y=850)
    
    bt_manual = Button(f0,image= manual, pady=20,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0, command = batch)
    bt_manual.place(x=1183, y=850)
    
    bt_newbatch = Button(f0,image= newbatch,bg ='#228A4F',activebackground='#228A4F', highlightthickness = 0, bd= 0 , command = commo)
    bt_newbatch.place(x=1558, y=850)
    

def core():   
        global w
        global weight
        global hx
        global frame_no
        hx.setUnit(Mass.Unit.KG)
        hx.zero()
        #weight = Label(root,text=w,font = ('', 150),bg='#228A4F',fg='white')
        #weight.place(x=600,y=300)
        while True:
            
            
            m = float(hx.weight(1))
            x = abs(m)
            w = float('{:.1f}'.format(x))
            #if frame_no == 0 or frame_no == 3:
            #weight = Label(root,text=w,font = ('', 150),bg='#228A4F',fg='white')
            #weight.place(x=600,y=300)
            weight.config(text=w)
            weight.update()
            #else :
                
                #print (w)

root = Tk()
root.geometry("1024x600" )
root.title(u"Weight scale")
root.attributes('-fullscreen',True)

#*************************************** Button images ****************************************************

reset = PhotoImage(file="reset.png")
records = PhotoImage(file="records.png")
manual = PhotoImage(file="manual.png")
newbatch = PhotoImage(file="newbatch.png")
Next = PhotoImage(file="next.png")
back = PhotoImage(file="back.png")
onion = PhotoImage(file="onion.png")
pumpkin = PhotoImage(file="pumpkin.png")
eggplant = PhotoImage(file="eggplant.png")
ladyfinger = PhotoImage(file="ladyfinger.png")
potato = PhotoImage(file="potato.png")
add = PhotoImage(file="add.png")
Print = PhotoImage(file="print.png")
save = PhotoImage(file="save.png")

zero = PhotoImage(file="0.png")
one = PhotoImage(file="1.png")
two = PhotoImage(file="2.png")
three = PhotoImage(file="3.png")
four = PhotoImage(file="4.png")
five = PhotoImage(file="5.png")
six = PhotoImage(file="6.png")
seven = PhotoImage(file="7.png")
eight = PhotoImage(file="8.png")
nine = PhotoImage(file="1.png")
backspace = PhotoImage(file="del.png")

onion1 = PhotoImage(file="onionimg.png")
pumpkin1 = PhotoImage(file="pumpkinimg.png")
eggplant1 = PhotoImage(file="eggplantimg.png")
ladyfinger1 = PhotoImage(file="ladyfingerimg.png")
potato1 = PhotoImage(file="potatoimg.png")

#*********************************************************************************************************

f1 = Frame(root)
f1.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
f2 = Frame(root)
f2.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)
f3 = Frame(root)
f3.pack(fill='both', expand=True, padx=0, pady=0, side=TOP)


main()
#t1 = threading.Thread(target= core)
#t1.start()
root.after(10,core)
root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:38:34 2019

@author: thomas
"""

import tkinter as tk
from tkinter import Menu
import tkinter.filedialog
from tkinter import ttk
from tkinter import messagebox

from scipy.stats import linregress
import pandas as pd

import webbrowser

window= tk.Tk()
window.geometry('600x600')
window.title('Henri')
#colore
window.configure(background='white')


var = tk.IntVar()

param = tk.LabelFrame(window, text="Params", padx=10, pady=10)
param.grid(column=0, row=10, sticky='W', padx= 10)

models = tk.LabelFrame(window, text="Models", padx=10, pady=10)
models.grid(padx=10, pady=10, sticky='W')

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("models")
    win.geometry('300x300')
    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    #b = ttk.Button(win, text="Okay", command=win.destroy)
    #b.grid(row=1, column=0)

#def popup_showinfo():
    #c=tk.Checkbutton(window, text="linear", command= second_print)
    #c.grid(row=3, column=0, sticky='W')
    #tk.messagebox.askquestion(c)
    #tk.simpledialog.Checkbutton(linear)
#def popupBonus():
 #   win = tk.Toplevel()
  #  win.wm_title("models")
   # win.resizable(False, False)

all_vars = [tk.IntVar() for _ in range(9)] #create 4 IntVars in one go
for i in all_vars : #set all vars to 0
    i.set(0)
    
lin_cb = tk.Checkbutton(models, text="linear regression", variable=all_vars[0])
lin_cb.grid(column=0, row=2, sticky='W')
nlin_cb = tk.Checkbutton(models, text="non-linear regression",variable=all_vars[1])
nlin_cb.grid(column=0, row=5, sticky='W')
lw_cb = tk.Checkbutton(models, text="lineweaver", variable=all_vars[2])
lw_cb.grid(column=1, row=2, sticky='W')
ha_cb = tk.Checkbutton(models, text="Hanes", variable=all_vars[3])
ha_cb.grid(column=1, row=3, sticky='W')
ea_cb = tk.Checkbutton(models, text="Eadie", variable=all_vars[4])
ea_cb.grid(column=1, row=4, sticky='W')
in_cb=tk.Checkbutton(models, text='inhibited', variable=all_vars[5])
in_cb.grid(column=0, row=7, sticky='W')
un_cb=tk.Checkbutton(models, text='unhibited', variable=all_vars[6])
un_cb.grid(column=0, row=8, sticky='W')   
lin_cb = tk.Checkbutton(models, text="Michaelis-Menten", variable=all_vars[7])
lin_cb.grid(column=1, row=5, sticky='W')
lin_cb = tk.Checkbutton(models, text="Hill", variable=all_vars[8])
lin_cb.grid(column=1, row=6, sticky='W')

run=tk.Button(models, text='run', width= 30, command= popup_bonus)
run.grid(column=10, row=10, sticky='SE')
          #if lin_cb.state()== 'selected' & if lw_cb.state()== 'selected' & if in_cb.state()=='selected'
          #command=Lineweaver
          #elif lin_cb.state()=='selected'& if lw_cb.state()== 'selected' & if un_cb.state()=='selected'
          #elif lin_cb.state()=='selected'& if lw_cb.state()== 'selected' & if un_cb.state()=='selected'
          #command=Lineweaver)
          #command=Lineweaver)
          #elif lin_cb.state()=='selected'& if lw_cb.state()== 'selected' & if un_cb.state()=='selected'
          #command=Lineweaver)
#run.grid(column=3, row=8, sticky='W')


tk.Label(param, text="substate").grid(row=1, sticky='W')
tk.Label(param, text="velocity").grid(row=2, sticky='W')
tk.Label(param, text="if inhibited").grid(row=3, sticky='W')
tk.Label(param, text="inibitor").grid(row=4, sticky='W')
tk.Label(param, text="inhibited velocity").grid(row=5, sticky='W')

tk.Label(param, text="Time unit").grid(row=2, column =6, sticky='W')

all_vars2 = [tk.IntVar() for _ in range(21)] #create 4 IntVars in one go
for i in all_vars : #set all vars to 0
    i.set(0)
    
su_M=tk.Checkbutton(param, text='M', variable=all_vars2[1])
su_M.grid(column=1, row=1, sticky='W')
su_mM=tk.Checkbutton(param, text='mM', variable=all_vars2[2])
su_mM.grid(column=2, row=1, sticky='W')
su_uM=tk.Checkbutton(param, text='µM', variable=all_vars2[3])
su_uM.grid(column=3, row=1, sticky='W')
su_Dabs=tk.Checkbutton(param, text='DAbs', variable=all_vars2[4])
su_Dabs.grid(column=4, row=1, sticky='W')
#check unità v min
v_M=tk.Checkbutton(param, text='M', variable=all_vars2[5])
v_M.grid(column=1, row=2, sticky='W')
v_mM=tk.Checkbutton(param, text='mM', variable=all_vars2[6])
v_mM.grid(column=2, row=2, sticky='W')
v_uM=tk.Checkbutton(param, text='µM', variable=all_vars2[7])
v_uM.grid(column=3, row=2, sticky='W')
v_Dabs=tk.Checkbutton(param, text='DAbs', variable=all_vars2[8])
v_Dabs.grid(column=4, row=2, sticky='W')
tu=tk.Checkbutton(param, text='s^-1', variable=all_vars2[9])
tu.grid(column=7, row=2, sticky='W')
tU=tk.Checkbutton(param, text='min^-1', variable=all_vars2[10])
tU.grid(column=8, row=2, sticky='W')
#check unità v inib
iu_M=tk.Checkbutton(param, text='M', variable=all_vars2[11])
iu_M.grid(column=1, row=4, sticky='W')
iu_mM=tk.Checkbutton(param, text='mM', variable=all_vars2[12])
iu_mM.grid(column=2, row=4, sticky='W')
iu_uM=tk.Checkbutton(param, text='µM', variable=all_vars2[13])
iu_uM.grid(column=3, row=4, sticky='W')
iu_Dabs=tk.Checkbutton(param, text='DAbs', variable=all_vars2[14])
iu_Dabs.grid(column=4, row=4, sticky='W')
#v inib
vi_M=tk.Checkbutton(param, text='M', variable=all_vars2[15])
vi_M.grid(column=1, row=5, sticky='W')
vi_mM=tk.Checkbutton(param, text='mM', variable=all_vars2[16])
vi_mM.grid(column=2, row=5, sticky='W')
vi_uM=tk.Checkbutton(param, text='µM', variable=all_vars2[17])
vi_uM.grid(column=3, row=5, sticky='W')
vi_Dabs=tk.Checkbutton(param, text='DAbs', variable=all_vars2[18])
vi_Dabs.grid(column=4, row=5, sticky='W')
tui=tk.Checkbutton(param, text='s^-1', variable=all_vars2[19])
tui.grid(column=7, row=5, sticky='W')
tUi=tk.Checkbutton(param, text='min^-1', variable=all_vars2[20])
tUi.grid(column=8, row=5, sticky='W')


def second_print():
    text='altre cose'
    text_output= tk.Label(window, text=text, fg='green', font=('Helvetica', 16))
    text_output.grid(row=1,column=1,padx=50, sticky='W')
    #padx sta per la spaziatura fra i print
    #sticky mi mantiene il testo in una posizione, usa punti cardinali N S E W
def Lineweaver(x,y):                       # definisco una funzione per la linearizzazione 
    s= 1/x                                 # per Lineweaver
    v=1/y
    slope,intercept,r_value,p_value,std_err=linregress(s,v)
    slope, intercept
    m=slope
    q=intercept
    l=list((m,q))
    return(l)

def fileopen():
    global df
    file= tkinter.filedialog.askopenfilename()
    df= pd.read_csv( file)
#menubar = tk.Menu(window)
#menubar.add_command(label='select file', command=fileopen)
#window.configure(menu=menubar)

menubar= tk.Menu(window)
filemenu= tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='select file', command= fileopen)
filemenu.add_command(label='save', command= second_print)
menubar.add_cascade(label='file', menu=filemenu)
window.configure(menu=menubar)
#modello matematico
modelmenu= tk.Menu(menubar, tearoff=0)

#menubar.add_cascade(label="model", command= popupBonus)
#guida, pdf articolo, spiegazione della statistica

def github():
    webbrowser.open('https://github.com/ThomasMasoero/primi')
    
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="about", command= github)
helpmenu.add_command(label="guide", command=second_print)
menubar.add_cascade(label="help", menu=helpmenu)


#impostazione parametri statistici
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="outlier study", command=second_print)
editmenu.add_command(label="standard deviation", command=second_print)
menubar.add_cascade(label="statistics", menu=editmenu)
def first_print():
    #Lineweaver(df['s'], df['v'])
    s_rec= 1/df['s']                                # per Lineweaver
    v_rec=1/df['v']
    slope,intercept,r_value,p_value,std_err=linregress(s_rec,v_rec)
    slope, intercept
    vmax=1/intercept
    km=slope*vmax
    linew=('the Vmax is '+str(vmax)+ 'the km is' +str(km) )
    linew_output= tk.Label(window, text=linew, fg='red', font=('Helvetica', 16))
    linew_output.grid(row=2,column=1,padx=50, sticky='W')
    
        







#questo impedisce di renderla ridimensionabile, non mi piace
#window.resizable(False, False)


#questa riga serve a far correre sempre la riga successiva
#if__name__=='__main__':
window.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:50:27 2019

@author: thomas
"""

import tkinter as tk
window= tk.Tk()
window.geometry('600x600')
window.title('abu gay')
#colore
window.configure(background='red')
def first_print():
    text='AAAAAAAAAhhh'
    text_output= tk.Label(window, text=text, fg='blue', font=('Helvetica', 16))
    text_output.grid(row=0,column=1, sticky='W')
def second_print():
    text='Smettila!!!'
    text_output= tk.Label(window, text=text, fg='green', font=('Helvetica', 16))
    text_output.grid(row=1,column=1,padx=50, sticky='W')
    #padx sta per la spaziatura fra i print
    #sticky mi mantiene il testo in una posizione, usa punti cardinali N S E W
#questo impedisce di renderla ridimensionabile, non mi piace
#window.resizable(False, False)
#specifichiamo ora la posizione nella finestra con grid
first_button = tk.Button(text='capezzolo', command=first_print)
first_button.grid(row=0,column=0, sticky='W')
second_button = tk.Button(text='orecchio', command=second_print)
second_button.grid(row=1,column=0, pady=20, sticky='W')

#questa riga serve a far correre sempre la riga successiva
#if__name__=='__main__':
window.mainloop()
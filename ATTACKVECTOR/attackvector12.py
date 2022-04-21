## ATTACK VECTOR 2 PAGE ##



import tkinter as tk                # python 3

from tkinter import font  as tkfont # python 3

#import Tkinter as tk     # python 2

#import tkFont as tkfont  # python 2



from tkinter import font as tkfont

from tkinter import *

from tkinter import font, messagebox

import random, requests, os, sys

import PySimpleGUI as sg

from nav_bar import *

from subprocess import call, Popen, PIPE

import os



class AttackVectorTwelve(tk.Frame):



    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")





        main_frame = tk.Frame(self)





        highlightFont = font.Font(family='Calibri', name='appHighlightFont11', size=18)





        def load_terminal():

            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell = True).stdout



        def change_to_Step1():

            text = (

            "\nStep 1: Reconnaissance\n\n"

                "o   Find what port is running on (usually looking for Apache service on port 80 but for Solar Apache service it is going to be on port 8983 as it is the default port) by using 'nmap target IP'.\n\n"

                "o   After using Nmap on target IP, we will Discover the target IP and the port we found, for example (http://Target.IP:Port)'.\n\n"

                "o   Once we are on the Target IP web service, we will be looking for /var/solr/logs.\n\n"

                "o   Check the directory or files you mounted, if you can't see it, exit the directory and access it again.\n\n"

            )

            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)

            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

            terminalButton = tk.Button(step1frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont, command=load_terminal, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)





        # creates blue bar as canvas below nav bar housing label containing title of page

        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)

        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)

        title_label = tk.Label(self, text="Solar, exploiting log4j Apache server", bg='#4D6C84', fg='white', anchor="c", font=framefont)

        title_label.place(rely=0.08, relheight=0.12, relwidth=1)



        allscreenframe = tk.Label(main_frame, bg='white')

        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)



        sidescreenframe = tk.Label(main_frame, text="\n            Steps", bg='#E7E7E7',  font=('Calibri', 20), anchor= 'nw')

        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)



        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05, relwidth=0.1)

        





        display_nav_bar(self, controller)

        main_frame.pack(fill='both', expand=1) 
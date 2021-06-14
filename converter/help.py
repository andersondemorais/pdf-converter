#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Using Python 3.x
""" 
Directory:
Documentation: 
"""
__author__   	= 'Fudencio'
__copyright__	= 'Copyright 2020, Mimimi'
__email__    	= 'neopunkat@gmail.com'
__date__     	= '2020-12-09 11:39:13'
__version__  	= '0.0.0'
__status__   	= ''

import tkinter as tkt
import textwrap
import webbrowser

LARGEFONT =("Verdana", 35)

class Help(tkt.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.config(background='#007849')
		
		txt = 'Documentação para execução do software'
		label1 = tkt.Label(self, text=textwrap.fill(txt, width=45), background='#007849')
		label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

		button = tkt.Button(self, text="Documentação", command=self.pdf_browser)
		button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
		
		
	def pdf_browser(self):
		webbrowser.open_new_tab(r'documentacao.pdf')

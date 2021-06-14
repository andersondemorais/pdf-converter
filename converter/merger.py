#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Using Python 3.x
""" 
Directory: Python
Documentation: Module to merge PDF files with Tkinter and PyPDF2
"""
__author__   	= 'Anderson Morais'
__copyright__	= 'Copyright 2020'
__email__    	= ''
__date__     	= '2020-12-08 14:38:56'
__version__  	= '1.0.0'
__status__   	= 'open'

import tkinter as tkt
from tkinter import filedialog
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileMerger
import getpass
import textwrap
import warnings

LARGEFONT =("Verdana", 35)
BGCOLOR = '#007849'

class Merger(tkt.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.config(background=BGCOLOR)		
		self.lbox = tkt.Listbox(self, width=40)
		self.label = tkt.Label(self)
		self.filenames = []
		self.filename = ''
		self.create_window()
		self.user = '/home/' + getpass.getuser()
		warnings.filterwarnings('ignore')

	def create_window(self):
		label = tkt.Label(self, text='Unir PDFs', font=LARGEFONT, background=BGCOLOR)
		label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

		self.label.config(text='Destino arquivo:', background=BGCOLOR)
		self.label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

		button_file = tkt.Button(self, text="Selecionar arquivos", command=self.load_files)
		button_file.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

		self.list_box()
		self.lbox.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

		button_move = tkt.Button(self, text="| Mover arquivo |", command=self.move_file)
		button_move.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

		button_clear = tkt.Button(self, text="Remover arquivo", command=self.remove_file)
		button_clear.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")

		button_clearall = tkt.Button(self, text="Remover todos", command=self.clear_all)
		button_clearall.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")

		button_merger = tkt.Button(self, text="Executar", command=self.compute)
		button_merger.grid(row=14, column=0, padx=10, pady=10, sticky="nsew")


	def load_files(self):
		filenames = filedialog.askopenfilenames(initialdir=self.user, title='Selecionar arquivos', filetypes=[('PDF files', '.pdf')])
		for file in filenames:
			self.filenames.append(file)
		self.lab_and_list()

	def list_box(self):
		self.lbox.delete(0,'end')
		for key, item in enumerate(self.filenames):
			item_box = str(key + 1) + ': ' + Path(item).name
			self.lbox.insert(key, item_box)

	def remove_file(self):
		if self.lbox.curselection():
			key = self.lbox.curselection()
			self.filenames.pop(key[0])
			self.list_box()

	def move_file(self):		
		if self.lbox.curselection():			
			key = self.lbox.curselection()[0]
			item = self.filenames[key]
			if key != 0:
				self.filenames[key] = self.filenames[key-1]				
				self.filenames[key-1] = item
				self.list_box()

	def compute(self):
		try:			
			if len(self.filenames) > 1 and len(self.filenames) < 50:
				self.label.config(text='Arquivo sendo criado...', foreground='white', background='black')			
				self.filename = filedialog.asksaveasfilename(initialdir=self.user, title='Salvar arquivo', filetypes=[('PDF files', '.pdf')])
				if not Path(self.filename).name.split('.')[1]:
					self.filename += '.pdf'							
				try:					
					merger = PdfFileMerger()
					for file in self.filenames:
						pdf = PdfFileReader(file)
						merger.append(pdf)
					merger.write(self.filename)
				except Exception as e:
					self.label.config(text='Erro: arquivo ñ foi criado.', background='#ff0000', foreground='black')
				else:
					self.label.config(text='Arquivo criado: ' + textwrap.fill(self.filename, width=30), background='#2398ab', foreground='black')
					self.clear()
			else:
				self.label.config(text='Arquivo ñ foi criado.', background='#fe634e', foreground='black')
		except:
			pass
	def clear(self):
		self.filename = ''
		self.filenames = []
		self.list_box()
			
	def clear_all(self):
		self.filename = ''
		self.filenames = []
		self.label.config(text='Destino arquivo:', background=BGCOLOR, foreground='black')
		self.list_box()
	
	def lab_and_list(self):
		self.label.config(text='Destino arquivo:', background=BGCOLOR, foreground='black')
		self.list_box()

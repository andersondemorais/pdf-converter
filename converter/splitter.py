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
__date__     	= '2020-12-08 14:35:52'
__version__  	= '1.0.0'
__status__   	= 'open'

import tkinter as tkt
from tkinter import filedialog
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import getpass
import textwrap
from os import path, mkdir
import warnings

LARGEFONT =("Verdana", 25)
BGCOLOR = '#007849'

class Splitter(tkt.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.config(background=BGCOLOR)
		self.label = tkt.Label(self)
		self.label1 = tkt.Label(self)		
		self.filename = ''
		self.directory = ''
		self.create_window()
		self.user = '/home/' + getpass.getuser()
		warnings.filterwarnings('ignore')

	def create_window(self):
		label = tkt.Label(self, text='Separar Páginas', font=LARGEFONT, background=BGCOLOR)
		label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

		self.label.config(text='Pasta destino: ', background=BGCOLOR)
		self.label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

		button_file = tkt.Button(self, text="Selecionar arquivo", command=self.load_files)
		button_file.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

		self.label1.config(text='Arquivo fonte:', background='white', width=40)
		self.label1.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")

		button_clear = tkt.Button(self, text="Remover arquivo", command=self.clear_all)
		button_clear.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")

		button_merger = tkt.Button(self, text="Executar", command=self.compute)
		button_merger.grid(row=14, column=0, padx=10, pady=10, sticky="nsew")


	def load_files(self):
		filename = filedialog.askopenfilenames(initialdir=self.user, title='Selecionar arquivo', filetypes=[('PDF files', '.pdf')])
		self.filename = filename[0]
		self.label1.config(text='Arquivo fonte: ' + textwrap.fill(self.filename, width=30))

	def remove_file(self):
		self.filename = ''
		self.label1.config(text='Arquivo fonte: ' + textwrap.fill(self.filename, width=30))

	def compute(self):
		try:
			self.directory = filedialog.askdirectory(initialdir=self.user, title='Nova pasta')
			folder = 'PAGS_PDF - ' + Path(self.filename).name
			folder = folder.split('.')[0]
			self.directory = path.join(self.directory, folder)
			try:
				self.label.config(text='Arquivos sendo criado...')
				mkdir(self.directory)
				with open(self.filename, 'rb') as file:
					reader = PdfFileReader(file)		
					for p in range(reader.numPages):
						writer = PdfFileWriter()
						writer.addPage(reader.getPage(p))
						page = 'page{}.pdf'.format(p+1)
						page = path.join(self.directory, page)				
						with open(page, 'wb') as pdf:
							writer.write(pdf)
			except Exception as e:
				self.label.config(text='Erro: arquivo ñ foi criado.', background='#ff0000')
			else:
				self.label.config(text='Pasta criada: ' + textwrap.fill(self.directory, width=30), background='#2398ab')
			finally:
				self.filename = ''
				self.directory = ''
		except:
			pass

	def clear_all(self):
		self.filename = ''
		self.directory = ''
		self.label.config(text='Pasta destino: ', background=BGCOLOR)
		self.label1.config(text='Arquivo fonte: ')

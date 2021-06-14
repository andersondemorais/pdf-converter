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
__date__     	= '2020-12-07 17:13:20'
__version__  	= '1.0.0'
__status__   	= 'open'

import tkinter as tkt
from merger import Merger
from splitter import Splitter
from converter_img import ConverterImg
from converter_pdf import ConverterPdf
from help import Help
import warnings

LARGEFONT = ("Verdana", 35)
BGCOLOR = '#117243'

class App(tkt.Tk):
	def __init__(self):
		super().__init__()
		self.geometry(self.geometryapp())		
		self.title('PDF Conversor')
		self.iconphoto(False, tkt.PhotoImage(file='py_icon.png'))
		warnings.filterwarnings('ignore')
		
		container = tkt.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (HomePage, Merger, Splitter, ConverterImg, ConverterPdf, Help):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("HomePage")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

	def geometryapp(self):
		width = 340
		height = 640

		width_scr = self.winfo_screenwidth()
		height_scr = self.winfo_screenheight()

		posx = (width_scr - width)/2
		posy = (height_scr - height)/2

		self.minsize(width, height)
		self.maxsize(width, height)

		return('%dx%d+%d+%d' % (width, height, posx, posy))

	def quit(self):
		self.destroy()

class MenuBar(tkt.Menu):
	def __init__(self, parent):
		super().__init__()

		filemenu = tkt.Menu(self, tearoff=False)
		convertmenu = tkt.Menu(self, tearoff=False)

		self.add_command(label='Início', command=parent.home)
		self.add_command(label='Unir', command=parent.merger)
		self.add_command(label='Separar', command=parent.splitter)
		self.add_command(label='Conv.IMG', command=parent.converter_img)
		self.add_command(label='Conv.PDF', command=parent.converter_pdf)
		#self.add_command(label='Help', command=parent.help)

class HomePage(tkt.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.parent = parent
		self.config(background=BGCOLOR)
		self.menubar = MenuBar(self)
		self.controller.config(menu=self.menubar)

		self.txt_merger = 'Unir arquivos PDF\nCombinar arquivos'
		self.txt_splitter = 'Extrair as páginas\ne criar vários arquivos'
		self.txt_converter_img = 'Converter arquivos IMG para PDF'
		self.txt_converter_pdf = 'Converter arquivos PDF para IMG'

		label = tkt.Label(self, text='Início', font=LARGEFONT, background=BGCOLOR)
		label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

		label_merger = tkt.Label(self, text=self.txt_merger, font='bold', background=BGCOLOR, borderwidth=1, relief='groove', height=3)
		label_merger = tkt.Button(self, label_merger, command=lambda: self.controller.show_frame("Merger"))
		label_merger.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

		label_splitter = tkt.Label(self, text=self.txt_splitter, font='bold', background=BGCOLOR, borderwidth=1, relief='groove', height=3)
		label_splitter = tkt.Button(self, label_splitter, command=lambda: self.controller.show_frame("Splitter"))
		label_splitter.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')

		label_converter_img = tkt.Label(self, text=self.txt_converter_img, font='bold', background=BGCOLOR, borderwidth=1, relief='groove', height=3)
		label_converter_img = tkt.Button(self, label_converter_img, command=lambda: self.controller.show_frame("ConverterImg"))
		label_converter_img.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')
		
		label_converter_pdf = tkt.Label(self, text=self.txt_converter_pdf, font='bold', background=BGCOLOR, borderwidth=1, relief='groove', height=3)
		label_converter_pdf = tkt.Button(self, label_converter_pdf, command=lambda: self.controller.show_frame("ConverterPdf"))
		label_converter_pdf.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')
		
		label_foot = tkt.Label(self, background=BGCOLOR, width=40)
		label_foot.grid(row=20, column=0, padx=10, pady=10, sticky='nsew')

	def quit(self):
		self.parent.quit()

	def home(self):
		self.controller.show_frame("HomePage")

	def merger(self):
		self.controller.show_frame("Merger")

	def splitter(self):
		self.controller.show_frame("Splitter")

	def converter_img(self):
		self.controller.show_frame("ConverterImg")

	def converter_pdf(self):
		self.controller.show_frame("ConverterPdf")

	def help(self):
		self.controller.show_frame("Help")
		
def main():
	print(__doc__)
	print(35*'=')

	app = App()
	app.mainloop()

if __name__ == '__main__': main()

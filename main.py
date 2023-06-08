import PyPDF3
import sys
import os

# Put your Pdfs in this current directory

merger = PyPDF3.PdfFileMerger()

for file in os.listdir(os.curdir):
    
    if file.endswith(".pdf"):
        merger.append(file)
        merger.write("combined.pdf")
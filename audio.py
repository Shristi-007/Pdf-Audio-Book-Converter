import os
import pyttsx3
import PyPDF2


PATH = './cp.pdf'

book = open(PATH, 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages
play = pyttsx3.init()
print('Playing Audio Book')
for num in range(0, num_pages):
    page = pdf_reader.getPage(num)

    data = page.extractText()

    play.say(data)

    play.runAndWait()

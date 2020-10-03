import pyttsx3
import PyPDF2
book = open('python_tutorial.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()
print (pages)
for i in range(1,pages):
    page = pdfreader.getPage(i)
    text = page.extractText()
    speaker.say(text)
speaker.runAndWait()

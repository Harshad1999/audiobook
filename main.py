import pyttsx3
import PyPDF2
book = open('the-rudest-book-ever-shwetabh-gangwar.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
speaker.say('Hey Harshad I am All yours')
speaker.runAndWait()
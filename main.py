import pyttsx3
import PyPDF2
book = open('the-rudest-book-ever-shwetabh-gangwar.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
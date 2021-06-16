import pyttsx3 as p
import PyPDF2
book = open('DWM.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = p.init()

for num in range(42,pages):
    page = pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    print(text)
    speaker.runAndWait()

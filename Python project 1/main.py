import pyttsx3
from PyPDF2 import PdfReader
print("First. Make you shure that pdf that would be converted on mp3 are on this current folder")
nameofpdf=input("Hey! can you show me what's the name of your book? pls end with '.pdf' => ")
reader=''
if nameofpdf.endswith('.pdf'):
    nameofpdf=nameofpdf
else:
    nameofpdf=nameofpdf+".pdf"
reader = PdfReader(open(nameofpdf, "rb"))#open pdf 
number_of_pages = len(reader.pages)
print(reader)
print(number_of_pages)
page = reader.pages[2]#para cada numero de páginas
text = page.extract_text(0)
clean_text=text.strip().replace('\n', ' ')
print(clean_text)
speaker=pyttsx3.init()
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()
speaker.stop()
#------------------------------------------------------
# for page_num in number_of_pages:
#     text=reader.getPage(page_num).extractText()
#     clean_text=text.strip().replace('\n', ' ')
#     print(clean_text)
#-----------------------------------------------------------
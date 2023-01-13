import pyttsx3
from PyPDF2 import PdfReader
print("First. Make you shure that pdf that would be converted on mp3 are on this current folder")
nameofpdf=input("Hey! can you show me what's the name of your book? pls end with '.pdf' => ")
reader=''
if nameofpdf.endswith('.pdf'):
    nameofpdf=nameofpdf
else:
    nameofpdf=nameofpdf+".pdf"
#try
reader = PdfReader(open(nameofpdf, "rb"))
number_of_pages = len(reader.pages)
#catch(error)
optionToConvert=input("would you like to: \n [a] Convert all the pdf \n [b] Convert a single page \n [c] Convert a range of pages \n => ")
optionToConvert.lower()
speaker=pyttsx3.init()
if optionToConvert.startswith("a"):
    print("This option are convert all the pdf")
    #for pag in len(reader.pages):
elif optionToConvert.startswith("b"):
    print("This option are are 'Convert a single page")
    pag=int(input("wich page would you want to convert?\n=> "))
    if pag>number_of_pages:
        pag=number_of_pages
    elif pag<=0:
        pag=1
    page=reader.pages[pag-1]
    text = page.extract_text(0)
    clean_text=text.strip().replace('\n', ' ')
    speaker.save_to_file(clean_text, 'pdfSinglePage.mp3')
    speaker.runAndWait()
    speaker.stop()
elif optionToConvert.startswith("c"):
    print("This option are on maintenance")
#page = reader.pages[2]#para cada numero de páginas
# text = page.extract_text(0)
# clean_text=text.strip().replace('\n', ' ')

# print(clean_text)
# speaker.save_to_file(clean_text, 'pdfSinglePage.mp3')
# speaker.runAndWait()
# speaker.stop()

#------------------------------------------------------
# for page_num in number_of_pages:
#     text=reader.getPage(page_num).extractText()
#     clean_text=text.strip().replace('\n', ' ')
#     print(clean_text)
#------------------------------------------------------
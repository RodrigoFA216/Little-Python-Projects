import pyttsx3, PyPDF2
print("First. Make you shure that pdf that would be converted on mp3 are on this folder")
# nameofpdf=input("Hey! can you show me what's the name of your book? pls end with '.pdf' => ")
# if nameofpdf.isalnum() and nameofpdf.endswith('.pdf'):
#     pdfreader=PyPDF2.PdfFileReader(open(nameofpdf, 'rb'))
# else:
#     print("you don't pay attention dude")
pdfreader=PyPDF2.PdfReader(open('Unidad3.pdf', 'rb'))
speaker=pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text=pdfreader.getPage(page_num).extractText()
    clean_text=text.strip().replace('\n', ' ')
    print(clean_text)
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()
speaker.stop()
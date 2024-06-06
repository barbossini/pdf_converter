from PyPDF2 import PdfReader
reader = PdfReader("others/ressources/course.pdf")
page = reader.pages[0]
text = page.extract_text()

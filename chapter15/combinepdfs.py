import PyPDF2, os

pdf_files = [filename for filename in os.listdir('chapter15') if filename.endswith('.pdf')]
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for f in pdf_files:
    reader = PyPDF2.PdfFileReader(open(f'chapter15/{f}', 'rb'))
    if reader.isEncrypted:
        reader.decrypt('rosebud')
    for pn in range(1,reader.getNumPages()):
        page = reader.getPage(pn)
        pdf_writer.addPage(page)

with open('chapter15/all.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)



import PyPDF2, os, sys


def enc_walk(user_dir, user_pw):
    if not os.path.exists(user_dir):
        print('invalid path')
        sys.exit()
    for dirpath, dirnames, filenames in os.walk(user_dir):
        for fn in filenames:
            if fn.endswith('.pdf'):
                with open(f'{dirpath}/{fn}', 'rb') as fr:
                    pdf_reader = PyPDF2.PdfFileReader(fr)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    with open(f'{dirpath}/{fn[:-4]}_encrypted.pdf', 'wb') as fw:
                        pdf_writer.encrypt(user_pw)
                        pdf_writer.write(fw)
                    with open(f'{dirpath}/{fn[:-4]}_encrypted.pdf', 'rb') as fe:
                        enc_reader = PyPDF2.PdfFileReader(fe)
                        if enc_reader.isEncrypted:
                            os.remove(f'{dirpath}/{fn}')

def dec_walk(user_dir, user_pw):
    if not os.path.exists(user_dir):
        print('invalid path')
        sys.exit()
    for dirpath, dirnames, filenames in os.walk(user_dir):
        for fn in filenames:
            if fn.endswith('.pdf'):
                with open(f'{dirpath}/{fn}', 'rb') as fr:
                    pdf_reader = PyPDF2.PdfFileReader(fr)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    if pdf_reader.isEncrypted:
                        if pdf_reader.decrypt(user_pw) == 0:
                            print(f'password failed on {dirpath}/{fn}')
                            continue
                    else:
                        continue
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    with open(f'{dirpath}/{fn[:-4]}_decrypted.pdf', 'wb') as fw:
                        pdf_writer.write(fw)

def main():
    input_dir = input('dir to walk and encrypt/decrypt pdfs: ')
    input_pw = input('password to encrypt/decrypt with: ')
    input_c = input('[e]ncrypt or [d]ecrypt: ')
    if input_c == 'e':
        enc_walk(input_dir, input_pw)
    elif input_c == 'd':
        dec_walk(input_dir, input_pw)
    else:
        print('invalid choice')



if __name__ == '__main__':
    main()
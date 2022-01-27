import PyPDF2, os, sys



def pdfbrute(pdf_path, lang_dic):
    if not os.path.exists(pdf_path) or not os.path.exists(lang_dic):
        print('invalid path')
        sys.exit()
    with open(pdf_path, 'rb') as f, open(lang_dic, 'r') as d:
        pdf_reader = PyPDF2.PdfFileReader(f)
        for word in d.readlines():
            pw_valid = pdf_reader.decrypt(word)
            if pw_valid:
                print(f'found password: {word}')

def main():
    user_path = input('path to pdf: ')
    user_dic = input('path to dictionary: ')
    pdfbrute(user_path, user_dic)



if __name__ == '__main__':
    main()
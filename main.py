import sys
import service.jpg_to_pdf_service as jpg_to_pdf
import service.pdf_to_img_service as pdf_to_img
import service.combine_pdfs_service as combine_pdfs

import os

def main():

    if sys.argv[1] == 'jpg_to_pdf':
        jpg_to_pdf.convert(os.getcwd())
    if sys.argv[1] == 'pdf_to_img':
        pdf_to_img.convert(os.getcwd())
    elif sys.argv[1] == 'combine_pdfs':
        combine_pdfs.combine(os.getcwd(), sys.argv[2])
    elif sys.argv[1] == 'help':
        print(f"Comandos disponiveis:\n")
        print(f"jpg_to_pdf -> Converte arquivos de imagens contidos na pasta para PDF")
        print(f"combine_pdfs <nome_do_arquivo_final> -> Combina arquivos PDFs contidos na pasta para um unico arquivo")
    else:
        print(f"Argumento inválido: {sys.argv[1]}")


if __name__ == "__main__":
    main()
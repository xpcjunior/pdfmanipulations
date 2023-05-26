from PyPDF2 import PdfReader
import os
import util.files_search as f_search

def convert(input_folder):
    
    arquivos = f_search.buscar_arquivos(input_folder, ['.pdf'])

    if len(arquivos) > 0:
        for arquivo in arquivos:

            pdf = PdfReader(arquivo.path)

            pages = pdf.pages

            for i, page in enumerate(pages):
                for image_file_object in page.images:
                    with open(os.path.join(input_folder, f"{arquivo.nome}_pag_{i+1}.jpg"), "wb") as fp:
                        fp.write(image_file_object.data)
        
        print("SUCESSO!")
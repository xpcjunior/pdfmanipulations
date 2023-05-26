from PIL import Image
import os
import util.files_search as f_search

def convert(input_folder):

    arquivos = f_search.buscar_arquivos(input_folder, ['.jpg','.png'])

    for arquivo in arquivos:        
        image = Image.open(arquivo.path)
        pdf_path = os.path.join(input_folder, f"{arquivo.nome}.pdf")
        image.save(pdf_path, "PDF", resolution=100.0)
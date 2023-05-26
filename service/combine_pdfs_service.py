from PyPDF2 import PdfWriter, PdfReader
import os
import util.files_search as f_search

def combine(input_folder, final_file_name):
    
    arquivos = f_search.buscar_arquivos(input_folder, ['.pdf'])

    if len(arquivos) > 0:
        output_file = os.path.join(input_folder, f"{final_file_name}.pdf")
        pdf_writer = PdfWriter()

        for arquivo in arquivos:
            with open(arquivo.path, "rb") as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

        with open(output_file, "wb") as output_file:
            pdf_writer.write(output_file)
        
        print("PDFs combinados com sucesso!")
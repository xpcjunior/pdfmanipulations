import os
from models.Arquivo import Arquivo

def buscar_arquivos(input_folder, ext):

    arquivos = []

    for path in os.listdir(input_folder):
        
        if os.path.isfile(os.path.join(input_folder, path)):
            nome_arquivo, extensao = os.path.splitext(path)
            if(extensao in ext):
                print(path)
                arquivos.append(
                    Arquivo(
                        nome_arquivo,
                        extensao,
                        os.path.join(input_folder, path)
                    )
                )

    return arquivos
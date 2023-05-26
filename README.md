# PDF Manipulations

Algoritimo que possui funções de auxilam na obtenção ou conversão de PDFs.

## Funções

Seguem abaixo a descriçào de todas as funcões do algoritimo. As mesmas devem ser executadas de dentro da pasta onde você deseja que a conversão/extração seja executada.

### Combinação de PDFs

Função que combina todos os PDFs contidos na pasta onde a função foi chamada em um unico PDF.

estrtura do comando:

    pdfm combine_pdfs <nome_arquivo_final>

exemplo:

    pdfm combine_pdfs revista_avon

### Conversão: Imagem para PDF
Função que converte todas as imagens contidas na pasta onde a função foi chamada em PDFs com o mesmo nome.

estrtura do comando:

    pdfm jpg_to_pdf

### Conversão: PDF para Imagem
Função que converte todos os PDFs contidos na pasta onde a função foi chamada em Imagens

estrtura do comando:

    pdfm pdf_to_img

## Instalação

### Windows

Crie uma variavel de ambiente e a adicione-a ao PATH do sistema. Esta variável deve apontar para seguinte pasta deste algoritimo:

> 📁 bin

Pronto! Execute as funções conforme é explicado acima.
import os
from fastapi.responses import FileResponse
LISTA_IMAGENS = os.listdir('./img/clicks/')


def get_lista_imagens():
    return {'imagens': LISTA_IMAGENS}


def get_imagem(nome_imagem):
    try:
        nome_imagem = f'{nome_imagem}.png'
        if (LISTA_IMAGENS.__contains__(nome_imagem)):
            return FileResponse(path=(f'./img/clicks/{nome_imagem}'))
        return {'Erro': f'Imagem {nome_imagem} nao encontrada'}
    except NameError:
        return {'fatal_error' : NameError}
    
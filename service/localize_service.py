import pyautogui as pg
import os

LISTA_IMAGENS = os.listdir('./img/clicks/')


def procure(imagem):
    try:
        confirme = pg.confirm(
            text=f'Posicione na tela do jogo para procurar a imagem {imagem}', title='Alerta', buttons=['OK', 'Cancel'])
        if confirme == 'OK':
            loc = pg.locateCenterOnScreen(
                f'./img/clicks/{LISTA_IMAGENS[LISTA_IMAGENS.index(imagem)]}')
            return {'pos_x': f'{int(loc.x)}', 'pos_y': f'{int(loc.y)}'} if loc != None else {'erro': f'Imagem ({imagem}) nao encontrada'}
    except NameError:
        return {'fatal_error': NameError}


def procure_loop(imagem):
    try:
        loc = pg.locateCenterOnScreen(
            f'./img/clicks/{LISTA_IMAGENS[LISTA_IMAGENS.index(imagem)]}')
        return {'pos_x': f'{int(loc.x)}', 'pos_y': f'{int(loc.y)}'} if loc != None else {'erro': f'Imagem ({imagem}) nao encontrada'}
    except NameError:
        return {'fatal_error': NameError}

from service.tarefas import verifica_estado_hero_service as ver_es_he_service
from service import localize_service as loc_service
from service import click_service as click_service
from service.tarefas import nao_ocioso_service as n_oc_service
import pyautogui as pg


def localize(imagem):
    pos_x, pos_y = loc_service.procure_sem_confirma(imagem).values()
    if pos_y != 0:
        return int(pos_x), int(pos_y)
    return 0, 0

def voltar_mapa(delay):
    x_close, y_close = localize('close.png')
    click_service.click(x_close, y_close, delay)
    pg.sleep(2)
    x_mapa, y_mapa = localize('treasure_hunt.png')
    click_service.click(x_mapa, y_mapa, delay)

def iniciar_trabalhar(delay, vezes_rolagem, tempo_entre_loops, tempo_verifica_hero):
    delay, vezes_rolagem, tempo_entre_loops, tempo_verifica_hero = int(delay), int(vezes_rolagem), int(tempo_entre_loops), int(tempo_verifica_hero)
    for i in range(0, tempo_verifica_hero):
        n_oc_service.nao_ocioso_sem_confirma(delay=delay, espera=tempo_entre_loops, vezes=1)
        pg.sleep(tempo_entre_loops)
        print(f'Tempo loop jogar {i}/{tempo_verifica_hero}')
    x_back, y_back = localize('back.png')
    print(localize('back.png'))
    if x_back > 0:
        click_service.click(x_back, y_back, delay)
        pg.sleep(2)
        x_hero, y_hero = localize('heros.png')
        if x_hero > 0:
            click_service.click(x_hero, y_hero, delay)
            pg.sleep(2)
            print(ver_es_he_service.estado_hero_sem_confirma(delay, vezes_rolagem))
    else:
        x_hero, y_hero = localize('heros.png')
        if x_hero > 0:
            click_service.click(x_hero, y_hero, delay)
            pg.sleep(2)
            print(ver_es_he_service.estado_hero_sem_confirma(delay, vezes_rolagem))
        print('falhou: error: imagens nao encontradas')
    voltar_mapa(delay)
    
def jogar(delay, vezes_rolagem, tempo_entre_loops, tempo_verifica):
    delay, vezes_rolagem, tempo_entre_loops, tempo_verifica = int(delay), int(
        vezes_rolagem), int(tempo_entre_loops), int(tempo_verifica)
    confirme = pg.confirm(
        text=f'Posicione na tela do jogo para iniciar o loop', title='Alerta', buttons=['OK', 'Cancel'])
    if confirme == 'OK':
        print('Aqui')
        while True:
            iniciar_trabalhar(delay, vezes_rolagem, tempo_entre_loops, tempo_verifica)

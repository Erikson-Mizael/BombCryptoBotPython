from service import click_service as click_service
from service import localize_service as loc_service
import pyautogui as pg

# Parametors
X_ESQUERDA, Y_TOPO, Y_BAIXO = 200, 250, 100
INICIO_RANGE, ADICIONE_Y_APOS_UPGRADE = 240, 40
X_LIMITE_BARRA = 470
PRIMEIRA_COR, SEGUNDA_COR = (177, 226, 118), (120, 159, 57)
COR_WORK_ATIVO, COR_WORK_DESA = (130, 193, 136), (91, 135, 95)


def ultimo_hero(pos_x_inicial, pos_x_final, pos_y_inicial, pos_y_final, delay, vezes_rolagem):
    click_service.click_arraste(
        pos_x_inicial, pos_x_final, pos_y_inicial, pos_y_final, delay, vezes_rolagem)


def localize(imagem):
    pos_x, pos_y = loc_service.procure_sem_confirma(imagem).values()
    if pos_y != 0:
        return int(pos_x), int(pos_y)
    return 0, 0


def loop_trabalhe_confere(delay):
    try:
        heros_ao_trabalho = 0
        pos_x_up, pos_y_up = localize('upgrade.PNG')
        if pos_x_up > 0:
            pg.sleep(2)
            for i in range(INICIO_RANGE, pos_y_up+ADICIONE_Y_APOS_UPGRADE):
                if pg.pixelMatchesColor(X_LIMITE_BARRA, i, PRIMEIRA_COR):
                    pos_x_work, pos_y_work = localize('work.png')
                    if pos_x_work > 0:
                        if pg.pixelMatchesColor(pos_x_work, i - 10, COR_WORK_DESA):
                            click_service.click(pos_x_work, i, 0)
                            heros_ao_trabalho += 1
                            pg.sleep(5)
                if pg.pixelMatchesColor(X_LIMITE_BARRA, i, SEGUNDA_COR):
                    pos_x_work, pos_y_work = localize('work.png')
                    if pos_x_work > 0:
                        if pg.pixelMatchesColor(pos_x_work, i - 10, COR_WORK_DESA):
                            click_service.click(pos_x_work, i, 0)
                            heros_ao_trabalho += 1
                            pg.sleep(5)
            return {'success': 'localizados', 'heros_ao_trabalho': heros_ao_trabalho}
        return {'falhou': {'x': pos_x_up, 'y': pos_y_up}}
    except NameError:
        return {'fatal_error': NameError}

def loop_trabalhe(delay, vezes_rolagem):
    try:
        heros_ao_trabalho = 0
        pos_x_up, pos_y_up = localize('upgrade.PNG')
        if pos_x_up > 0:
            pg.sleep(2)
            for i in range(vezes_rolagem):
                for i in range(INICIO_RANGE, pos_y_up+ADICIONE_Y_APOS_UPGRADE):
                    #pg.moveTo(X_LIMITE_BARRA, i)
                    if pg.pixelMatchesColor(X_LIMITE_BARRA, i, PRIMEIRA_COR):
                        pos_x_work, pos_y_work = localize('work.png')
                        if pos_x_work > 0:
                        # print('Cor', pg.pixel(pos_x_work, i - 10))
                            if pg.pixelMatchesColor(pos_x_work, i - 10, COR_WORK_DESA):
                                click_service.click(pos_x_work, i, 0)
                                heros_ao_trabalho += 1
                                pg.sleep(5)
                    if pg.pixelMatchesColor(X_LIMITE_BARRA, i, SEGUNDA_COR):
                        pos_x_work, pos_y_work = localize('work.png')
                        if pos_x_work > 0:
                            #print('Cor', pg.pixel(pos_x_work, i - 10))
                            if pg.pixelMatchesColor(pos_x_work, i - 10, COR_WORK_DESA):
                                click_service.click(pos_x_work, i, 0)
                                heros_ao_trabalho += 1
                                pg.sleep(5)
                loop_trabalhe_confere(delay)
                print('Loops verificar terminados')
                ultimo_hero(pos_x_up-X_ESQUERDA, pos_x_up-X_ESQUERDA, pos_y_up,pos_y_up-Y_TOPO, delay, 1)
                loop_trabalhe_confere(delay)
            return {'success': 'localizados', 'heros_ao_trabalho': heros_ao_trabalho}
        return {'falhou': {'x': pos_x_up, 'y': pos_y_up}}
    except NameError:
        return {'fatal_error': NameError}
    


def estado_hero(delay, vezes_rolagem):
    confirme = pg.confirm(
        text=f'Posicione na tela do jogo para iniciar o loop', title='Alerta', buttons=['OK', 'Cancel'])
    if confirme == 'OK':
        return loop_trabalhe(delay, vezes_rolagem)
    return {'falhou': 'evento cancelado'}

def estado_hero_sem_confirma(delay, vezes_rolagem):
    try:
        return loop_trabalhe(delay, vezes_rolagem)
    except NameError:
        return {'falhou': 'evento nao iniciado'}

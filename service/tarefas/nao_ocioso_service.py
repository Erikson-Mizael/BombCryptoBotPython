import pyautogui as pg
from service import localize_service as loc_service
from service import click_service as click_service
pg.FAILSAFE = False


def nao_ocioso(delay, espera, vezes):
    try:
        confirme = pg.confirm(
            text=f'Posicione na tela do jogo para iniciar o loop', title='Alerta', buttons=['OK', 'Cancel'])
        if vezes > 0 and confirme == 'OK':
            for i in range(0, vezes):
                x_cash, y_cash = loc_service.procure_loop('cash.png').values()
                click_service.click(int(x_cash), int(y_cash), delay)
                pg.sleep(espera)
                x_close, y_close = loc_service.procure_loop(
                    'close.png').values()
                click_service.click(int(x_close), int(y_close), delay)
                pg.sleep(espera)
            return {'success': 'loop finalizado', 'contagem': vezes}
        return {'info': 'loop não inicializado'}
    except NameError:
        return {'erro': NameError}

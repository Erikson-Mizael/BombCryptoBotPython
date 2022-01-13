import pyautogui as pg
pg.FAILSAFE = False
DELAY_MOUSE = 3

print('Bot iniciado ... *** ... Bot iniciado')
bau = './img/clicks/cash.png'
fechar = './img/clicks/close.png'

def up():
    localize_bau = pg.locateOnScreen(bau)
    if localize_bau != None:
        print('Baú Localizado!')
        localize_bau = pg.center(localize_bau)
        pg.moveTo(localize_bau.x, localize_bau.y, DELAY_MOUSE)
        pg.click()
        pg.sleep(5)
    else:
        print('Baú nao localizado')

    localize_fechar = pg.locateOnScreen(fechar)
    if localize_fechar != None:
        print('Fechar Localizado!')
        localize_fechar = pg.center(localize_fechar)
        pg.moveTo(localize_fechar.x, localize_fechar.y, DELAY_MOUSE)
        pg.click()
        pg.sleep(5)
    else:
        print('Fechar não localizado')
c = pg.confirm(text='Coloque no mapa do Jogo e aperte OK', title='Mensagem de Alerta', buttons=['OK', 'Cancel'])
pg.sleep(1)
if c == 'OK' :
    while True:
        for i in range(5):
            print(f'Inicializando {i}')
            pg.sleep(1)
            up()
            pg.sleep(3)

print('... *** ... Bot desligado ... *** ...')

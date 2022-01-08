import pyautogui as pg


def click(pos_x, pos_y, delay):
    try:
        pg.moveTo(pos_x, pos_y, delay, pg.easeInQuad)
        pg.sleep(1)
        pg.click()
        return {'clicado': True}
    except NameError:
        return {'clicado': False, 'error': NameError}


def click_arraste(pos_x_inicial, pos_x_final, pos_y_inicial, pos_y_final, delay, vezes_rolagem):
    try:
        for i in range(0, vezes_rolagem):
            pg.moveTo(pos_x_inicial, pos_y_inicial, delay, pg.easeInQuad)
            pg.sleep(1)
            pg.dragTo(pos_x_final, pos_y_final, delay, button='left')
        return {'clicado_arrastado': True}
    except NameError:
        return {'clicado_arrastado': False, 'error': NameError}
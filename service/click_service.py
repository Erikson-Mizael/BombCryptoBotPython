import pyautogui as pg


def click(pos_x, pos_y, delay):
    try:
        pg.moveTo(pos_x, pos_y, delay, pg.easeInQuad)
        pg.sleep(1)
        pg.click()
        return {'clicado': True}
    except NameError:
        return {'clicado': False, 'error': NameError}

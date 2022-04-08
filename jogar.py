from service import localize_service as loc_service
from service import click_service as click_service
from service.tarefas import nao_ocioso_service as n_oci_service
import threading
import pyautogui as pg

# 'reload', 'erro_click', 'nada' erro
# 'mapa', 'menu', 'inicio', erro_encontrado' localize-se

class Boot():
    def __init__(self, vezes_espera, senha_desbloqueio, delay):
        self.vezes_espera = vezes_espera
        self.senha_desbloqueio = senha_desbloqueio
        self.delay = delay
        print('Script iniciado')
        tempo = 0
        while True:
            result = self.main()
            if result == 1:
                tempo += result
            print(f'Result: {result} tempo: {tempo} entro no loop')
            if tempo == vezes_espera:
                self.heros()
                tempo = 0
        
        
    def main(self):
        
        if self.erro():
            self.atualizar_navegador()
            return True
        
        if self.localize_se() == 'mapa':
            pg.sleep(1)
            return 1
        
        if self.localize_se() == 'erro_encontrado':
            self.erro()
            self.atualizar_navegador()
            return True
        
        if self.localize_se() == 'inicio':
            self.logar()
            return True
        
        if self.localize_se() == 'menu':
            x_entrar, y_entrar = loc_service.procure_sem_confirma('treasure_hunt.png').values()
            while y_entrar == 0:
                x_entrar, y_entrar = loc_service.procure_sem_confirma('treasure_hunt.png').values()
            click_service.click(x_entrar, y_entrar, self.delay)
            return True
    
    def wallet(self):
        x_connect, y_connect = loc_service.procure_sem_confirma('connect_wallet.PNG').values()
        if y_connect > 0:
            return True
        return False
    
    def heros(self):
        x_back, y_back = loc_service.procure_sem_confirma('back.png').values()
        while y_back == 0:
            if self.erro():
                self.atencao('reload')
                break
            if self.wallet():
                self.atencao('reload')
                break
            x_back, y_back = loc_service.procure_sem_confirma('back.png').values()
        click_service.click(x_back, y_back, self.delay)
        pg.sleep(1)
        x_hero, y_hero = loc_service.procure_sem_confirma('heros.png').values()
        while y_back == 0:
            if self.erro():
                self.atencao('reload')
                break
            x_hero, y_hero = loc_service.procure_sem_confirma('heros.png').values()
        click_service.click(x_hero, y_hero, self.delay)
        pg.sleep(1)
        self.trabalhe_todos()
        
    def atencao(self, motivo):
        if motivo == 'reload' or motivo == 'erro_click':
            self.atualizar_navegador()
            self.logar()
        if motivo == 'nada':
            self.localize_se()
            
    def atualizar_navegador(self):
        pg.keyDown('ctrl')
        pg.press('f5')
        pg.keyUp('ctrl')


    def erro(self,):
        x_erro, y_erro = loc_service.procure_sem_confirma('ok.PNG').values()
        if y_erro > 0:
            x_erro, y_erro = int(x_erro), int(y_erro)
            click_service.click(x_erro, y_erro, 2)
            return True
        return False


    def logar(self):
        x_connect, y_connect = loc_service.procure_sem_confirma('connect_wallet.PNG').values()
        while y_connect == 0:
            if self.erro():
                self.atencao('reload')
                break
            x_connect, y_connect = loc_service.procure_sem_confirma('connect_wallet.PNG').values()
        print('Achou wallet')
        click_service.click(x_connect, y_connect, self.delay)
        print('Clicou')
        pg.sleep(2)
        x_assinar, y_assinar = loc_service.procure_sem_confirma('assinar.PNG').values()
        while y_assinar == 0:
            if self.erro():
                print(f'Achou erro {self.erro()}')
                self.atualizar_navegador()
                self.atencao('reload')
                break
            x_assinar, y_assinar = loc_service.procure_sem_confirma('assinar.PNG').values()
            pg.write(self.senha_desbloqueio, interval=0.25)
        print('Achou assinar')
        click_service.click(x_assinar, y_assinar, self.delay)
        print('Clicou')
        pg.sleep(2)
        return True


    def localize_se(self):
        x_hero, y_hero = loc_service.procure_sem_confirma('heros.png').values()
        x_back, y_back = loc_service.procure_sem_confirma('back.png').values()
        x_wallet, y_wallet = loc_service.procure_sem_confirma('connect_wallet.PNG').values()
        x_erro, y_erro = loc_service.procure_sem_confirma('ok.PNG').values()
        x_close, y_close = loc_service.procure_sem_confirma('close.png').values()
        if y_back > 0:
            return 'mapa'
        if y_hero > 0:
            return 'menu'
        if y_wallet > 0:
            return 'inicio'
        if y_close > 0:
            return 'close'
        if y_erro > 0:
            return 'erro_encontrado'
        else:
            if self.erro():
                return 'erro_encontrado'
            return 'nada'


    def erro_thread(self):
        while True:
            if self.erro():
                x_erro, y_erro = loc_service.procure_sem_confirma('ok.PNG').values()
                if y_erro > 0:
                    click_service.click(1, 1, 2)
                else:
                    print('erro clicar erro')
                    self.atencao('erro_click')
                    break
            print('Thread')
            pg.sleep(4)


    def trabalhe_todos(self):
        x_all, y_all = loc_service.procure_sem_confirma('all.PNG').values()
        while y_all == 0:
            if self.erro():
                print('erro trabalhe todos')
                self.atencao('erro_click');
                break
            if self.wallet():
                self.atencao('reload')
                break
            x_all, y_all = loc_service.procure_sem_confirma('all.PNG').values()
        click_service.click(x_all, y_all, 2)
        
        x_close, y_close = loc_service.procure_sem_confirma('close.png').values()
        while y_close == 0:
            if self.erro():
                print('erro volta')
                self.atencao('erro_click');
                break
            if self.wallet():
                self.atencao('reload')
                break
            x_close, y_close = loc_service.procure_sem_confirma('close.png').values()
        click_service.click(x_close, y_close, 2)
        return True


    
if __name__ == '__main__':
    senha_desbloqueio = ''
    delay = 2
    vezes_espera = 50
    try:
        senha_desbloqueio = input('Senha de desbloqueio caso precise: ')
        delay = input('Delay do mouse: ')
        senha_desbloqueio = input('Limite vezes_espera para all heros: ')
    except NameError:
        print(f'Erro: {NameError} Algo não esteve certo.')
        print(f'Iniciando com valores padroes.')
    
    bot = Boot(int(delay), senha_desbloqueio, int(vezes_espera))
    

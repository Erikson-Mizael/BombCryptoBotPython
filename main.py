from service import imagem_service as img_service
from service import localize_service as loc_service
from service import click_service as click_service
from service.tarefas import nao_ocioso_service as n_oci_service
from service.tarefas import verifica_estado_hero_service as ver_es_he_service
from service.loop import jogar_service
import pyautogui as pg
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./")
APP = FastAPI()


@APP.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Lista dos nomes das imagens
@APP.get("/funcao/lista-imagens")
def get_lista_imagens():
    return img_service.get_lista_imagens()

# Retorna localização da imagem
@APP.get("/funcao/localize")
def get_posicao(nome_imagem):
    return loc_service.procure(nome_imagem)


# Clicks
@APP.get("/funcao/click")
def click(pos_x, pos_y, delay):
    return click_service.click(pos_x, pos_y, delay)


@APP.get("/tarefa/nao-ocioso")
def nao_ocioso(delay, espera, vezes):
    return n_oci_service.nao_ocioso(int(delay), int(espera), int(vezes))

@APP.get("/tarefa/hero-trabalhe")
def hero_trabalhe(delay, vezes_rolagem):
    retornado_est_hero = ver_es_he_service.estado_hero(int(delay), int(vezes_rolagem))
    return retornado_est_hero 

@APP.get("/loop/jogar")
def jogar(delay, vezes_rolagem, tempo_entre_loops, tempo_verifica_hero):
    return jogar_service.jogar(delay, vezes_rolagem, tempo_entre_loops, tempo_verifica_hero)

@APP.get("/mouse")
def mouse():
   while True:
       x, y = pg.position()
       print(x, y)
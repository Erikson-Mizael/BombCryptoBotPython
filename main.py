from service import imagem_service as img_service
from service import localize_service as loc_service
from service import click_service as click_service
from service.tarefas import nao_ocioso_service as n_oci_service
from fastapi import FastAPI
APP = FastAPI()


# Lista dos nomes das imagens
@APP.get("/funcao/lista-imagens")
def get_lista_imagens():
    return img_service.get_lista_imagens()


# Retorna imagem
@APP.get("/funcao/imagem")
def get_imagem(nome_imagem):
    return img_service.get_imagem(nome_imagem)


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
"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""
from datetime import date

ano = int(input('\033[0:44:mQue ano quer analisar? coloque 0 para analisar o ano atual: \033[0:44:m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[0:31mBISSEXTO'.format(ano))
else:
    print('O ano {} \033[0:31mNÃO É BISSEXTO'.format(ano))

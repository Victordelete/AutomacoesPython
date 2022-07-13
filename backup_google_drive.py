# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:38:41 2022
Automação simples da movimentação de um arquivo para o backup no google drive. 

@author: Victor Hugo Marques
"""

import pyautogui
import time

pyautogui.alert('O codigo vai começar. Não use o computador enquanto script estiver executando')
pyautogui.PAUSE = 0.5

#abrir o google drive 
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#entrar na área de trabalho
pyautogui.hotkey('winleft', 'd')

#clique no arquivo que eu quro fazer backup e arrastar ele
pyautogui.moveTo(x=1318, y=42)
pyautogui.mouseDown(button='left')

pyautogui.moveTo(x=607, y=508) #movo para a posição do drive
pyautogui.hotkey('alt', 'tab')

time.sleep(3)

#largar o arquino google drive
pyautogui.mouseUp(button='left')

#esperar alguns segundos
time.sleep(1)

pyautogui.alert('Código finalizado. \nFavor conferir se o arquivo foi movido com sucesso. ')



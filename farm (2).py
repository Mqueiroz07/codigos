import pyautogui as py
import time

py.FAILSAFE = True


time.sleep(3) #tempo para o usuário abrir o jogo e posicionar a tela
py.click(860, 444)
time.sleep(3) #para abrir a aba de dme
py.click(860, 213)
time.sleep(3) #para clicar em favoritos
py.click(299, 216)
time.sleep(3) #para clicar na caixa de pesquisa
py.click(284, 265)
time.sleep(3) #para filtrar os dmes 
py.click(412, 409) #para selecionar o dme


while True:##########################------ Esse try: e while true: são para restringir o looping
    try:
        time.sleep(3)
        py.click(1095, 334) #para montar o elenco
        time.sleep(3)
        py.click(1172, 211) #para enviar o elenco
        time.sleep(3)
        py.click(412, 409)
    
    except py.FailSafeException:
        print("Programa interrompido pelo usuário.")
        break
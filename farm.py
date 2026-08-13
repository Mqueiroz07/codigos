import pyautogui as py
import time

py.FAILSAFE = True




time.sleep(3) #tempo para o usuário abrir o jogo e posicionar a tela
py.click(860, 444) #para abrir a aba de dme
py.click(860, 213) #para clicar em favoritos
py.click(299, 216) #para clicar na caixa de pesquisa
py.write('diária') #para filtrar os dmes 
py.click(412, 409) #para selecionar o dme


while True:
    try:
        time.sleep(1)
        py.press('p') #para montar o elenco
        time.sleep(1)
        py.press('s') #para enviar o elenco
        time.sleep(2)
    except py.FailSafeException:
        print("Programa interrompido pelo usuário.")
        break
#Criação de uma Viabilidade 
import pyautogui, time

pyautogui.moveTo(1439, 651, 2)
pyautogui.click() #Autenticação 

time.sleep(7) #Esperar 6 segundos

pyautogui.moveTo(1794, 99, 1)
pyautogui.click() #Novo Empreendimento 


pyautogui.moveTo(567, 113, 1)
pyautogui.click() #Nome do Empreendimento

pyautogui.press('del', presses=20) #Apaga Nome do Empreendimento 

pyautogui.write('Viabilidade Python', interval=0.25)

pyautogui.moveTo(743, 286, 1)
pyautogui.click() #Nome do Empreendimento

pyautogui.moveTo(740, 340, 1)
pyautogui.click() #Tipo de Projeto

pyautogui.moveTo(620, 420, 1)
pyautogui.click() #Loteamneto

pyautogui.moveTo(642, 420, 1)
pyautogui.click() #Data 

pyautogui.write('23/12/2022', interval=0.25)

pyautogui.moveTo(1360, 420, 1)
pyautogui.click() #Veiculo

pyautogui.moveTo(800, 466, 1)
pyautogui.click() #TG ATivo Real

pyautogui.moveTo(918, 580, 1)
pyautogui.click() #Estado

pyautogui.moveTo(600, 629, 1)
pyautogui.click() #Acre

pyautogui.moveTo(1360, 580, 1)
pyautogui.click() #Cidade

pyautogui.moveTo(1000, 625, 1)
pyautogui.click() #Acrelandia

pyautogui.moveTo(920, 660, 1)
pyautogui.click() #Lider

pyautogui.moveTo(691, 711, 1)
pyautogui.click() #Lider

pyautogui.moveTo(1356, 666, 1)
pyautogui.click() #Analista

pyautogui.moveTo(1139, 711, 1)
pyautogui.click() #Analista


pyautogui.moveTo(1320, 908, 1)
pyautogui.click() #Criar Projeto




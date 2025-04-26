#É necessário instalar as bibliotecas para conseguir importa-las, execute no terminal os comandos de cada biblioteca
import pyautogui #para instalar a pyautogui utilize o comando "pip install pyautogui"
import time #para instalar a biblioteca time utilize o comando "pip install time"
import pandas as pd # para instalar a biblioteca pandas utilize o comando "pip install pandas"

pyautogui.PAUSE = 0.5

#ACESSO A PLATAFORMA DE CADASTRO DE PRDUTOS
pyautogui.press("Win")
time.sleep(3)
pyautogui.write("google chrome")
time.sleep(3)
pyautogui.press("Enter")
time.sleep(4)

pyautogui.click(x=204, y=21)
pyautogui.hotkey("ctrl","n")
time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=658, y=374)
time.sleep(4)
pyautogui.write("Jhon.teste@automação.com")
pyautogui.press("tab")
pyautogui.write("SenhaTeste2025")
pyautogui.press("enter")
time.sleep(5)

#IMPORTANDO BASE DE DADOS
tabelaProdutos = pd.read_csv("produtos.csv")
print(tabelaProdutos)

#CADASTRO DE PRODUTOS EM LOOP ATÉ QUE NÃO HAJA MAIS PRODUTOS A SEREM CADASTRADOS
pyautogui.click(x=645, y=261)
for linha in tabelaProdutos.index:
    codigo = tabelaProdutos.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabelaProdutos.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabelaProdutos.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabelaProdutos.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    precoUnitario = tabelaProdutos.loc[linha,"preco_unitario"]
    pyautogui.write(str(precoUnitario))
    pyautogui.press("tab")
    
    custo = tabelaProdutos.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabelaProdutos.loc[linha,"obs"]
    if not pd.isna(tabelaProdutos.loc[linha,"obs"]):
        pyautogui.write(str(obs))
    
    pyautogui.press("enter")
    pyautogui.scroll(50000)
    pyautogui.click(x=645, y=261)
    


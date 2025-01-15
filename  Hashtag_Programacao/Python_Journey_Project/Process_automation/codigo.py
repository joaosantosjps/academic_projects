import time
import pyautogui
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.typewrite('google-chrome')
pyautogui.press('enter')

# Espera para garantir que o Chrome esteja aberto
time.sleep(3)

pyautogui.hotkey("ctrl", "t")  # Abre uma nova aba
#time.sleep(1)

# Copia a URL para a área de transferência e cola no Chrome
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyperclip.copy(url)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#time .sleep(5)
pyautogui.click(x=924, y=440)

pyautogui.write(f'jhoon123@gmail.com')
pyautogui.press("tab") 
pyautogui.write("jhoon123")
pyautogui.click(x=950, y=601) # clique no botao de login
#time.sleep(3)

df = pd.read_csv("produtos.csv")
for linha in df.index:
    pyautogui.click(x=868, y=319)
    pyautogui.write(str(df.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if df.loc[linha, "obs"] != "nan":
        pyautogui.write(str(df.loc[linha, "obs"]))
    
    pyautogui.press("tab") 
    pyautogui.press("enter")     

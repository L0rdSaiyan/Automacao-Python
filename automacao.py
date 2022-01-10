#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Importando as bibliotecas
import pyautogui

import pyperclip

import time

pyautogui.PAUSE = (2)

pyautogui.hotkey("ctrl", "t")

pyperclip.copy("https://www.youtube.com")

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(5)


pyautogui.click(x=411, y=131)

pyperclip.copy("Goku e Vegeta fazem a fusão pela primeira vez")

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

pyautogui.click(x=351, y=373)


# In[18]:


#Teste da posição do mouse.
time.sleep(5)

pyautogui.position()


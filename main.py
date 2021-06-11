from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException as te
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

import pandas as pd

import pyautogui
import time
import logging
import pyperclip

# <DATABASE>

# planilha
database = pd.read_excel( r"your path")

colunas = database.columns

# listas
pasta = database[ 'pasta' ].values.tolist()
tema = database[ 'tema' ].values.tolist() #int
total_de_aulas = database[ 'total_de_aulas' ].values.tolist() #int
aula = database[ 'aula' ].values.tolist()
cod = database[ 'cod' ].values.tolist()
link = database[ 'link' ].values.tolist()

# <PATH>

# Paths, URLS, frames
Path = r"yourpathhere"
driver = webdriver.Chrome(Path)

urL= "https://youraccountname.club.hotmart.com/admin/beta/dashboard" 


# <WEBDRIVER>


try:

    driver.get(urL)

    # login
    login = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="__blaze-root"]/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input'))
    )
    login.send_keys("youremail")

    # senha
    password = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="__blaze-root"]/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/span/input'))
    )
    password.send_keys("yourpassword")

    # botao entrar
    enter =  WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="__blaze-root"]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]/button'))
    )
    enter.click()

    # autogui sidebar
    time.sleep(15)
    pyautogui.hotkey('tab', 'tab', 'enter')

    # <FOR LOOP COMEÇA AQUI> 

    for i in range(len(pasta)):

        # abrir pagina de adicionar novo conteúdo a módulo
        time.sleep(5)
        driver.get("https://youraccountname.com/admin/beta/modules/cod/content/new")

        # adicionar  título
        titulo_hotmart = pasta[i] + " - " +  tema[i] + " - " + "Aula: " + str( aula[i] ) + " / " + str( total_de_aulas[i] )

        add_content = WebDriverWait(driver,30).until( 
            ec.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        
        add_content.send_keys(titulo_hotmart)
        
        # clicar na area de texto
        iframe = '<iframe src="https://player.vimeo.com/video/' + str(cod[i]) + '?title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>' + '<p><a href="https://vimeo.com/' + str(cod[i]) + '"></a></p>'
        add_iframe = WebDriverWait(driver,15).until( 
            ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/div[3]/div/div/div'))
        )

        add_iframe.click()

        # clicar no botao de html 
        click_html = WebDriverWait(driver,15).until( 
            ec.presence_of_element_located((By.CSS_SELECTOR, "#redactor-toolbar-0 > li:nth-child(1) > a"))
        )
        click_html.click()

        # clicar na area de texto html
        text_html = WebDriverWait(driver,15).until( 
            ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/div[3]/div/div/textarea'))
        )
        text_html.click()
        
        time.sleep(1)
        text_html.send_keys(iframe)

        time.sleep(1)
        click_html.click()

        # salvar e voltar
        saveback = WebDriverWait(driver,15).until( 
            ec.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div > div.content__base__page__actions.action__buttons__wrapper > button:nth-child(2)"))
        )
        saveback.click()
        
except NameError as e:
    #driver.quit()
    print(str(e))

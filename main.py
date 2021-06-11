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
database = pd.read_excel( r"C:\Users\Usuário\Downloads\Escola Nacional Online\DIREITO TRIBUTÁRIO - Prof. João Marcelo.xlsx")

colunas = database.columns

# listas
pasta = database[ 'pasta' ].values.tolist()
tema = database[ 'tema' ].values.tolist() #int
total_de_aulas = database[ 'total_de_aulas' ].values.tolist() #int
aula = database[ 'aula' ].values.tolist()
cod = database[ 'cod' ].values.tolist()
link = database[ 'link' ].values.tolist()

# for loop iframe
'''
for i in range( len( codigo_list ) -1 , 0 - 1, -1 ):
    iframe = '<iframe src="https://player.vimeo.com/video/' + str({i}) + '?title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>' + '<p><a href="https://vimeo.com/' + str({i}) + '">344912</a></p>'
    print( iframe.format( *codigo_list)) #o ultimo elemento da lista é movido para o começo com asterisco
'''

# <PATH>

# Paths, URLS, frames
Path = r"C:\Users\Usuário\Documents\chromedriver.exe"
driver = webdriver.Chrome(Path)

urL= "https://escolanacionaldeconcurs-bmrqmk.club.hotmart.com/admin/beta/dashboard" 

'''
# <SHEETLOADER>

def sheetloader():

    titulo_hotmart = topicos_list[0] + " - " + "Professor: " + professor_list[0] + " - " + "Aula: " + str( capitulos_list[0] ) + " / " + str( aulas_list[0] ) 
    iframe = '<iframe src="https://player.vimeo.com/video/' + str({0}) + '?title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>' + '<p><a href="https://vimeo.com/' + str({0}) + '">344912</a></p>'

'''
# <WEBDRIVER>


try:

    driver.get(urL)

    # login
    # uso dois parênteses no EC para ele aceitar mais de um argumento
    login = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="__blaze-root"]/div[2]/div/div/div/div/div/div[2]/div/form/div[1]/input'))
    )
    login.send_keys("encformou@gmail.com")

    # senha
    password = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="__blaze-root"]/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/span/input'))
    )
    password.send_keys("!encformou10")

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
        driver.get("https://escolanacionaldeconcurs-bmrqmk.club.hotmart.com/admin/beta/modules/Go4E8d5ROz/content/new")

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

    '''
    modules = WebDriverWait(driver,20).until(
        driver.find_element(By.LINK_TEXT, 'Conteúdo')
    )
    modules.click()
    '''
    
    '''
    #achar pelo nome do link
    modules =  WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, 'Conteúdo'))
    )
    modules.click()
    #"/admin/beta/modules/n2OMoaBre6/content/new"
    '''
    '''
    #achar pelo contains xpath
    modules = WebDriverWait(driver, 10).until( 
        ec.presence_of_element_located((By.XPATH, '//*[contains(@id,"g97BqRnRep")]'))
    )
    modules.click()
    '''
    '''
    time.sleep(10)
    links = [elem.get_attribute("href") for elem in driver.find_elements_by_tag_name("a")]
    print(links)
    print(len(links))
    '''

'''
# listas
topicos_list = database[ 'Matéria' ].values.tolist()
capitulos_list = database[ 'Capitulo' ].values.tolist() #int
aulas_list = database[ 'N_Aula' ].values.tolist() #int
codigo_list = database[ 'Codigo' ].values.tolist()
links_list = database[ 'Link' ].values.tolist()
professor_list = database[ 'Professor' ].values.tolist()
'''
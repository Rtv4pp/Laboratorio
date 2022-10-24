from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)

nav.get('https://blaze.com/pt/games/double')

pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

tfg = pegardados.split()

def qualnum(x):
    if x == '1':
        return 1

    if x == '2':
        return 2

    if x == '3':
        return 3

    if x == '4':
        return 4

    if x == '5':
        return 5

    if x == '6':
        return 6

    if x == '7':
        return 7

    if x == '8':
        return 8

    if x == '9':
        return 9

    if x == '10':
        return 10

    if x == '11':
        return 11

    if x == '12':
        return 12

    if x == '13':
        return 13

    if x == '14':
        return 14

def qualcor(x):
    if x == '1':
        return 'Vermelho'

    if x == '2':
        return 'Vermelho'

    if x == '3':
        return 'Vermelho'

    if x == '4':
        return 'Vermelho'

    if x == '5':
        return 'Vermelho'

    if x == '6':
        return 'Vermelho'

    if x == '7':
        return 'Vermelho'

    if x == '8':
        return 'Preto'

    if x == '9':
        return 'Preto'

    if x == '10':
        return 'Preto'

    if x == '11':
        return 'Preto'

    if x == '12':
        return 'Preto'

    if x == '13':
        return 'Preto'

    if x == '14':
        return 'Preto'

pd = tfg[0:16]

mapeando = map(qualnum, pd)
mapeando2 = map(qualcor, pd)

finalnum = list(mapeando)
finalcor = list(mapeando2)

print(finalnum)



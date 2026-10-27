from urllib import response

import requests
from bs4 import BeautifulSoup
from conexao_ora_aluno import conectar_oracle

def coletar_citacoes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    print(quotes)
    print(authors)

if __name__ == '__main__':
    conectar_oracle()
    coletar_citacoes()
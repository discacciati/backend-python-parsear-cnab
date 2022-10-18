# Projeto de Backend para parsear arquivos CNAB

Projeto de backend desenvolvido em Python, responsável por receber e parsear arquivos CNAB.

## Tecnologias

. Linguagem Python 3.0 </br>

## Inicialização do Projeto

Para rodar o projeto é necessário: </br>

1. Configurar seu ambiente virtual : </br>
   1.1 #criar seu ambiente virtual executando o comando (via bash/terminal)</br>
   $ python -m venv venv --upgrade-deps</br>
   1.2 #Ativar seu ambiente virtual executando o comando (via bash/terminal)</br>
   Linux</br>
   $ source venv/bin/activate</br>
   Windows</br>
   $ source venv/Scripts/activate</br>
   1.3 #Instalar as dependências executando o comando (via bash/terminal)</br>
   $ pip install -r requirements.txt</br>
2. Rodar as migrações da API executando o comando (via bash/terminal): </br>
   2.1 $ python manage.py migrate </br>
3. Por fim, rodar sua API executando o comando (via bash/terminal) </br>
   3.1 $ python manage.py runserver</br>
   </br>
   Para acessar o formulário entre no endereço: </br>

   http://127.0.0.1:8000/

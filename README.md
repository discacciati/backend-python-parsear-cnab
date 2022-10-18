# Projeto de Backend para parsear arquivos CNAB

Projeto de backend desenvolvido em Python, responsável por receber e parsear arquivos CNAB.

## Tecnologias

. Linguagem Python 3.0 </br>
. Docker</br>

## Inicialização do Projeto

Para rodar o projeto é necessário: </br>

1. Clonar esse repositório</br>
2. Utilizar Python 3.0 e o Pip </br>
3. Configurar seu ambiente virtual : </br>
   4.1 #criar seu ambiente virtual executando o comando (via bash/terminal)</br>
   $ python -m venv venv --upgrade-deps</br>
   2.2 #Ativar seu ambiente virtual executando o comando (via bash/terminal)</br>
   Linux</br>
   $ source venv/bin/activate</br>
   Windows</br>
   $ source venv/Scripts/activate</br>
   2.3 #Instalar as dependências executando o comando (via bash/terminal)</br>
   $ pip install -r requirements.txt</br>
4. Criar arquivo .env para definir suas variáveis de ambiente, utilizando como exemplo .env.example</br>
5. Rodar as migrações da API executando o comando (via bash/terminal): </br>
   4.1 $ python manage.py migrate </br>
6. Por fim, rodar sua API executando o comando (via bash/terminal) </br>
   5.1 $ python manage.py runserver</br>
   </br>
   Para acessar o formulário entre no endereço: </br>

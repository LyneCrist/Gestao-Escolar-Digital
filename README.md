## Sobre
Projeto desenvolvido com foco em acessibilidade e inclusão, voltado para o acompanhamento do histórico médico e do bem estar de alunos com necessidades especiais. A solução digital oferece uma interface intuitiva para pais e responsáveis inserirem registros importantes, além de permitir que professores e profissionais da educação acessem e atualizem essas informações de forma segura e centralizada.

O projeto é desenvolvido na linguagem [**Python 3.12.2**](https://www.python.org/downloads/release/python-3122/),  framework [**Django 5.0.4**](https://docs.djangoproject.com/en/5.0/releases/5.0.4/) e banco de dados [**SQLite**](https://www.sqlite.org/)

## Instalação
Necessário antes clonar o repo para um diretório local de sua escolha. O script abaixo pode ser executado usando um terminal **powershell** ou vinculado o terminal do VSCode usando o próprio **powershell**. *Todo o script deverá ser executado para a criação e execução do ambiente no primeiro acesso a aplicação* O suporte mencionado estende apenas para ambiente operacional Windows. Aquele que for atuar deverá ter o conhecimento mínimo de terminal e linguagem Python.

Criando ambiente virtual
```powershell
python -m venv .venv
```
Ativando ambiente virtual
```powershell
.\.venv\Scripts\activate
```
Instalando dependências usando arquivo de *requirements*
```powershell
pip install -r requirements.txt
```
Verificando a instalação do Django
```powershell
python -m django --version
```
Executando migrate para acesso a base de dados em **SQLite**
```powershell
python manage.py migrate
```
Executa o serviço Django para acesso ao site
```powershell
python manage.py runserver
```

## Execução
A execução abaixo se faz necessária para o funcionamento do site, todo o processo é baseado no serviço Django.

Ativando ambiente
```powershell
.\.venv\Scripts\activate 
```
Baixando atualizações
```powershell
git pull
```
Atualizando estrutura da base de dados
```powershell
python manage.py makemigrate
```
Seguido do comando
```powershell
python manage.py migrate
```

Executando o serviço Django
```powershell
python manage.py runserver
```

# sv-django-03-enquete
Tutorial do  docs.djangoproject.com/pt-br/5.1

1) Criar ambiente virtual e ativar
Linux:
		python3 -m venv .venv         >> Cria um Ambiente Virtual
		source .venv/bin/activate     >> Entra no Ambiente Virtual

2) Instalar o Django (dentro do ambiente virtual >> criado e ATIVADO no passo 1)
	pip install django

Para saber que esta dentro do ambiente virtual, verificar no inicio da linha de comando (.venv)

	
3) Criar um projeto (Projeto é um conjunto de app >> app seria cada funcionalidade)
	django-admin startproject mysite .
	Cria um projeto chamado mysite dentro do diretorio atual (indicado pelo ".")
4) Rodar projeto
	python manage.py runserver

5) Criar um APP -- Aplicação(deve estar com o Ambiente Virtual ativo)
    python manage.py startapp polls

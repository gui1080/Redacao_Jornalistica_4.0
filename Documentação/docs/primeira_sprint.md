# Backend da Primeira Sprint

## Comandos

* `mkdocs serve` - Rodar na pasta "documentação" para ler a documentação. 

* `python3 -m venv venv` - Criar ambiente virtual.

* `source venv/bin/activate` - Entrar no ambiente virtual.

* `chmod +x dependencias.sh` - Para dar permissão para rodar o script de dependências.

* `./dependencias.sh`- Rodar script que baixa dependências.

Dependência para rodar documentação: 

```python
pip install mkdocs
```

## Arquivo de Dependências

Arquivo com atalho para confirguação de ambiente virtual. Basicamente baixa o Django se necessário e vê se o Python está na versão correta!

```python

echo "Hello $USER"
echo "Se certifique que seu Python3 está em dia (pelo menos Python 3.9.7)"
python3 --version
pip3 install --upgrade pip3
python3 manage.py makemigrations
python3 manage.py migrate
pip3 install djangorestframework
pip3 install django-cors-headers
pip3 install Django
echo "Rodando Django -> 'python3 manage.py runserver'"
echo "Tchau $USER"
python3 manage.py runserver

```

## Layout do projeto

```
.
├── func_basic
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── migrations
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── 0001_initial.cpython-310.pyc
│   │   │   └── 0002_alter_user_login_user_id.cpython-310.pyc
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_user_login_user_id.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── TAC_RedJor4
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv
│   ├── ...
├── .DS_Store
├── db.sqlite3
├── dependencias.sh
└── manage.py
```

## Proposta de Desenvolvimento

![Sprints](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documentac%CC%A7a%CC%83o/plano.jpeg?raw=true)

## Mapeamento teórico do conteúdo

![Content Mapping](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documentac%CC%A7a%CC%83o/tac_content_mapping.png?raw=true)

## Modelos

![Banco de Dados Proposto](https://github.com/gui1080/Redacao_Jornalistica_4.0/blob/master/Documentac%CC%A7a%CC%83o/bd.jpeg?raw=true)

Para a primeira iteração do trabalho, focou-se em implementar a funcionalidade de adição de texto, imagem e gráficos por parte do jornalista.

### User_Login

```python

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=150, unique=False, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    
```

#### GET

Dado par usuário e senha, retorna seu objeto de usuário. Passa seu id nas requisições para adicionar itens de mídia novos.

#### POST

Adiciona um usário novo.


### Basic_Metadata

Metadados comuns entre as mídias a serem adicionadas.

### NewsItem_Text

Cadastro de texto por parte do jornalista.

Herda metadados de "Basic_Metadata". Recebe id do usuário para verificação.

Adiciona os campos:

```python

    title = models.CharField(max_length=150, unique=False)  
    sutien = models.CharField(max_length=150, unique=False) 
    authors = models.CharField(max_length=150, unique=False) 
    editors = models.CharField(max_length=150, unique=False)
    
    # texto em si
    news_text = models.CharField(max_length=15000, unique=False) 
    
    keywords = models.CharField(max_length=1500, unique=False) 
    related_news = models.CharField(max_length=1500, unique=False) 
    
    # pra qual editoria isso vai
    related_publisher = models.CharField(max_length=350, unique=False) 
    
    # em qual qual midia isso circulou
    posted_on = models.CharField(max_length=150, unique=False)

```

### NewsItem_Photo

Cadastro de imagem por parte do jornalista.

Herda metadados de "Basic_Metadata". Recebe id do usuário para verificação.

Adiciona os campos:

```python

    title = models.CharField(max_length=150, unique=False)
    place = models.CharField(max_length=350, unique=False) 
    photographer = models.CharField(max_length=350, unique=False)
    keywords = models.CharField(max_length=350, unique=False)
    used_equipament = models.CharField(max_length=350, unique=False)
    description = models.CharField(max_length=350, unique=False)

    # arquivo!
    image = models.FileField(upload_to=upload_path, blank=True, null=True)

```

### NewsItem_Graphics

Cadastro de gráfico por parte do jornalista.

Herda metadados de "Basic_Metadata". Recebe id do usuário para verificação.

Adiciona os campos:

```python

    description = models.CharField(max_length=350, unique=False)
    data = models.CharField(max_length=350, unique=False)
    type_graphic = models.CharField(max_length=350, unique=False)
    designer = models.CharField(max_length=350, unique=False)
    
    # arquivo!
    graphic_image = models.FileField(upload_to=upload_path, blank=True, null=True)
    
```
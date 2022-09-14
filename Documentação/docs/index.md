# Backend da Primeira Sprint

Backend em Django Python para TAC, 2022/01 redação Jornalística 4.0

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

## Modelos



### User_Login

#### GET

Dado par usuário e senha, retorna seu objeto de usuário. Passa seu id nas requisições para adicionar itens de mídia novos.

#### POST

Adiciona um usário novo.


### Basic_Metadata

Metadados comuns entre as mídias a serem adicionadas.

### NewsItem_Text

Herda metadados de "Basic_Metadata".

### NewsItem_Photo

Herda metadados de "Basic_Metadata".

### NewsItem_Graphics

Herda metadados de "Basic_Metadata".
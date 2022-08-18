# Script shell para instalação de dependências

echo "Hello $USER"
echo "Se certifique que seu Python3 está em dia (Python 3.9.7)"
python3 --version
pip3 install --upgrade pip3
echo "Instalando ambiente virtual"
pip3 install virtualenv
python3 -m venv venv
echo "Para rodar se deve rodar -> 'source venv/bin/activate'"
source venv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
pip3 install djangorestframework
pip3 install Django
echo "Rodando Django -> 'python3 manage.py runserver'"
echo "Tchau $USER"
python3 manage.py runserver


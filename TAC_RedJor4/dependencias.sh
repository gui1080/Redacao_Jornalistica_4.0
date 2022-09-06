# Script shell para instalação de dependências

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


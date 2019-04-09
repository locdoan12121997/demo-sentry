git clone

if not install pip:
sudo apt-get install python3-pip

if not install virtualenv:
sudo pip3 install virtualenv 

virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

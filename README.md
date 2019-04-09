#Demo Sentry Flask
###Setup Guide
Clone the project:

```
git clone git@github.com:locdoan12121997/demo-sentry.git
cd demo-sentry
```


Install pip:

`sudo apt-get install python3-pip`

Install virtualenv:

`sudo pip3 install virtualenv`

Activate project environment:

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run app:

`FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run`

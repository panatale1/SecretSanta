#!/bin/bash
VENV_NAME="secretsanta"
VENV_DIR="$HOME/.virtualenvs"

mkdir -p $VENV_DIR

if [[ $(grep WORKON_HOME ~/.bashrc) == "" ]]; then
    echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
fi

wrapper_path=$(which virtualenvwrapper.sh)
if [[ wrapper_path != "" ]]; then
    echo $wrapper_path
    if [[ $(grep "source $wrapper_path" ~/.bashrc) == "" ]]; then
        echo "source $wrapper_path" >> ~/.bashrc
        source "$wrapper_path"
    fi 
fi
source /usr/local/bin/virtualenvwrapper.sh
if [[ ! -e $VENV_DIR/$VENV_NAME ]]; then
	mkvirtualenv secretsanta
fi
if [[ -z $(echo $VIRTUAL_ENV) ]]; then
	workon secretsanta
fi
pip install --upgrade -r requirements 
cd secretsanta
./manage.py migrate

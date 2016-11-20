#!/bin/bash
VENV_NAME="django-ops"
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

source $VENV_DIR/$VENV_NAME/bin/activate
#echo $VIRTUAL_ENV
sudo pip install --upgrade -r requirements
django-admin startproject secretsanta 

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
mkvirtualenv secretsanta
source $VENV_DIR/$VENV_NAME/bin/virtualenv_activate
. virtualenv_activate.sh secretsanta
echo $VIRTUAL_ENV
workon secretsanta
sudo pip install --upgrade -r requirements -t $VENV_DIR/$VENV_NAME
cd $VENV_DIR/$VENV_HOME/secretsanta
./manage.py migrate

#!/bin/bash

###################################
# Script to set up the python env
###################################

if python --version | grep '3.6'; then
    # Making sure dependencies are installed
    pip install flask
    pip install nltk
    pip install rivescript
    pip install numpy
    pip install boto3

else
    echo "Incorrect version of python. Cannot launch chatbot"
    exit
fi

# Launch the bot
python ./vunl-bot/chatApi.py
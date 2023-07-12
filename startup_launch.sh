#!/bin/bash

sleep 5
sudo python3 /home/onzme/Research-Project/GUI_tkinter.py
cd /home/onzme/Research-Project/server.py
flask run --host=0.0.0.0


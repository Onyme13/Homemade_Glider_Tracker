#!/bin/bash

sleep 2
sudo python3 /home/onzme/Research-Project/GUI_tkinter.py

sleep 2
cd /home/onzme/Research-Project/server.py
flask run --host=0.0.0.0


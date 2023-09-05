#!/bin/bash

sleep 2

cd Homemade_Glider_Tracker

sleep 1

sudo python3 ./server.py &

sleep 2

sudo python3 ./GUI_tkinter.py



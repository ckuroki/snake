#!/usr/bin/bash
nohup pico8 -o state.out -run snake.p8 &
python agent.py

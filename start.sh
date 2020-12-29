#!/bin/bash 
function check {
	if [ $1 -eq 1 ]; then
		echo "Dependencies missing. Installing $2..."
		pip3 install $2 >/dev/null
	fi
}
echo "Checking dependencies..."
python3 -c "import discord"
check $? discord.py
python3 -c "import praw"
check $? praw
python3 main.py
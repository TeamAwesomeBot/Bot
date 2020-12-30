#!/bin/bash 
function check {
	if [ $1 -eq 1 ]; then
		echo -e "Dependencies missing. Installing $2..."
		pip3 install $2 > /dev/null 2>&1
		echo -e "Successfully installed $2."
	fi
}
echo -e "Checking dependencies..."

lst=("import praw" "import discord")
mods=("praw" "discord.py")
for ((i = 0; i < ${#lst[@]}; i++)); do
    python -c "${lst[$i]}" > /dev/null 2>&1
	check $? "${mods[$i]}"
done
printf "\n"
python3 main.py
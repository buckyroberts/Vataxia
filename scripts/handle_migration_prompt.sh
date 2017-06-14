#!/usr/bin/expect -f

set answer [lindex $argv 0]

spawn python /home/bucky/Desktop/Projects/Vataxia/manage.py makemigrations
expect "Select an option: "
send "1\n"
expect ">>>"
send "$answer\n"
interact

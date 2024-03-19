#!/bin/bash
# Prompt for password
#Syam
echo "Please Enter the listsearch password"

sleep 5
read -s -p "Password:"  password
echo

#read $password

echo $password >>  /opt/password.txt

sleep 3


echo "=================="
echo "Password Updated"
echo "=================="

# Check if password is correct
#if [[ "$password" == "" ]]; then
#    echo "Access granted."
#else
#    echo "Access denied."
#fi


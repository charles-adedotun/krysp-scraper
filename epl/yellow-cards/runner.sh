#!/bin/bash

file_list=['teams.py','teams2.py','referees.py']

for py_file in file_list
do
    python3 $py_file
done
#!/bin/sh
for f in $(find tests -iname "*.in")
do
	./main_script.py $f > $f.out
done

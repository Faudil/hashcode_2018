#!/bin/bash
for f in $(find tests -iname "*.in")
do
	time ./main_script.py $f > $f.out &
done

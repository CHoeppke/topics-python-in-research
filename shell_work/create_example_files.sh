#!/bin/bash
for x in 0 1 2 3 4 5 6 7 8 9
do
    touch examplefile$x
done

for x in 0 1 2 3
do
    mkdir exampledir$x
done
touch exampledir1/examplefileA
touch .hiddenexamplefile
echo "Test in a file" > exampledir1/examplefile.txt

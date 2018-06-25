#!/bin/bash
for x in 0 1 2 3 4 5 6 7 8 9
do
    touch tmp2/examplefile$x
done

for x in 0 1 2 3
do
    mkdir tmp2/exampledir$x
done
touch tmp2/exampledir1/examplefileA
touch tmp2/.hiddenexamplefile
echo "Test in a file" > tmp2/exampledir1/examplefile.txt

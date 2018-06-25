#!/bin/bash

function cleanLatexMess {
    junklist=$(find ./tmp -name *.$1)
    for JF in $junklist;
    do
        echo "Removing" $JF
        rm $JF
    done
}
#Clear the working environment
rm -rf tmp/*
echo "Cleaned the working environment"


# Create some directories
for x in 0 1 2 3 4 5 6 7 8 9;
do
    echo "Created directory" $x
    mkdir tmp/MyDir$x
done

# Create some files
for y in 1 2 3 4 5;
do
    echo "Create File" $y "with important information"
    touch ./tmp/MyFile$y
    # Save some important information
    echo "My secret code is" $((0 + RANDOM % 1000)) > ./tmp/MyFile$y
done

#Solving the exercises:

# Example 1:
clear
echo "Exercise 4"
touch foo\ bar
ls
# sleep 1s
rm foo\ bar
ls
# sleep 1s

# Example 2:
clear
echo "Exercise 4"
touch ./\-\r\f
ls
# sleep 1s
rm ./\-\r\f
ls
# sleep 1s

#Example 3:
clear
echo "Exercise 4"
touch nasty\ \$\SHELL
ls
# sleep 1s
rm nasty\ \$\SHELL
ls
# sleep 1s

# Example 4 remove Latex by-products
# First create some Latex-junk
clear
echo "Exercise 4"
echo "Creating some latex junk"
for x in 1 2 3;
do
    cp $HOME/Templates/Latex-Journal.tex ./tmp/MyDir$x/Example.tex
    cp $HOME/Templates/CRPITStyle.cls ./tmp/MyDir$x
    cd ./tmp/MyDir$x
    #Compile latex and silence output
    latex Example.tex > /dev/null
    cd ..
    cd ..
done
echo "Created some latex junk"
sleep 0.5s

# Now clean up the latex junk:
echo "Cleaning up the mess I just made"
cleanLatexMess aux
cleanLatexMess log
cleanLatexMess out

# Example 5 list all executable files in a directory including
# the hidden ones

clear
echo "Moving on to exercise 5"
echo "Create a testing environment"
for x in 1 2 3 4 5;
do
    touch ./tmp/myExecutableFile$x.sh
    echo "echo My important secret is $x" > ./tmp/myExecutableFile$x.sh
    chmod a+x ./tmp/myExecutableFile$x.sh
done

for x in 1 2 3;
do
    touch ./tmp/.myHiddenExecutableFile$x.sh
    echo "echo My important secret is $x" > ./tmp/.myHiddenExecutableFile$x.sh
    chmod a+x ./tmp/.myHiddenExecutableFile$x.sh
done

# Now list all executable files
filelist=$(find tmp -executable -type f)
for fname in $filelist;
do
    echo $fname
done
sleep 1s


# Exercise 6: List all directories
clear
echo "Exercise 6: List all directories"
dirlist=$(find ./tmp -type d)
for myDir in $dirlist;
do
    echo $myDir
done
sleep 1s

# Exercise 7: A function that determines if a file is older than my .zshrc
clear
echo "Exercise 7:"

function olderThanZSHrc(){
    dateZSHrc=$(echo $(($(date +%s) - $(date +%s -r "$HOME/.zshrc"))))
    dateFile=$(echo $(($(date +%s) - $(date +%s -r "$1"))))

    if test $dateFile -gt $dateZSHrc
    then
        echo "The file '"$1"' is older than my ZSHrc"
    else
        echo "The file '"$1"' is not older than my ZSHrc"
    fi
}

olderThanZSHrc example1.sh
olderThanZSHrc ~/Documents/scannedDocuments.pdf

#!/bin/bash
pyenv versions | grep 2.7.2
if [ $? -ne 0 ];
then
pyenv install 2.7.2
else
echo "!!! 2.7.2 was installed before !!!"
fi

pyenv versions | grep 3.7.2
if [ $? -ne 0 ];
then
pyenv install 3.7.2
else
echo "3.7.2 was installed before"
fi

pyenv versions | grep 1st272
if [ $? -ne 0 ];
then
pyenv virtualenv 2.7.2 1st272
else
echo "1st272 was installed before"
fi

pyenv versions | grep 2nd372
if [ $? -ne 0 ];
then
pyenv virtualenv 3.7.2 2nd372
else
echo "2nd372 was installed before"
fi





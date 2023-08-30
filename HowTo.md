## How to run the tests in this project

## First step
cd cd ~/playwright/test

## Run all the tests

pytest -s

## Run a specific test by file name, for example run test_header.py

pytest test_header.py -s 

## Run all the tests and generate an html report

pytest -s cd --html=report.html
#!/usr/bin/env bash
# variables
#export INFILE=test.in
# run cmd with input from INFILE pip the ouput to cmd1
./cmd2 < $INFILE | ./cmd1
#!/usr/bin/env bash
#OUTFILE = test
out=${OUTFILE}.out
err=${OUTFILE}.err
echo $out
echo $err
./cmd1 < $INFILE | ./cmd3 > $out 2> $err
#!/bin/bash
CWD=$(pwd)
TS=$(date +%s)

source $CWD/venv/bin/activate
python $CWD/run.py > $CWD/scrapes/$TS.json

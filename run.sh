#!/bin/bash
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TS=$(date +%s)

source $CWD/venv/bin/activate
python $CWD/run.py > $CWD/scrapes/$TS.json

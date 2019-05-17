#! /usr/bin/bash
set FLACK_ENV=production
nohup flask run --host 0.0.0.0 --port 80 > nohup.out &
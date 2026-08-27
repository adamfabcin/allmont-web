#!/bin/bash
cd "$(dirname "$0")" || exit 1
PORT=8123
while lsof -nP -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; do PORT=$((PORT+1)); done
( sleep 1; open "http://localhost:$PORT" ) &
exec python3 serve.py "$PORT"

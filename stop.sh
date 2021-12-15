#  shell script to exit the program

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

# Create initial data in DB
python ./initial_data.py


# Run server
exec uvicorn --reload --host "$HOST" --port "$PORT" "$APP_MODULE" &

sleep 15

# LASTPID=$!

# kill -9 $LASTPID

kill -9 $(lsof -t -i tcp:$PORT)

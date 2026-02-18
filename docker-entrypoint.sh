#!/bin/sh
export PYTHONUNBUFFERED=1
if [ -z "$DISPLAY" ]; then
  export DISPLAY=:99
  Xvfb :99 -screen 0 1024x768x24 &
fi
exec jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
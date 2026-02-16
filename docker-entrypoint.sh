#!/bin/sh
# If DISPLAY is not set (e.g. no X11 forwarding), use virtual display so the app runs headless.
if [ -z "$DISPLAY" ]; then
  export DISPLAY=:99
  Xvfb :99 -screen 0 1024x768x24 &
fi
exec jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

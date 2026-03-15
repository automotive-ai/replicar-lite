# replicar-lite: run Jupyter + example notebook on Linux (e.g. from macOS host)
# Python 3.8 to match packages/python3.8/linux/aai
# Platform must be amd64: the pre-built .so packages are x86_64-linux-gnu (won't load on arm64).
FROM --platform=linux/amd64 python:3.8-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    unzip \
    build-essential \
    libx11-6 \
    libxrender1 \
    libxcb1 \
    libxext6 \
    libgl1 \
    libglvnd0 \
    libegl1 \
    libgles2 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir jupyter

WORKDIR /workspace

# Copy repo (maps, packages, notebook, images) and entrypoint
COPY maps ./maps
COPY packages ./packages
COPY images ./images
COPY example.ipynb ./
COPY data ./data
COPY README.md LICENSE.md ./
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN apt-get update && apt-get install -y --no-install-recommends imagemagick
RUN chmod +x /docker-entrypoint.sh

# libtensorflow.so is required at runtime. Copy zip and/or .so (at least one must exist in repo root).
COPY libtensorflow* ./
RUN if [ ! -f libtensorflow.so ]; then unzip -o libtensorflow.zip && rm -f libtensorflow.zip; fi

# So the notebook and native modules find packages and libtensorflow
ENV PYTHONPATH=/workspace/packages/python3.8/linux/aai
ENV LD_LIBRARY_PATH=/workspace:/usr/local/lib
ENV QEMU_CPU=max

EXPOSE 8888

# Entrypoint: if DISPLAY is set (X11 forwarding), use it; else start Xvfb for headless run
ENTRYPOINT ["/docker-entrypoint.sh"]


FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    python3-tk \
    libtk8.6 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /appli_python2
COPY appli.py .
COPY index.json .
COPY produit.txt .
COPY utilisateur.csv .
RUN pip install matplotlib
RUN pip install requests
CMD ["xvfb-run","python", "appli.py"]

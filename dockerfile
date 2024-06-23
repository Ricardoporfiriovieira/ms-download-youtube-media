# Use a imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /ms-download-youtube-media

# Copia os arquivos necessários para o container
COPY ./ms-download-youtube-media /ms-download-youtube-media

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Abre a porta 80 para o tráfego HTTP
EXPOSE 80

# Comando para executar o servidor FastAPI usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
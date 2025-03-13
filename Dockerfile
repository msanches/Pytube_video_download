# Base image
FROM python:3.10-slim

# Instalar dependências
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para iniciar o script
CMD ["python", "main.py"]
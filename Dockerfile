# Usa imagem oficial Python
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo código para dentro do container
COPY . .

# Comando padrão para rodar o script
CMD ["python", "main.py"]

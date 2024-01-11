#Imagem do python
FROM python:3.8

#Diretorio do projeto
WORKDIR /app

#Copiar os arquivos de configuracao, deps e codigo
COPY requirements.txt .

# Instalar as dependencias
RUN pip install --no-cache-dir -r requirement.txt

#Comando de execucao do app
CMD ["python", "main.py"]

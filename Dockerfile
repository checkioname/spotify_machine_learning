#Imagem do python
FROM python:3.8

USER user

#Diretorio do projeto
WORKDIR /app

#Copiar os arquivos de configuracao, deps e codigo
COPY /app/requirements.txt .

# Configuração do Apache Airflow
COPY airflow/ /opt/airflow/

# Adiciona o diretório de DAGs
COPY airflow/dags/ /opt/airflow/dags/

# Instalar as dependencias
RUN echo 'root:sua_senha' | chpasswd
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN apt-get update && apt-get install -y duckdb


#Comando de execucao do app
CMD ["python", "main.py"]

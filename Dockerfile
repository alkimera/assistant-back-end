FROM python:3.11.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Define variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copia o script entrypoint para o container
COPY entrypoint.sh /entrypoint.sh

# Torna o script executável
RUN chmod +x /entrypoint.sh

# Define o script como ponto de entrada
ENTRYPOINT ["/entrypoint.sh"]

# Comando para rodar a aplicação
CMD ["flask", "run"]
#!/bin/sh

echo "Executando migrações do Flask-Migrate..."
flask db upgrade

echo "Iniciando a aplicação Flask..."
exec flask run

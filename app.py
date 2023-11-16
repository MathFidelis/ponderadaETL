from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_ingestao = db.Column(db.DateTime, default=datetime.utcnow)
    tipo = db.Column(db.String(50))
    valores = db.Column(db.String(100))
    uso = db.Column(db.String(100))

def fetch_weather(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7058a786edbe467bb14b38cd5bdc54dd')
    return response.json() if response.status_code == 200 else None

def transform(city, data):
    details = {key: data['main'].get(key) for key in ['temp', 'humidity', 'pressure']}
    return {'tipo': city, 'valores': json.dumps(details), 'uso': 'previsão'}

def load(data):
    db.session.add(WeatherData(**data))
    db.session.commit()

@app.route('/etl')
def etl():
    cities = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Fortaleza', 'Belo Horizonte', 'Acre', 'Rio Grande do Sul', 'Alagoas', 'Brasília', 'Foz do Iguaçu']
    [load(transform(city, fetch_weather(city))) for city in cities if fetch_weather(city)]

    return {'message': 'ETL executado com sucesso.'}

@app.route('/data')
def get_data():
    return jsonify([{'data_ingestao': entry.data_ingestao.strftime('%Y-%m-%d %H:%M:%S'),
                     'tipo': entry.tipo,
                     'uso': entry.uso,
                     'valores': json.loads(entry.valores)} for entry in WeatherData.query.all()])

if __name__ == '__main__':
    with app.app_context(): db.create_all()
    app.run(debug=True)

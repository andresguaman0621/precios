from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Archivo para almacenar los datos
DATA_FILE = 'productos_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    productos = load_data()
    categorias = list(set(p['categoria'] for p in productos if p.get('categoria')))
    return render_template('index.html', productos=productos, categorias=categorias)

@app.route('/api/productos')
def api_productos():
    productos = load_data()
    categoria = request.args.get('categoria', '')
    codigo = request.args.get('codigo', '')
    nombre = request.args.get('nombre', '')
    
    # Aplicar filtros
    if categoria:
        productos = [p for p in productos if p.get('categoria', '').upper() == categoria.upper()]
    if codigo:
        productos = [p for p in productos if str(p.get('codigo', '')).startswith(codigo)]
    if nombre:
        productos = [p for p in productos if nombre.upper() in p.get('nombre_completo', '').upper()]
    
    return jsonify(productos)

@app.route('/api/guardar_precio', methods=['POST'])
def guardar_precio():
    data = request.json
    codigo = data.get('codigo')
    precio_actual = data.get('precio_actual')
    
    productos = load_data()
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['precio_anterior'] = producto.get('precio_actual', '')
            producto['precio_actual'] = precio_actual
            break
    
    save_data(productos)
    return jsonify({'success': True})

@app.route('/api/guardar_todos', methods=['POST'])
def guardar_todos():
    data = request.json
    productos = load_data()
    
    for item in data:
        codigo = item.get('codigo')
        precio_actual = item.get('precio_actual')
        
        for producto in productos:
            if producto['codigo'] == codigo:
                if precio_actual != producto.get('precio_actual'):
                    producto['precio_anterior'] = producto.get('precio_actual', '')
                    producto['precio_actual'] = precio_actual
                break
    
    save_data(productos)
    return jsonify({'success': True})

@app.route('/api/nueva_toma', methods=['POST'])
def nueva_toma():
    productos = load_data()
    
    for producto in productos:
        producto['precio_anterior'] = producto.get('precio_actual', '')
        producto['precio_actual'] = ''
    
    save_data(productos)
    return jsonify({'success': True})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
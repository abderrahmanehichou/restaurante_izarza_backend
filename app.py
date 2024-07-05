from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import config

from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config.from_object(config['development'])

# Configuración de CORS
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:5001"}})
CORS(app, resources={r"/api/*": {"origins": "*"}})

conexion = MySQL(app)

@app.route('/api/menus/sondika', methods=['GET'])
def obtener_menu_sondika():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Sondika'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/txorierri', methods=['GET'])
def obtener_menu_txorierri():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.id AS plato_id, p.nombre AS plato_nombre, 
                GROUP_CONCAT(DISTINCT a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM platos p
            JOIN elementos_menu em ON p.id = em.plato_id
            JOIN menus m ON em.menu_id = m.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE m.id IN (
                SELECT m.id
                FROM subcategorias s
                JOIN menus m ON s.id = m.subcategoria_id
                WHERE s.nombre = 'Txorierri'
            )
            GROUP BY p.id, p.nombre
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
  

@app.route('/api/menus/izarza', methods=['GET'])
def obtener_menu_izarza():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Izarza'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/berreteaga', methods=['GET'])
def obtener_menu_berreteaga():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Berreteaga'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/errekalde', methods=['GET'])
def obtener_menu_errekalde():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Errekalde'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/goietxea', methods=['GET'])
def obtener_menu_goietxea():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Goietxea'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/kumea', methods=['GET'])
def obtener_menu_kumea():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Kumea'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/plato_combinado', methods=['GET'])
def obtener_menu_plato_combinado():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Plato combinado'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/menu_del_dia', methods=['GET'])
def obtener_menu_menu_del_dia():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú del día'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/menu_chuleton', methods=['GET'])
def obtener_menu_menu_chuleton():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú chuletón'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/menu_express_1', methods=['GET'])
def obtener_menu_menu_express_1():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú Express 1'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0]} # , 'alergenos': fila[1]
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/menu_express_2', methods=['GET'])
def obtener_menu_menu_express_2():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú Express 2'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]} 
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/lubarrieta', methods=['GET'])
def obtener_menu_lubarrieta():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú Lubarrieta'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})

@app.route('/api/menus/aixerrota', methods=['GET'])
def obtener_menu_aixerrota():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Menú Aixerrota'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/paseo_por_la_carta', methods=['GET'])
def obtener_menu_paseo_por_la_carta():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Paseo por la carta'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/kumea_especial', methods=['GET'])
def obtener_menu_kumea_especial():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'kumea_especial'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/plato_combinado_especial', methods=['GET'])
def obtener_menu_plato_combinado_especial():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Plato combinado especial'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})


@app.route('/api/menus/entrantes', methods=['GET'])
def obtener_menu_entrantes():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Entrantes'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/pescados', methods=['GET'])
def obtener_menu_pescados():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Pescados'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/carnes', methods=['GET'])
def obtener_menu_carnes():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Carnes'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/postres', methods=['GET'])
def obtener_menu_postres():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Postres'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/coffe_break_1', methods=['GET'])
def obtener_menu_coffe_break_1():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Coffe break 1'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/coffe_break_2', methods=['GET'])
def obtener_menu_coffe_break_2():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Coffe break 2'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/coffe_break_3', methods=['GET'])
def obtener_menu_coffe_break_3():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Coffe break 3'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/lunch_1', methods=['GET'])
def obtener_menu_lunch_1():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Lunch 1'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/lunch_2', methods=['GET'])
def obtener_menu_lunch_2():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Lunch 2'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/lunch_3', methods=['GET'])
def obtener_menu_lunch_3():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Lunch 3'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})
    

@app.route('/api/menus/lunch_4', methods=['GET'])
def obtener_menu_lunch_4():
    try:
        cursor = conexion.connection.cursor()
        consulta = """
            SELECT p.nombre AS nombre_plato, 
                   GROUP_CONCAT(a.nombre ORDER BY a.nombre SEPARATOR ', ') AS alergenos
            FROM subcategorias s
            JOIN menus m ON s.id = m.subcategoria_id
            JOIN elementos_menu em ON m.id = em.menu_id
            JOIN platos p ON em.plato_id = p.id
            LEFT JOIN platos_alergenos pa ON p.id = pa.plato_id
            LEFT JOIN alergenos a ON pa.alergeno_id = a.id
            WHERE s.nombre = 'Lunch 4'
            GROUP BY p.id
            ORDER BY p.id;
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        platos = []
        for fila in resultado:
            plato = {'nombre_plato': fila[0], 'alergenos': fila[1]}
            platos.append(plato)
        return jsonify({'platos': platos, 'mensaje': 'Platos listados.'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error', 'error': str(ex)})

def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe.</h1>", 404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(port=5001)

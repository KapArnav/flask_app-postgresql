from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host='localhost', 
        port=5432,  
        dbname='postgres', 
        user='postgres', 
        password='123'  
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/students', methods=['GET'])
def api_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students') 
    students = cur.fetchall() 
    cur.close()
    conn.close()
    

    student_list = [{'id': student[0], 'name': student[1], 'grade': student[2]} for student in students]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug=True)

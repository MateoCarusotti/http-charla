from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

# Usuarios simulados para prueba
users = {'admin': 'password123', 
         'magma': 'ocean', 'cloud': 'flame', 
         'bird': 'leaf', 'pine': 'spoon', 
         'moon': 'storm', 'star': 'sand' }


def buscar_string_en_archivo(nombre_archivo, string_a_buscar):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()  
        
        if string_a_buscar in contenido:  
            return True  
        else:
            return False  


@app.route('/')
def home():
    if 'username' in session:
        username = session['username'] 
        return render_template('home.html', username=username)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Datos Invalidos')
    
    return render_template('login.html')

@app.route('/ingresar_dato')
def ingresar_dato():
    with open('scoreboard.txt' ,mode= 'a', encoding= 'UTF-8') as score:
        username = session['username']
        if not buscar_string_en_archivo('scoreboard.txt', username):
        
            current_time = datetime.now()

            score.write(f"{current_time} - {username}\n")

    return render_template('home.html', username=username, message= '¡Ya lo enviaste!')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    with open('scoreboard.txt' ,mode= 'w', encoding= 'UTF-8') as score:
        score.write('')
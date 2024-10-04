from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key'

# Usuarios simulados para prueba
users = {'admin': 'password123', 
         'magma': ['ocean', 'sacachispas'], 'cloud': ['flame','chicago'], 
         'bird': ['leaf', 'Berazategui'], 'pine': ['spoon', 'Ituzaingo'], 
         'moon': ['storm', 'Cambaceres'], 'star': ['sand', 'Yupanqui'] }

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        special_word = users[username][1]  # Segundo elemento del arreglo en el diccionario
        return render_template('home.html', username=username, special_word=special_word)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        
        if username in users and users[username][0] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Datos Invalidos')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
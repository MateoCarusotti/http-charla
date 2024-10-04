from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key'

# Usuarios simulados para prueba
users = {'admin': 'password123', 
         'magma': 'ocean', 'cloud': 'flame', 
         'bird': 'leaf', 'pine': 'spoon', 
         'moon': 'storm', 'star': 'sand' }

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        special_word = "4to año del Liceo" 
        return render_template('home.html', username=username, special_word=special_word)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        
        if username in users and users[username] == password:
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
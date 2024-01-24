from flask import Flask, render_template, request, redirect, url_for, jsonify,flash
import json
import sqlite3
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('PetPuja.db')
    cursor = conn.cursor()
    return conn, cursor

app=Flask(__name__)
users = {
    'Doab': {'password': '12345'},
    # Add more users as needed
}



@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        role=request.form['role']
        username = request.form['id']
        password = request.form['password']
        conn, cursor = get_db_connection()
        if(role=='Student'):
            user = cursor.execute('SELECT * FROM customers WHERE id = ?', (username,)).fetchone()

            if(user == None):
                # flash('Invalid Roll number.')
                # print('Invalid Roll number.')
                return '<script>alert("Incorrect Roll number Entered!");window.location.href = "/";</script>'
            # print(user)

            usernameint=int(username)

            # print(username)
            # print(password)
            # print((type(user[0]), type(username)) , (user[4] == password))

            if (user[0] == usernameint)  and (user[4] == password):
                # Login successful
                # return redirect(url_for('home'))
                print("Login successful")
                conn.close()
                return render_template('index2.html')

            else:
                # Login unsuccessful
                # return jsonify({'success': False})
                # flash('Incorrect password')
                conn.close()
                return '<script>alert("Incorrect Password Entered!");window.location.href = "/";</script>'

                # return render_template('login.html')

        elif(role=='CanteenAdmin'):
            user = cursor.execute('SELECT * FROM canteen WHERE id = ?', (username,)).fetchone()

            
            if(user == None):
                # flash('Invalid Roll number.')
                # print('Invalid Roll number.')
                conn.close()
                return '<script>alert("Incorrect Canteen Number Entered!");window.location.href = "/";</script>'
            # print(user)

            usernameint=int(username)

            # print(username)
            # print(password)
            # print((type(user[0]), type(username)) , (user[4] == password))
            # print(password)
            # print(user[4])
            if (user[0] == usernameint)  and (user[4] == password):
                # Login successful
                # return redirect(url_for('home'))
                print("Login successful")
                conn.close()
                return render_template('orders.html')

            else:
                # Login unsuccessful
                # return jsonify({'success': False})
                # flash('Incorrect password')
                conn.close()
                return '<script>alert("Incorrect Password Entered!");window.location.href = "/";</script>'

                # return render_template('login.html')

    return render_template('login.html')



@app.route('/signup.html', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        role=request.form['role']
        id=request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        print(id,name,email,phone,password)
        conn, cursor = get_db_connection()

        # Insert data into the customers table
        # print(role)
        if role=='Student':
            cursor.execute('''
                INSERT INTO customers (id,name,email,phone,password)
                VALUES (?, ?, ?, ?, ?)
            ''', (id, name, email, phone, password))

        elif role=='CanteenAdmin':
            # print('here')
            cursor.execute('''
                INSERT INTO canteen (id,name,email,phone,password)
                VALUES (?, ?, ?, ?,?)
            ''', (id, name, email, phone,password))
        # Commit the changes to the database
        conn.commit()
        conn.close()

    return render_template('signup.html')


@app.route('/stock.html', methods=['POST','GET'])
def stocktoorders():
    return render_template('orders.html')

@app.route('/orders.html', methods=['POST','GET'])
def ordertostock():
    return render_template('stock.html')

@app.route('/menu.html', methods=['POST','GET'])
def select_canteen():
    conn = sqlite3.connect('PetPuja.db')
    c = conn.cursor()
    c.execute("SELECT id,name FROM canteen")
    data=c.fetchall()
    datalol=[]

    if request.method=='POST':
        id = request.form['id']
        c.execute("SELECT name,price from Prepared_dishes WHERE canteen_id=(?)", (id))
        datalol=c.fetchall()
    conn.close()
    return render_template('menu.html', canteen=data, datalol=datalol)


@app.route('/use_canteen', methods=['POST', 'GET'])
def use_canteen():
    id = request.form['id']
    print(id)
    conn = sqlite3.connect('PetPuja.db')
    c = conn.cursor()
    c.execute("SELECT name,price from Prepared_dishes WHERE canteen_id=(?)", (id))
    datalol=c.fetchall()
    c.execute("SELECT id,name FROM canteen")
    data=c.fetchall()
    print(datalol, data)
    conn.close()
    return render_template('menu.html', canteen=data, datalol=datalol)

@app.route("/index2.html",methods=['POST','GET'])
def home():
    return render_template('index2.html')


@app.route("/food.html",methods=['POST','GET'])
def food():
    return render_template('food.html')

@app.route("/faq.html",methods=['POST','GET'])
def faq():
    return render_template('faq.html')

@app.route("/about.html",methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.route("/index2.html",methods=['POST','GET'])
def index2():
    return render_template('index2.html')

@app.route("/menu.html",methods=['POST','GET'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        number=request.form['phone']
        canteen=request.form['canteen']
        order1=request.form['message1']
        order2=request.form['message2']
        order3=request.form['message3']
        if canteen=='JC':
          with open('info1.txt',"a") as f:
              f.write(name+','+email+','+number+','+order1+','+order2+','+order3+'\n')
        if canteen=='VC':
          with open('info2.txt',"a") as f:
              f.write(name+','+email+','+number+','+order1+','+order2+','+order3+'\n')
        if canteen=='BBC':
          with open('info3.txt',"a") as f:
              f.write(name+','+email+','+number+','+order1+','+order2+','+order3+'\n')
        if len(order2)==0 and len(order3)==0:
            order=order1
        if len(order2)==0 and len(order3)!=0:
            order=order1+','+order3
        if len(order2)!=0 and len(order3)==0:
            order=order1+','+order2
        if len(order2)!=0 and len(order3)!=0:
            order=order1+','+order2+','+order3
        studentdata=[]
        studentdata.append({'name':name,'email':email,'phone':number,'order':order,'canteen':canteen})
        return render_template('Tracking.html',orders=studentdata)
    else:
        return render_template('menu.html')

@app.route("/details1",methods=['GET'])
def order1():
    with open('info1.txt','r') as f:
        data=f.readlines()
        studentdata=[]
        for line in data:
            userdata=line.strip().split(',')
            name=userdata[0]
            email=userdata[1]
            phone=userdata[2]
            order=userdata[3]+','+userdata[4]+','+userdata[5]
            studentdata.append({'name':name,'email':email,'phone':phone,'order':order})
        return render_template('jc.html',orders=studentdata)

@app.route("/details2",methods=['GET'])
def order2():
    with open('info2.txt','r') as f:
        data=f.readlines()
        studentdata=[]
        for line in data:
            userdata=line.strip().split(',')
            name=userdata[0]
            email=userdata[1]
            phone=userdata[2]
            order=userdata[3]+','+userdata[4]+','+userdata[5]
            studentdata.append({'name':name,'email':email,'phone':phone,'order':order})
        return render_template('vc.html',orders=studentdata)

@app.route("/details3",methods=['GET'])
def orde3r():
    with open('info3.txt','r') as f:
        data=f.readlines()
        studentdata=[]
        for line in data:
            userdata=line.strip().split(',')
            name=userdata[0]
            email=userdata[1]
            phone=userdata[2]
            order=userdata[3]+','+userdata[4]+','+userdata[5]
            studentdata.append({'name':name,'email':email,'phone':phone,'order':order})
        return render_template('bbc.html',orders=studentdata)

if __name__=="__main__":
    app.run(debug=True)
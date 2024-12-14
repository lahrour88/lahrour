from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/logane')
def log():
    return render_template('logane.html')


@app.route('/about')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('2cole.html')
 
@app.route('/page4')
def page4():
    return render_template('1cole.html')


@app.route('/page5')
def page5():
    return render_template('2bac.html')

@app.route('/page6')
def page6():
    return render_template('3cole.html')


@app.route('/page7')
def page7():
    return render_template('5eme.html')
 
@app.route('/page8')
def page8():
    return render_template('6eme.html')

# lesson fr

@app.route('/less1')
def less1():
    return render_template('less1.html')
    
@app.route('/less2')
def less2():
    return render_template('less2.html')
    

@app.route('/less3')
def less3():
    return render_template('less3.html')

@app.route('/less4')
def less4():
    return render_template('less4.html')
    
@app.route('/less5')
def less5():
    return render_template('less5.html')
    
@app.route('/less6')
def less6():
    return render_template('less6.html')
    


@app.route('/less7')
def less7():
    return render_template('less7.html')

# less arabec
@app.route('/PC')
def PC1():
    return render_template('PC.html')

@app.route('/arless1')
def ar():
    return render_template('ar less1.html')
    
@app.route('/arless2')
def arless2():
    return render_template('arless2.html')
    

@app.route('/arless3')
def arless3():
    return render_template('arless3.html')

    
@app.route('/less5')
def arless5():
    return render_template('arless5.html')
    
@app.route('/less6')
def arless6():
    return render_template('arless6.html')
#exercice pc
@app.route('/expc')
def expc():
    return render_template('expc.html')

# troncomin
@app.route('/less1')
def  tcarless1():
    return render_template('TRC/less1.html')
    

@app.route('/less2')
def tcarless2():
    return render_template('TRC/less2.html')

    
@app.route('/tcarless4')
def tcarless4():
    return render_template('TRC/less3.html')
    

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app= Flask(__name__)

@app.route('/welcome')
def welcome_page():
    html="""
    <html>
        <h1>Welcome</h1> 
    </html> 
    """
    return html

@app.route('/welcome/home')
def home_page():
    html="""
    <html>
        <h1>Welcome Home</h1> 
    </html>
    """
    return html

@app.route('/welcome/back')
def welcome_back_page():
    html="""
    <html>
        <h1>Welcome Back</h1>
    </html>
    """
    return html

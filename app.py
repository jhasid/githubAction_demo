from flask import Flask
import os

app=Flask(__name__)

@app.route('/',methods=['Get'])
def index():
    return "hello world"

if __name__=="__main__":
    app.run()
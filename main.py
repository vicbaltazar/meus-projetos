from flask import Flask
app = Flask (__name__)

from views import *

#Executar
if __name__ == '__main__':
    app.run(debug=True)
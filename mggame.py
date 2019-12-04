from flask import Flask
from flask import request
import mgdt
app = Flask(__name__)




@app.route('/')
def mg():
    with open('./mg.html','r') as aa:
        data = aa.read()
    return data



@app.route('/dt', methods=["GET", "POST"])
def dt():
    return mgdt.data;







if __name__ == '__main__':
    app.run()
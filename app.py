from flask import Flask, request
import handlers

app = Flask(__name__)

@app.route('/')
def indexpage():
    return "Welcome"

@app.route("/search", methods =['GET'])
def search():
    if request.method == 'GET':
        query = request.args.get('name')
        return handlers.search_query(query=query)
    return "Error"

if (__name__ == '__main__'):
    app.run(debug=True)
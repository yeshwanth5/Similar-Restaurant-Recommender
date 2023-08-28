from flask import Flask, request, jsonify
from utils import utils
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
utils=utils()

@app.route('/get_restaurant_names',methods=['GET'])
def get_restaurant_names():
    restaurant_names = utils.get_restaurant_names()
    response = jsonify({
        'restaurant_names' : restaurant_names
    })
    return response

@app.route('/get_similar_restaurants',methods=['POST'])
def get_similar_restaurants():
    restaurant_name = request.form['restuarant_name']
    similar_restaurants = utils.get_nearest_neighbours(restaurant_name)
    response = jsonify({
        'similar_restaurants' : similar_restaurants
    })
    return response
    
if __name__ == '__main__':
    app.run(debug=True)
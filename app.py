import random
from flask import Flask, render_template

app = Flask(__name__)
map_list = ['Ancient', 'Anubis', 'Inferno', 'Mirage', 'Nuke', 'Overpass', 'Vertigo', 'Tuscan', 'Dust II', 'Train',
            'Cache', 'Agency', 'Office']
map_list_wingman = ['Boyard', 'Chalice', 'Vertigo', 'Inferno', 'Overpass', 'Cobblestone', 'Train', 'Nuke', 'Shortdust', 'Lake']
@app.route('/', methods=['GET', 'POST'])
def index():
    new_heading = str(map_list[random.randint(0, 11)])
    return render_template('index.html', new_heading=new_heading)

@app.route('/wingman', methods=['GET'])
def get_random_map():
    return random.choice(map_list_wingman)

if __name__ == '__main__':
    app.run(debug=True)

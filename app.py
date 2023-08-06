import random

from flask import Flask, render_template,request

app = Flask(__name__)
map_list = ['Ancient', 'Anubis', 'Inferno', 'Mirage', 'Nuke', 'Overpass', 'Vertigo', 'Tuscan', 'Dust II', 'Train',
            'Cache', 'Agency', 'Office']


@app.route('/', methods=['GET', 'POST'])
def index():
    new_heading = str(map_list[random.randint(0, 12)])
    if request.method == 'POST':
        # Handle the POST request here (if needed)
        pass
    return render_template('index.html',new_heading=new_heading)

if __name__ == '__main__':
    app.run(debug=True)

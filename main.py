from flask import Flask, render_template, request
import albumart_loader
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')
	
@app.route("/search", methods=['GET'])
def search():
	data = request.args
	if 'query' in data:
		query = data['query']
	else:
		query = 'Vincent Laguardia Gambini Sings Just for You'
	return render_template('search.html', imgs = albumart_loader.get_urls(query))

if __name__ == '__main__':
	app.run()

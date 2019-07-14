from flask import Flask, render_template, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/plot/temp')
def plot_temp():
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.set_title("Temperature [°C]")
	axis.set_xlabel("x")
	axis.set_ylabel("y = x^2 + 1")
	axis.grid(True)
	xs = np.arange(1, 10, 0.5)
	ys = xs**2 + 1
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

if __name__ == "__main__":
   app.run()
from tkinter import *
from datetime import date, timedelta
import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg ,NavigationToolbar2Tk)
from functools import lru_cache

root = Tk()
root.title("astro graph")
root.geometry("1080x690")
root.iconbitmap("Resources/code.ico")


@lru_cache(maxsize=None)
def getData():
   DATE = date.today()
   Date = DATE - timedelta(days=1)
   api_key = "py1vSxJlQkBACx6of5pchXzVL4FzMNmMmgO3qLYl"
   url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={Date}&end_date={Date}&api_key={api_key}"
   api = requests.get(url)
   data = api.json()
   element_count = data['element_count']
   distance = []
   size = []
   for i in range(element_count):
      miss_distance = data['near_earth_objects'][f"{Date}"][i][
          'close_approach_data'][0]['miss_distance']['kilometers']
      dis_data = int(float(miss_distance))
      distance.append(dis_data)
      size_max = data['near_earth_objects'][f"{Date}"][i][
          'estimated_diameter']['kilometers']['estimated_diameter_max']
      size.append(size_max)
   size_list = []
   for i in range(len(size)):
      size_data = size[i]
      size_no = int(float(size_data))
      size_list.append(size_no)
      element = 0
      neo_count = []
   for j in range(element_count):
      element += 1
      neo_count.append(element)
   return distance, neo_count




distance_x, element_count_y = getData()

def save_graph():
   global distance_x, element_count_y
   DATE = date.today()
   Date = DATE - timedelta(days=1)
   plt.scatter(distance_x, element_count_y, edgecolors="black", c="red", s=10)
   plt.savefig(f"astro_graph{Date}.png")


graph_fig = Figure(figsize=(5,5), dpi=50)
graph_fig.add_subplot(111).scatter(distance_x, element_count_y, edgecolors="black", c="red")
canvas = FigureCanvasTkAgg(graph_fig, master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
save_btn = Button(root, text="Save", bg="#1EE8AB", fg="white", command=save_graph, width= 30)
save_btn.pack(side=BOTTOM, expand=1)
root.mainloop()


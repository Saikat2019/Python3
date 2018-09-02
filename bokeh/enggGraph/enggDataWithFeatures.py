from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df=pandas.read_csv("bachelors.csv")

x=df["Year"]
y=df["Engineering"]

f=figure(plot_width=500,plot_height=500,tools='pan',logo=None)
f.title.text="Cool Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Data"
f.yaxis.axis_label="Intensity"

f.line(x,y)

output_file("bachelors.html")
show(f)
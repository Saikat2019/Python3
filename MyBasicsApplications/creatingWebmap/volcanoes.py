import folium
import pandas

map=folium.Map(location=[40.58,-110.09],zoom_start=5)

data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fg=folium.FeatureGroup(name="Volcanoes Map")

def getColor(elevation):
    if elevation<=1000:
        return "green"
    elif 1000< elevation<=2000:
        return "beige"
    elif 2000< elevation<=3000:
        return "lightred"
    elif 3000< elevation<=4000:
        return "red"
    elif elevation>4000:
        return "darkred"
for la,lo,el in zip(lat,lon,elev):

    fg.add_child(folium.Marker(location=[la,lo],popup=str(el)+"m",icon=folium.Icon(color=getColor(el))))
                                                     #folium.Popup(str(elev)+"m",parse_html=True)
map.add_child(fg)
map.save("Volcanoes.html")

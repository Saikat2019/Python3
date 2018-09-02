import folium
import pandas

map=folium.Map(location=[40.58,-110.09],zoom_start=5)

data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fgv=folium.FeatureGroup(name="Volcanoes Map")
fgp=folium.FeatureGroup(name="Population Map")

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
    fgv.add_child(folium.Marker(location=[la,lo],popup=str(el)+"m",icon=folium.Icon(color=getColor(el))))
                                                     #folium.Popup(str(elev)+"m",parse_html=True)

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
                               style_function=lambda x :{"fillColor":"green" if x["properties"]["POP2005"]<=10000000
                                                                             else "yellow" if 10000000<x["properties"]["POP2005"]<=200000000
                                                                             else "orange" if 200000000<x["properties"]["POP2005"]<=500000000
                                                                             else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("polygonLayers.html")

import folium

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")
Coordinates=[[37.3,-97.8],[39.05,-96.23],[40,-96.8],[37.5,-98.9]]
for coordinate in Coordinates:
    fg.add_child(folium.Marker(location=coordinate,popup="Marker here",icon=folium.Icon(color="Yellow")))

map.add_child(fg)

map.save("foliumBegining.html")

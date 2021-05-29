import folium

m = folium.Map(location = [36.48755210716709, 127.25417828425252], zoom_start=12)
folium.Marker([36.48755210716709, 127.25417828425252], icon=folium.Icon(color='purple',icon='info-sign'),popup=m).add_to(m)
folium.Marker([36.355845392177216, 127.34289586922338], icon=folium.Icon(color='red',icon='info-sign'),popup=m).add_to(m)
folium.Marker([36.375380274851096, 127.31970895787448], icon=folium.Icon(color='green',icon='info-sign'),popup=m).add_to(m)
folium.Marker([36.39088501185242, 127.36552897107842], icon=folium.Icon(color='orange',icon='info-sign'),popup=m).add_to(m)
folium.Marker([36.374262841051994, 127.32403913853334], icon=folium.Icon(color='blue',icon='info-sign'),popup=m).add_to(m)
m.save('Chopssal.html')


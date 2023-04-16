import folium

# Define a localização do marcador
location = [-23.5505, -46.6333]

# Cria um mapa do Folium centrado na localização do marcador
m = folium.Map(location=location, zoom_start=13)

# Adiciona um marcador na localização definida com um pop-up
folium.Marker(location=location, popup="São Paulo").add_to(m)

# Exibe o mapa
m.save("map.html")
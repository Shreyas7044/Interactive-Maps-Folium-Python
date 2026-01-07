import folium
import pandas as pd

# Load stadium data
data = pd.read_csv("stadium.csv", encoding="cp1252")

latitude = list(data['LAT'])
longitude = list(data['LON'])
name = list(data["NAME"])
capacity = list(data["capacity"])
website = list(data["website"])
picture = list(data['picture'])

# Create feature group
f = folium.FeatureGroup("Indian Cricket Stadiums")

# Add India states geojson
f.add_child(
    folium.GeoJson(
        data=open("india_states.json", 'r', encoding='utf-8-sig').read()
    )
)

# Add markers
for lt, ln, nm, cp, ws, pic in zip(latitude, longitude, name, capacity, website, picture):
    f.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=(
                f"<b>Name:</b> {nm}<br>"
                f"<b>Capacity:</b> {cp}<br>"
                f"<b>Wikipedia:</b> <a href={ws} target='_blank'>Click here</a><br>"
                f"<img src={pic} height='142' width='290'>"
            ),
            icon=folium.Icon(color="green")
        )
    )

# Create map
map = folium.Map(location=[21.1458, 79.0082], zoom_start=5)
map.add_child(f)

# Save map
map.save("map.html")
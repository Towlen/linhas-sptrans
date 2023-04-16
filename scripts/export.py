from routes import Routes
import pandas as pd
import folium

class Export(Routes):
    def __init__(self, routes_file="bus_routes.csv", areas_file="sptrans_areas.csv", data_folder="../data/output_tables"):
        super().__init__(filename=routes_file, data_folder=data_folder)
        self.areas = pd.read_csv(f"{data_folder}/{areas_file}")
        self.shapes = pd.read_csv('../data/gtfs_data/shapes.txt')

    def get_color_by_areaid(self, area_id):
        color_id = self.areas[self.areas['area_id'] == area_id]['area_color'].values
        return color_id[0] if len(color_id) > 0 else None

    def export_view(self, df):
        m = folium.Map(location=[-23.5477, -46.6623], zoom_start=11)
        for index, row in df.iterrows():
            # extrair as coordenadas do shapes.txt pelo 'shape_id'
            shapeid = row['shape_id']
            coords = self.shapes.loc[self.shapes['shape_id'] == shapeid].reset_index()
            coords2 = coords[['shape_pt_lat', 'shape_pt_lon']].to_records(index=False)
            # construir a view
            color = self.get_color_by_areaid(row['route_areaid'])
            popup_html = "<h3>{}-{}</h3>{}<p>{:.1f} km</p>".format(row['route_id'], row['route_code'], row['route_long_name'], row['shape_dist_traveled'])
            popup = folium.Popup(popup_html, max_width=300)
            polyline = folium.PolyLine(coords2, color=f'#{color}', weight=3.5, opacity=1)
            polyline.add_child(popup)
            polyline.add_to(m)
        return m
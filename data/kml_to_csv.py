import os, csv
from bs4 import BeautifulSoup

kml_path = "neighborhood_clusters.kml"
kml_path = os.path.normpath(kml_path)

output_path = "neighborhood_clusters.csv"
output_path = os.path.normpath(output_path)

data_tag = "PolyID"

out = open(output_path, 'w')
headers = "\"Polygon_ID\",\"Point_ID\",\"Latitude\",\"Longitude\"\n"
out.write(headers)

with open(kml_path, 'r') as f:
   soup = BeautifulSoup(f, 'html.parser')
   coord_tag = soup.select('coordinates')
   id = soup.select('simpledata')
   
   count_poly = 1
   for data in coord_tag:
      poly_tag = data_tag + str(count_poly) # add here
      count_poly += 1
      text_data = data.string.rstrip().lstrip().split(" ")
      count_point = 1
      for item in text_data:
         coords = item.split(",")
         longitude = coords[0]
         latitude = coords[1]
         out.write("\"" + str(poly_tag) + "\",\"" + str(count_point) + "\",\"" + latitude + "\",\"" + longitude + "\"\n")
         count_point += 1
f.close()
out.close()
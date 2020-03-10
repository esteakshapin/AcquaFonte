import csv

filename = 'static/AcquaFonte (GIS infor included).csv'


with open(filename) as csvfile:
  markers_file = csv.reader(csvfile, delimiter=',')
  i = 0
  for row in markers_file:
    if (i != 0 ):
      markers.insert_one({'name': row[0], 'lat': row[1], 'lon': row[2],'type': row[3], 'status': row[6], 'ratings': [], 'comments': [row[5]]})
      i+= 1
    else:
      i+=1
    

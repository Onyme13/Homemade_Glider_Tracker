""" This script is used to strore map tiles (256x256) in a database. 
To be used later for offline use """

import os
import sqlite3

zoom_array =[]

#name of the database file
db_name = "MAP_OSM"
db_name = db_name + ".db"

#create database 
conn = sqlite3.connect(db_name)

conn.execute("CREATE TABLE IF NOT EXISTS server (server VARCHAR(255), max_zoom INT);")

#create table
conn.execute("CREATE TABLE IF NOT EXISTS tiles (zoom INTEGER, x INTEGER, y INTEGER, server VARCHAR(255) DEFAULT 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png' , tile_image BLOB);") 

# file path of the tiles
dir_path = 'C:/Users/jocor/Desktop/tiles_OSM' 

for zoom in os.listdir(dir_path):
    zoom_array.append(int(zoom))
    progess_bar =""
    print("Processing zoom level: "+ str(zoom))
    for x in os.listdir(os.path.join(dir_path, zoom)):
        progess_bar += "-"
        print(progess_bar)
        for y in os.listdir(os.path.join(dir_path, zoom, x)):
           
            tile_path = os.path.join(dir_path, zoom, x, y)
            
            y = y.split(".")[0]
            
            with open(tile_path, "rb") as file:
                tile_blob = file.read()

            conn.execute("""INSERT INTO tiles (zoom, x, y, tile_image) VALUES (?,?,?,?);""",(zoom, x, y, tile_blob))

zoom = max(zoom_array)
conn.execute("INSERT INTO server (server, max_zoom) VALUES (?,?);",('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png',zoom))

conn.commit()
conn.close()

print("================================================================")
print("Database created successfully")
print("Stored tiles in DB" + str(db_name))
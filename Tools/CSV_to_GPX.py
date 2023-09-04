"""Function that creates a gpx file from a csv file. For a GPS Visualizer like https://www.gpsvisualizer.com/"""


import csv
import xml.etree.ElementTree as ET
import datetime
import random




def create_gpx(csv_filename, gpx_filename):


    elem =0


    # Create the root GPX element
    gpx = ET.Element("gpx", version="1.1", xmlns="http://www.topografix.com/GPX/1/1")

    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  

        for row in csv_reader:
            elem+=1
            #"lat,long,alt,time"
            lat, lon, alt, time = row  

            wpt = ET.SubElement(gpx, "wpt", lat=str(lat), lon=str(lon))
            ET.SubElement(wpt, "ele").text = str(elem)
            ET.SubElement(wpt, "name").text = str(alt)

    tree = ET.ElementTree(gpx)
    tree.write(gpx_filename, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":

    current_datetime = datetime.datetime.now()
    # Get the current date in the format: YYYY-MM-DD
    current_date = current_datetime.date()

    glider_models = [
        "ASK-21",
        "ASK-13",
        "ASK-18",
        "DG-1000",
        "SZD-48 Jantar",
        "LS8",
        "Discus",
        "Ventus",
        "Nimbus",
        "Blanik",
        "Libelle",
        "PW-5 Smyk",
        "Standard Cirrus",
        "Schempp-Hirth Duo Discus",
        "Pilatus B4",
        "Grob G102 Astir",
        "DG Flugzeugbau DG-808",
        "JS1 Revelation",
        "Rolladen-Schneider LS4",
        "Swift S-1"
        ]   
    
    #Choose a random glider model, this is just for prototyping
    random_integer = random.randint(0, len(glider_models) - 1)


    file_name = "data/"  + glider_models[random_integer] + " " + str(current_date) + ".gpx"


    csv_filename = "data/mouvement.csv"  
    gpx_filename = "data/"  + glider_models[random_integer] + "_" + str(current_date) + ".gpx"
    create_gpx(csv_filename, gpx_filename)
    print(f"Conversion from {csv_filename} to {gpx_filename} complete.")

import requests
import datetime
import pytz
import time
import os
import sys
import subprocess

BASE_URL = "http://api.open-notify.org/iss-now.json"
NUM_RUNS = 10
WAIT_TIME = 30  # 30 seconds between points

# Start KML
kml_content = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>ISS Trajectory</name>
    <Style id="issPointStyle">
      <IconStyle>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/pal2/icon2.png</href>
        </Icon>
      </IconStyle>
    </Style>
"""

collected_points = 0

for i in range(NUM_RUNS):
    try:
        # Get ISS position
        r = requests.get(BASE_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        lon = float(data["iss_position"]["longitude"])
        lat = float(data["iss_position"]["latitude"])

        # Current UTC time
        now = datetime.datetime.now(pytz.utc).strftime("%d/%m/%Y %H:%M:%S UTC")

        # Add placemark with "on" before date
        kml_content += f"""
    <Placemark>
      <name>Point {i+1} - on {now}</name>
      <styleUrl>#issPointStyle</styleUrl>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>
"""
        collected_points += 1
        print(f"✅ Collected point {i+1}/{NUM_RUNS} at {now}")

        if i < NUM_RUNS - 1:
            time.sleep(WAIT_TIME)

    except Exception as e:
        print("❌ Error:", e)
        break

# Close KML
kml_content += """
  </Document>
</kml>
"""

# Save file with updated naming (date with dashes)
file_name = f"ISS_trajectory_on_{datetime.datetime.now(pytz.utc).strftime('%d-%m-%Y_at_%H-%M-%S_UTC')}.kml"
with open(file_name, "w") as f:
    f.write(kml_content)

print(f"\n✨ File '{file_name}' created with {collected_points} points!")

# Try opening automatically
try:
    if sys.platform.startswith("win"):
        os.startfile(file_name)
    elif sys.platform == "darwin":
        subprocess.run(["open", file_name])
    else:
        subprocess.run(["xdg-open", file_name])
    print("🌍 Opening in Google Earth (or your default KML viewer)...")
except Exception as e:
    print("⚠️ Could not open automatically:", e)

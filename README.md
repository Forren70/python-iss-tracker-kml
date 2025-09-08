# **Python Script for Real-Time ISS Tracking and KML Visualization**

This script retrieves the International Space Station's (ISS) live position using a public API and generates a KML file to visualize its trajectory in Google Earth, combining Python programming, API integration, and geospatial visualization.

![ISS Trajectory visualized in Google Earth](https://github.com/Forren70/python-iss-tracker-kml/blob/main/ISS-trajectory-GoogleEarth.png)
*In this screenshot from Google Earth, the ISS trajectory is above the Pacific Ocean, about 1000 km East of Kiribati islands, moving approximately from NNW to SSE.*

## Features
-Real-Time Data Acquisition: Uses the "Where the ISS at?" API to get the exact -coordinates (latitude, longitude, altitude) of the ISS.

-Geospatial Visualization: Converts the data into a KML file that can be imported into Google Earth for a dynamic 3D visualization.

-Temporal Data Handling: Each tracked point includes a UTC timestamp for a -precise log of the path.

-Custom Icons: The KML file includes a custom icon representing the ISS, enhancing the visual experience.

## Requirements
To run this script, ensure you have the following installed:
-Python 3.x

-Python Modules: requests (for API calls) and simplekml (for KML file generation). You can install them via pip:
pip install requests simplekml

-Google Earth: To visualize the generated KML file.

## How to Run
1) Clone this repository to your local machine or download the script.
git clone https://github.com/Forren70/python-iss-tracker-kml.git

2) Navigate to the project directory.
cd python-iss-tracker-kml

3) Execute the script from the command line:
python iss_tracker.py

4) The script will automatically generate a file named iss_trajectory.kml and open it in Google Earth, showing the ISS's path.

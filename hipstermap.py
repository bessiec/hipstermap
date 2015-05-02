"""
Made a roadtrip of the most hipster destinations in America using the codebase for Optimal Roadtrip 
by Randal S. Olson: http://www.randalolson.com/2015/03/08/computing-the-optimal-road-trip-across-the-u-s/
Hipster neighborhoods populated based off the following lists and my own opinions about hipster neighborhoods:
http://www.forbes.com/sites/morganbrennan/2012/09/20/americas-hippest-hipster-neighborhoods/
http://www.thrillist.com/travel/nation/coolest-neighborhoods-in-america-the-mission-wicker-park-and-highland-park-top-our-list
http://www.thrillist.com/travel/nation/americas-most-hipster-cities-epicenter-of-the-american-hipster-in-2013
http://www.travelandleisure.com/slideshows/americas-best-cities-for-hipsters-2013/5
"""

import googlemaps 
from itertools import combinations

gmaps = googlemaps.Client(key="AIzaSyDkJdKtzn4J0bTF68OnZPuYw1cjva5HsOs")

all_waypoints = ["Silver Lake, Los Angeles, CA", # As an Angeleno, clearly I am partial to the hipster neighborhoods of my city. 
				"Los Feliz, Los Angeles, CA",
				"Highland Park, Los Angeles, CA",
				"Arts District, Los Angeles, CA",
				"The Mission, San Francisco, CA", # I lived in SF for five years, a piece of my heart will always be left there! 
				"Venice Beach, CA",
				"North Park, San Diego, CA",
				"East Austin, Austin, TX", # Breakfast tacos! 
				"Somerville, MA",
				"Wicker Park, Chicago, IL",
				"Alberta, Portland, OR", # The dreams of the 90s are alive in Portland... Portland... Portland... 
				"Pearl District, Portland, OR",
				"Downtown, Portland, OR",
				"North Loop, Minneapolis, MN",
				"Kansas City, MO",
				"Hampden, Baltimore, MD", # I wonder how John Waters feels about this 
				"Little Five Points, Atlanta, GA",
				"East Nashville, Nashville, TN", # Rednecks and hipsters!  Miller Lite versus PBR! 
				"Bushwick, Brooklyn, NY", 
				"Williamsburg, Brooklyn, NY",
				"H Street Corridor, Washington, DC",
				"Capitol Hill, Seattle, WA",
				"The Uptown, Oakland, CA",
				"Warehouse District, New Orleans, LA"
				"Louisville, KY",
				"Savannah, GA",
				"Boulder, CO",
				"Asheville, NC",
				"Northern Liberties, Philadelphia, PA",
				"LoHi, Denver, CO",
				"Allston-Brighton, Boston, MA",
				"Wynwood, Miami, FL",
				"Westheimer Road, Houston, TX",
				"Providence, RI",
				"Charleston, SC",
				"Portland, ME"]



waypoint_distances = {}
waypoint_durations = {}

for (waypoint1, waypoint2) in combinations(all_waypoints, 2):
    try:
        route = gmaps.distance_matrix(origins=[waypoint1],
                                      destinations=[waypoint2],
                                      mode="driving", 
                                      language="English",
                                      units="metric")

        # "distance" is in meters
        distance = route["rows"][0]["elements"][0]["distance"]["value"]

        # "duration" is in seconds
        duration = route["rows"][0]["elements"][0]["duration"]["value"]

        waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
        waypoint_durations[frozenset([waypoint1, waypoint2])] = duration
    
    except Exception as e:
        print("Error with finding the route between %s and %s." % (waypoint1, waypoint2))

with open("my-waypoints-dist-dur.tsv", "wb") as out_file:
    out_file.write("\t".join(["waypoint1",
                              "waypoint2",
                              "distance_m",
                              "duration_s"]))
    
    for (waypoint1, waypoint2) in waypoint_distances.keys():
        out_file.write("\n" +
                       "\t".join([waypoint1,
                                  waypoint2,
                                  str(waypoint_distances[frozenset([waypoint1, waypoint2])]),
                                  str(waypoint_durations[frozenset([waypoint1, waypoint2])])]))
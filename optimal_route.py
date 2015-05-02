"""
Made a roadtrip of the most hipster destinations in America using the codebase for Optimal Roadtrip 
by Randal S. Olson: http://www.randalolson.com/2015/03/08/computing-the-optimal-road-trip-across-the-u-s/
Hipster neighborhoods populated based off the following lists and my own opinions about hipster neighborhoods:
http://www.forbes.com/sites/morganbrennan/2012/09/20/americas-hippest-hipster-neighborhoods/
http://www.thrillist.com/travel/nation/coolest-neighborhoods-in-america-the-mission-wicker-park-and-highland-park-top-our-list
http://www.thrillist.com/travel/nation/americas-most-hipster-cities-epicenter-of-the-american-hipster-in-2013
http://www.travelandleisure.com/slideshows/americas-best-cities-for-hipsters-2013/5
"""

optimal_route = ('Williamsburg, Brooklyn, NY', 'Bushwick, Brooklyn, NY', 'Allston-Brighton, Boston, MA', 'Somerville, MA', 'Portland, ME', 'Providence, RI', 'Northern Liberties, Philadelphia, PA', 'Hampden, Balitmore, MD', 'Warehouse District, New Orleans, LALouisville, KY', 'Wicker Park, Chicago, IL', 'North Loop, Minneapolis, MN', 'Kansas City, MO', 'LoHi, Denver, CO', 'Boulder, CO', 'Capitol Hill, Seattle, WA', 'Alberta, Portland, OR', 'Pearl District, Portland, OR', 'Downtown, Portland, OR', 'The Mission, San Francisco, CA', 'The Uptown, Oakland, CA', 'Venice Beach, CA', 'Los Feliz, Los Angeles, CA', 'Silver Lake, Los Angeles, CA', 'Highland Park, Los Angeles, CA', 'Arts District, Los Angeles, CA', 'North Park, San Diego, CA', 'East Austin, Austin, TX', 'Westheimer Road, Houston, TX', 'East Nashville, Nashville, TN', 'Little Five Points, Atlanta, GA', 'Wynwood, Miami, FL', 'Savannah, GA', 'Charleston, SC', 'Asheville, NC', 'H Street Corridor, Washington, DC')

optimal_route = list(optimal_route)
optimal_route += [optimal_route[0]]
subset = 0
    
while subset < len(optimal_route):
    
    waypoint_subset = optimal_route[subset:subset + 10]
    output = "calcRoute(\"%s\", \"%s\", [" % (waypoint_subset[0], waypoint_subset[-1])
    for waypoint in waypoint_subset[1:-1]:
        output += "\"%s\", " % (waypoint)
        
    if len(waypoint_subset[1:-1]) > 0:
        output = output[:-2]
        
    output += "]);"
    print(output)
    print("")
    subset += 9
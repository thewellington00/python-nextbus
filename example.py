import nextbus

# get a list of agencies
agencies = nextbus.agency_list()

# grab the SF Muni agency object
sfmuni = [a for a in agencies if a.title=='San Francisco Muni'][0]

# get a list of route objects on the SF Muni
routes = nextbus.route_list(agency=sfmuni.tag)

# grab a specific route object, in this case "1-California"
r = [r for r in routes if r.title=='1-California'][0]

# get more info on that route
route = nextbus.route_config(agency=sfmuni.tag, route=r.tag)

# grab a stop on that route
stop = [s for s in route.stops if s.title=='California St & Spruce St'][0]

# get the prediction objects for that route and stop
predictions = nextbus.predictions(agency=sfmuni.tag, route=route.tag, stop_id=stop.stop_id)
print 'Vehicles arrive in ' + ', '.join([p.minutes for p in predictions]) + ' minutes'




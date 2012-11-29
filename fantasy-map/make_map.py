#!/usr/bin/env python
import mapnik
print ''
print '=' * 42
print '-' * 42
print 'Making...'
print '-' * 42
mapfile = "style.xml"
m = mapnik.Map(1690, 800)
mapnik.load_map(m, mapfile)
#bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
#bbox = mapnik.Envelope(mapnik.Coord(-80, 30.0), mapnik.Coord(-49.0, 54.0))
#bbox = mapnik.Envelope(mapnik.Coord(-90, 40.0), mapnik.Coord(-64.0, 50.0))
bbox = mapnik.Envelope(mapnik.Coord(-70, 45.0), mapnik.Coord(-54.0, 50.0))
m.zoom_to_box(bbox) 
mapnik.render_to_file(m, 'map.png', 'png')
mapnik.save_map(m,'generated_map.xml')
print '-' * 42
print 'Made!'
print '-' * 42
print ''

import ephem
import random
from datetime import datetime

MIN_ALTITUDE = '10:00:00'

# Exam Date 28-12-2013
iiserb = ephem.Observer()
iiserb.lat = '23.289002'
iiserb.lon = '77.273153'
iiserb.elevation = 500
#iiserb.date = '2013/12/28'

# exam date 26-12-2015
ratibad = ephem.Observer()
ratibad.lat = '23.166765'
ratibad.lon = '77.325822'
ratibad.elevation = 500

# exam date 23-12-2017
radharaman = ephem.Observer()
radharaman.lat = '23.160305'
radharaman.lon = '77.330573'
radharaman.elevation = 500
radharaman.date = '2017/12/23'

objects_string = ["Polaris", "Vega", "Deneb", "Altair", "Caph", "Schedar",
"Scheat",  "Algenib", "Fomalhaut", "Hamal", "Aldebaran", "Atlas",
"Capella", "Menkalinan", "Achernar", "Elnath", "Bellatrix",  "Rigel",
"Mintaka", "Alnilam", "Betelgeuse", "Alnitak", "Saiph", "Castor", "Sirius", "Dubhe",
"Procyon", "Pollux", "Merak", "Canopus", "Megrez", "Phecda", "Alphard", "Algieba",
"Regulus", "Alioth", "Mizar", "Denebola", "Alcaid"
]
exam_venue = radharaman

j = ephem.Jupiter()
j.compute(exam_venue)

objects = []
for s in objects_string:
    objects.append(ephem.star(s))

#["Ruchbah" "Alpheratz", "Cursa", , "RNGC 1980", "M 42"]
ruchbah = ephem.FixedBody()
ruchbah.name = "Ruchbah"
ruchbah._ra = '0:56:42.0'
ruchbah._dec = '60:43:00.0'

alpheratz = ephem.FixedBody()
alpheratz.name = "Alpheratz"
alpheratz._ra = '0:08:23.0'
alpheratz._dec = '29:05:26.0'

cursa = ephem.FixedBody()
cursa.name = "Cursa"
cursa._ra = '5:07:51.0'
cursa._dec = '-5:05:11.0'

rngc1980 = ephem.FixedBody()
rngc1980.name = "RNGC 1980"
rngc1980._ra = '5:36:27.0'
rngc1980._dec = '-5:54:35.0'

m42 = ephem.FixedBody()
m42.name = "M 42"
m42._ra = '5:35:21.0'
m42._dec = '-5:23:31.0'


m45 = ephem.FixedBody()
m45.name = "M 45"
m45._ra = '3:47:24.0'
m45._dec = '24:7:0.0'

other_objects = [ruchbah, alpheratz,  cursa, rngc1980, m42, m45]


#["Saturn", "Mars", "Moon","Jupiter"]
objects.append(ephem.Saturn())
objects.append(ephem.Mars())
objects.append(ephem.Moon())
objects.append(ephem.Jupiter())
objects = objects + other_objects

#for o in objects:    
#    print o.name
#    exam_venue.date = '2013/12/27 19:30:00'
#    try: 
#        print 
#       print str(ephem.localtime( exam_venue.next_rising(o) )) + " " + str(ephem.localtime(exam_venue.next_transit(o))) + " " + str(ephem.localtime( exam_venue.next_setting(o)) ) 
#        print ephem.localtime( exam_venue.next_rising(o)).strftime("%Y-%m-%d %H:%M:%S")
#    	exam_venue.date = exam_venue.next_rising(o)
#        print ephem.localtime( exam_venue.next_transit(o)).strftime("%Y-%m-%d %H:%M:%S")
#        print ephem.localtime( exam_venue.next_setting(o)).strftime("%Y-%m-%d %H:%M:%S")
#    except ephem.CircumpolarError: 
#        print 'NA'
        
def isSafelyUp(obj):    
    exam_venue.date = ephem.now()
    obj.compute(exam_venue)
#    if not(obj.alt > ephem.degrees(MIN_ALTITUDE)) :
#        print obj.name
#        print obj.alt
    return obj.alt > ephem.degrees(MIN_ALTITUDE)

# Pick N random objects that are not set
def pick(n):
    assert(n>0)
    filtered_objects = list(filter(lambda o: isSafelyUp(o) ,objects))
    print( "Total number of Sky Objects in the DB : " + str(len(objects)))
    print( "Number of Sky Objects in the sample : " + str(len(filtered_objects)))
    print( "Selecting " + str(n) + " Sky Objects")
    return random.sample(filtered_objects, n)

for o in pick(5):
    print (o.name)
##import gtk
#from gi.repository import Gtk 

#class ExamApp:
    #def __init__(self):
        #filename = "examui.glade"
        #builder = Gtk.Builder()
        #builder.add_from_file(filename)
        #builder.connect_signals(self)
        #builder.get_object("window1").show_all() 

    #def buttonWriteNameToFile_clicked(self, widget):
        #print("File write code...")

#if __name__ == "__main__":
    #app = ExamApp()
    #Gtk.main()

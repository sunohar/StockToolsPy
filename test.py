from panchanga import planetary_positions, sidereal_longitude, ketu, Date, Place
import swisseph as swe

# namah suryaya chandraya mangalaya ... rahuve ketuve namah
swe.KETU = swe.PLUTO  # I've mapped Pluto to Ketu
SUN = swe.SUN; MOON = swe.MOON; MARS = swe.MARS;  MERCURY = swe.MERCURY; JUPITER = swe.JUPITER;
VENUS = swe.VENUS; SATURN = swe.SATURN; MEAN_NODE =  swe.MEAN_NODE; RAHU = MEAN_NODE; KETU = swe.KETU;
URANUS = swe.URANUS; NEPTUNE = swe.NEPTUNE 


# 'jd' can be any time: ex, 2015-09-19 14:20 UTC
# today = swe.julday(2015, 9, 19, 14 + 20./60)
def planet_position(jd, place, planet):
    """Computes instantaneous planet position   """
    jd_ut = jd - place.timezone / 24.

    if planet != swe.KETU:
        nirayana_long = sidereal_longitude(jd_ut, planet)
    else: # Ketu
        nirayana_long = ketu(sidereal_longitude(jd_ut, swe.RAHU))

    return nirayana_long

if __name__ == "__main__":
    print("starting...")
    # hyderabad = Place(17.383, 78.484, +5.5)
    # today = swe.julday(2020, 3, 10, 18 + 00./60)
    # planet_pos = planetary_positions(today, hyderabad)
    # for planet in planet_pos:
    #     print(planet) 

    hyderabad = Place(17.383, 78.484, +5.5)
    jd = swe.julday(2020, 3, 15, 12 + 00./60)
    print(jd)
    position = planet_position(jd, hyderabad, swe.GURU)
    print(position)
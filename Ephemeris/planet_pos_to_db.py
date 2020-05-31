from panchanga import planetary_positions, sidereal_longitude, ketu, Date, Place
import swisseph as swe
import sqlite3
from datetime import datetime, timedelta

# namah suryaya chandraya mangalaya ... rahuve ketuve namah
#swe.KETU = swe.PLUTO  # I've mapped Pluto to Ketu
SUN = swe.SUN; MOON = swe.MOON; MARS = swe.MARS;  MERCURY = swe.MERCURY; JUPITER = swe.JUPITER;
VENUS = swe.VENUS; SATURN = swe.SATURN; MEAN_NODE =  swe.MEAN_NODE; RAHU = MEAN_NODE; KETU = swe._KETU;
URANUS = swe.URANUS; NEPTUNE = swe.NEPTUNE 

def get_name(planet):
  names = { SUN: 'SUN', MOON: 'MOON', MARS: 'MARS',
            MERCURY: 'MERCURY', JUPITER: 'JUPITER', VENUS: 'VENUS',
            SATURN: 'SATURN', RAHU: 'RAHU', KETU: 'KETU', URANUS: 'URANUS', NEPTUNE: 'NEPTUNE'}

  return names[planet]


# 'jd' can be any time: ex, 2015-09-19 14:20 UTC
# today = swe.julday(2015, 9, 19, 14 + 20./60)
def planet_position(jd, place, planet):
    """Computes instantaneous planet position   """
    jd_ut = jd - place.timezone / 24.

    if planet != swe._KETU:
        nirayana_long = sidereal_longitude(jd_ut, planet)
    else: # Ketu
        nirayana_long = ketu(sidereal_longitude(jd_ut, swe._RAHU))

    return nirayana_long


if __name__ == "__main__":
    print("Starting Program...")

    # Input parameters
    # start_date = '1980-01-01'
    start_date = '1980-01-01'
    end_date = '2030-12-31'
    hyderabad = Place(17.383, 78.484, +0.0)
    planet = KETU
    # End of Input parameters

    start_datetime = f"{start_date} 15:30:00"
    end_datetime = f"{end_date} 15:30:00"
    end_datetime_object = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
    planet_name = get_name(planet)

    conn = sqlite3.connect('ephemeris.db3')
    cursor = conn.cursor()

    datetime_object = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
    print(datetime_object)
    print(end_datetime_object)
    while(datetime_object <= end_datetime_object):
        jd = swe.julday(datetime_object.year, datetime_object.month, datetime_object.day, 15 + 30./60)
        position = planet_position(jd, hyderabad, planet)
        sqlstmt =  f"INSERT INTO planet_position_daily (planet,date_time,place,position) \
                    VALUES ('{planet_name}', '{datetime_object.strftime('%Y-%m-%d %H:%M:%S')}', 'hyderabad', {position})"
        print(f"Date: {datetime_object.strftime('%Y-%m-%d %H:%M:%S')} position: {position}")
        cursor.execute(sqlstmt)
        datetime_object = datetime_object + timedelta(days=1)
        datediff = end_datetime_object - datetime_object

    conn.commit()
    conn.close()
    print("Program Completed.")
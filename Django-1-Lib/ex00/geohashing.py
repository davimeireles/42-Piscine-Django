import sys

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def encoding_geohash(latitude, longitude, precision=12):
    latitude_interval = (-90.0, 90.0)
    longitude_interval = (-180.0, 180.0)
    
    binary_latitude = ''
    binary_longitude = ''
    binary_string = ''
    
    geohash = ''
        
    while len(binary_longitude) < precision:
        # Longitude encoding
        longitude_half = (longitude_interval[0] + longitude_interval[1]) / 2
        if longitude > longitude_half:
            binary_longitude += '1'
            longitude_interval = [longitude_half, longitude_interval[1]]
        else:
            binary_longitude += '0'
            longitude_interval = [longitude_interval[0], longitude_half]
        
    while len(binary_latitude) < precision:
        # Latitude encoding
        latitude_half = (latitude_interval[0] + latitude_interval[1]) / 2
        if latitude > latitude_half:
            binary_latitude += '1'
            latitude_interval = [latitude_half, latitude_interval[1]]
        else:
            binary_latitude += '0'
            latitude_interval = [latitude_interval[0], latitude_half]    

    for i in range(0, len(binary_longitude)):
        binary_string += binary_longitude[i]
        binary_string += binary_latitude[i]
    
    for b in range(0, len(binary_string), 5):
        chunk = binary_string[b:b+5]
        index = int(chunk, 2)
        geohash += BASE32[index]

    return geohash
        
if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception("Usage: python3 geohashing.py (latitude) (longitude)")
        
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
            try:
                if not -90 <= latitude <= 90:
                    raise Exception("Latitude must be between 90 and -90")
                if not -180 <= longitude <= 180:
                    raise Exception("Longitude must be between 180 and -180")
                geohash = encoding_geohash(latitude=latitude, longitude=longitude)
                print(f'Encoding hash for latitude({latitude}) and longitude({longitude}) is [ {geohash} ]')
            except Exception as error:
                print(f'{error}')
        except ValueError:
            raise Exception("Use numbers for latitude and longitude and if its a float use '.'")        
        
    except Exception as error:
        print(f'{error}')
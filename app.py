from geocode.geocode import get_latitude_and_longitude_by_address


def run():
    address = input("Please enter a valid address.")
    latitude, longitude = get_latitude_and_longitude_by_address(address)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    return


if __name__ == '__main__':
    run()

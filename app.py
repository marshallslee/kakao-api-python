from geocode.geocode import get_latitude_and_longitude_by_address


def run():
    address = input("Please enter a valid address.")
    latitude, longitude = get_latitude_and_longitude_by_address(address)
    if latitude and longitude is not None:
        print("Latitude:", latitude)
        print("Longitude:", longitude)
    else:
        print("Failed to calculate latitude and longitude from the given address.")
    return


if __name__ == '__main__':
    run()

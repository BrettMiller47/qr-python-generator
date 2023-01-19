import segno
import io
from PIL import Image
from segno import helpers


def create_qr_location(latitude, longitude, name):
    """
    Creates a .png QR code for a location.  The QR code will automatically open the maps app on mobile.
    :param latitude: location's latitude
    :param longitude: location's longitude
    :param name: the location's name
    :return: a file named 'location-{name}.png'
    """
    # store the latitude and longitude in variable 'geo_uri'
    geo_uri = helpers.make_geo_data(latitude, longitude)
    geo_uri
    f'geo:{latitude},{longitude}'

    # Make the qr code & use error correction level "H"
    qrcode = segno.make(geo_uri, error='H')
    qrcode.designator
    '4-H'
    qrcode.save(f'location-{name}.png', scale=10)


def create_qr_wifi(ssid, password):
    """
    Creates a .png QR code for wifi access.
    :param ssid: the wifi's ssid
    :param password: the password for the wifi's ssid
    :return: a file named '{ssid}-wifi-access.png'
    """
    qrcode = helpers.make_wifi(ssid=ssid, password=password, security='WPA')
    qrcode.designator
    '3-M'
    qrcode.save(f'{ssid}-wifi-access.png', scale=10)


def create_qr_contact(name, email, phone, url=''):
    """
    Creates a .png QR code for contact info.
    :param name: contact's name
    :param email: contact's email
    :param phone: contact's phone number
    :param url: contact's personal site
    :return: a file named 'contact-{name}.png'
    """
    qrcode = helpers.make_mecard(name=name, email=email, phone=phone, url=url)
    qrcode.designator
    '4-H'
    qrcode.save(f'contact-{name}.png', scale=10)


if __name__ == '__main__':
    create_qr_contact('name', 'email', 'phone#', 'url')

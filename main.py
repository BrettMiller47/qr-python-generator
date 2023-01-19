import segno
import io
from PIL import Image
from segno import helpers


def create_qr_location(latitude, longitude, name):
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
    qrcode = helpers.make_wifi(ssid=ssid, password=password, security='WPA')
    qrcode.designator
    '3-M'
    qrcode.save(f'{ssid}-wifi-access.png', scale=10)


def create_qr_contact(name, email, phone, url=''):
    qrcode = helpers.make_mecard(name=name, email=email, phone=phone, url=url)
    qrcode.designator
    '4-H'
    qrcode.save(f'contact-{name}.png', scale=10)


if __name__ == '__main__':
    create_qr_contact('name', 'email', 'phone#', 'url')

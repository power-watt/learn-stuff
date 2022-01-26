# an example of how to read QR/barcodes
# code taken from https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/

from pyzbar import pyzbar # read QR/barcodes
import cv2


# read QR/barcode
def read(file_path):
    barcodes = pyzbar.decode(cv2.imread(file_path)) # finds all barcodes it can

    # loop through all barcodes
    for i, barcode in enumerate(barcodes):
        (x, y, w, h) = barcode.rect # spatial location in image

        barcode_data = barcode.data.decode('utf-8') # get encoded data
        barcode_type = barcode.type                 # encoding type

        text = 'barcode date: {} \t barcode type: {}'.format(barcode_data, barcode_type)
        print(i, text)

read('multi_qr.jpg')
read('hello_world.png')


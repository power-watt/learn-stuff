# an example of how to generate a QR Code - it's pretty easy
import qrcode # gnerate QR Code

# generate QR code
def gen(message, file_name):
    img = qrcode.make(message)

    img.save(file_name, 'png')

    plt.imshow(img)
    plt.show()

gen('hello world', 'hello_world.png')

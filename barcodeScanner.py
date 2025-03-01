# pip install pyzbar
import cv2
from pyzbar import pyzbar

class BarcodeScanner:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.barcodes = ''

    def detect_barcodes(self):
        # Convert the image to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Use pyzbar to detect barcodes in the image
        self.barcodes = pyzbar.decode(gray)
        return self.barcodes

    def draw_barcodes(self):
        # Loop over detected barcodes and draw rectangles around them
        for barcode in self.barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            text = f"{barcode_data}"
            cv2.putText(self.image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    def show_image(self):
        # Display the image with detected barcodes
        cv2.imshow("Barcode Scanner", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, output_path):
        # Save the image with detected barcodes to the specified path
        cv2.imwrite(output_path, self.image)

    def get_barcode_values(self):
        # Retrieve the values from detected barcodes
        barcode_values = [barcode.data.decode("utf-8") for barcode in self.barcodes]
        self.full_barcode_value = ''.join(barcode_values)  # Concatenate all barcode values into a single string
        return self.full_barcode_value

from PIL import Image
import io
import random


class Main:

    def __init__(self, filename, filename_added=None):
        self.filename = filename
        self.filename_added = filename_added

    def append_text(self):
        with open(str(filename), 'ab') as f:
            f.write(b"Test")

    def reveal_text(self):
        with open(filename, 'rb') as f:
            file = f.read()
            offset = file.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)
            return str(f.read())

    def reveal_text2(self):
        with open(filename, 'rb') as f:
            file = f.read()
            offset = file.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)
            message = str(f.read())
            if message.startswith("b'"):
                simplify = message[1:]
            return simplify

    def add_img_file(self):
        img = Image.open(self.filename_added)
        byte_array = io.BytesIO()
        img.save(byte_array, format='PNG')
        try:
            with open(self.filename, 'ab') as f:
                f.write(byte_array.getvalue())
        except PermissionError as e:
            print(e)
            pass

    def extract_img_file(self):
        with open(self.filename, 'rb') as f:
            file = f.read()
            offset = file.index(bytes.fromhex("FFD9"))
            f.seek(offset + 2)
            new_img = Image.open(io.BytesIO(f.read()))
            new_img.save(str(random.getrandbits(128)) + ".png")

    def add_exe(self):
        with open(self.filename, 'ab') as f, open('test_light.bat', 'rb') as e:
            f.write(e.read())

    def open_exe(self):
        with open(self.filename, 'rb') as f:
            file = f.read()
            offset = file.index(bytes.fromhex("FFD9"))
            f.seek(offset + 2)
            with open('new_exe.bat', 'wb') as e:
                e.write(f.read())


if __name__ == '__main__':
    second_filename = "chicken.png"
    filename = r"C:\Users\Caio Madeira\Documents\GitHub\greek-delivery\resources\assets\Capture.JPG"
    print(Main(filename=filename).reveal_text2())

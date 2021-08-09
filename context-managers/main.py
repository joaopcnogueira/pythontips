import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Implementing a Context Manager as a Class
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


if __name__ == '__main__':
    with File(os.path.join(BASE_DIR, 'demo.txt'), 'w') as opened_file:
        opened_file.write('Hola!')

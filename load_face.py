import os
import face_recognition
import json

class Loadface:

    def __init__(self):
        self.known_face=[]
        self.known_face_encoding=[]


    def read_face(self):
        face_name = os.listdir('face_photo')
        print('{}'.format(face_name))

        path = '/home/angel/Desktop/donkey_custom/angel_facerec/face_photo'
        for i in face_name:
            img_name = face_recognition.load_image_file('{}/{}'.format(path,i) ) 
            img_encoding = face_recognition.face_encodings(img_name)[0]
            self.known_face.append(i[:-4])
            self.known_face_encoding.append(list(img_encoding))


    def to_json(self):
        face = {'name': self.known_face , 'encoding': self.known_face_encoding }
        tojson = json.dumps(face)

        with open('rec_face.json','w') as f:
            f.write(tojson)

    def load_json(self):
        with open('rec_face.json','r') as f:
            load = json.load(f)
            self.known_face = load['name']
            self.known_face_encoding = load['encoding']

    def update(self, name):

        path = '/home/angel/Desktop/donkey_custom/angel_facerec/face_photo'
        img_name = face_recognition.load_image_file('{}/{}.jpg'.format(path,name) ) 
        img_encoding = face_recognition.face_encodings(img_name)[0]
        self.known_face.append(name)
        self.known_face_encoding.append(list(img_encoding))


if __name__ == '__main__':
    do = Loadface()
    #do.load_json()
    do.read_face()
    print(do.known_face)
    print('-'*20)
    print(do.known_face_encoding)
    do.to_json()


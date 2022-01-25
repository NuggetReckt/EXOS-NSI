class Domino:

    def __init__(self, face_a, face_b):
        self.face_a = face_a
        self.face_b = face_b
    def affiche_points(self):
        return self.face_a , self.face_b
    def total(self):
        return self.face_a + self.face_b
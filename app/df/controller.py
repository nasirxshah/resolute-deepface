import os
import pickle

from deepface import DeepFace


def register(identity, img, database):
    embedding = DeepFace.represent(img_path=img)
    if not os.path.exists(database):
        with open(database, "wb") as wf:
            obj = [[identity, embedding[0]["embedding"]]]
            pickle.dump(obj, wf)
    else:
        with open(database, "rb+") as f:
            obj = pickle.load(f)
            obj.append([identity, embedding[0]["embedding"]])
            pickle.dump(obj, f)


def recognise(img, db_path):
    objs = DeepFace.find(img_path=img, db_path=db_path, silent=True)
    identity = objs[0].to_dict()["identity"]
    if identity:
        return identity[0]

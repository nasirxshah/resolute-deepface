import os
import pickle

from deepface import DeepFace


def register(identity, img, db_path):
    embedding = DeepFace.represent(img_path=img)
    if not os.path.exists(db_path):
        with open(db_path, "wb") as wf:
            obj = [[identity, embedding[0]["embedding"]]]
            pickle.dump(obj, wf)
    else:
        with open(db_path, "rb+") as f:
            obj = pickle.load(f)
            obj.append([identity, embedding[0]["embedding"]])
            pickle.dump(obj, f)


def recognise(img, db_path):
    objs = DeepFace.find(img_path=img, db_path=db_path, silent=True)
    identity = objs[0].to_dict()["identity"]
    if identity:
        return identity[0]

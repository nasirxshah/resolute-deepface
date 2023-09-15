import os
import pickle

from deepface import DeepFace


def register(identity, img, database):
    try:
        embeddings = DeepFace.represent(img_path=img)
        if len(embeddings) > 1:
            return {"status": "error", "message": "more than one faces detected"}
        print("#######################",os.path.exists(database))
        
        with open(database, "rb") as rf:
            obj = pickle.load(rf)

        with open(database,"wb") as wf:
            obj.append([identity, embeddings[0]["embedding"]])
            pickle.dump(obj, wf)

        return {"status": "success"}

    except ValueError as e:
        return {"status": "error", "message": str(e)}


def recognise(img, db_path):
    try:
        dfs = DeepFace.find(img_path=img, db_path=db_path, silent=True)
        if len(dfs) > 1:
            return {"status": "error", "message": "more than one faces detected"}

        if dfs[0].empty:
            return {"status":"error","message":"no user found"}

        identity = dfs[0]['identity'][0]

        return {"status":"success","identity":identity}
    except ValueError as e:
        return {"status": "error", "message": str(e)}


from flask import Flask, request, jsonify
from . import models, checksum
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route("/checksum-news/", methods=['POST'])
def create_checksum_news():
    search_keys = request.get_json()
    db_gen = get_db()
    db = next(db_gen)
    result_checksum = checksum.checksum_news(search_keys)
    db_result = models.Result(endpoint="checksum-news", search_key=", ".join(search_keys), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    next(db_gen, None)
    return jsonify({"id": db_result.id, "endpoint": db_result.endpoint, "search_key": db_result.search_key, "checksum": db_result.checksum})

@app.route("/checksum-images-news/", methods=['POST'])
def create_checksum_images():
    search_keys = request.get_json()
    db_gen = get_db()
    db = next(db_gen)
    result_checksum = checksum.checksum_images(search_keys)
    db_result = models.Result(endpoint="checksum-images-news", search_key=", ".join(search_keys), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    next(db_gen, None)
    return jsonify({"id": db_result.id, "endpoint": db_result.endpoint, "search_key": db_result.search_key, "checksum": db_result.checksum})

@app.route("/checksum-files/", methods=['POST'])
def create_checksum_files():
    depth = int(request.args.get('depth'))
    db_gen = get_db()
    db = next(db_gen)
    result_checksum = checksum.checksum_files(depth)
    db_result = models.Result(endpoint="checksum-files", search_key=str(depth), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    next(db_gen, None)
    return jsonify({"id": db_result.id, "endpoint": db_result.endpoint, "search_key": db_result.search_key, "checksum": db_result.checksum})

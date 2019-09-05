import os

import numpy as np
from flask import send_file, abort, jsonify
from sklearn.cluster import KMeans

inputs = {}  # dict: job_id -> file

inputs_r = {}  # dict: file -> job_id

models = {}  # dict: job_id -> model

default_model_params = {'n_clusters': 2, 'random_state': 0}

INPUT_DIR = '/tmp/rest-py-test/input'
os.makedirs(INPUT_DIR, exist_ok=True)

OUTPUT_DIR = '/tmp/rest-py-test/output'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def kmeans_fit(body):
    print(body)

    job_id = body['job_id']

    if job_id not in inputs or not os.path.exists(inputs[job_id]):
        abort(500, "input file missing for job id " + str(job_id))
        return
    in_file = inputs[job_id]

    X = np.genfromtxt(in_file, delimiter=",")  # create the model

    params = dict(default_model_params)
    params.update(body['model_params'])

    kmeans = KMeans(**params).fit(X)

    models.update({job_id: kmeans})  # add the model in to the dict

    labels = OUTPUT_DIR + "/" + str(job_id) + ".labels"
    np.savetxt(labels, kmeans.labels_, delimiter=",")

    return send_file(labels)


def kmeans_predict(body, file=None):
    job_id = int(body['job_id'])

    if job_id in models:
        p_file = OUTPUT_DIR + '/' + str(job_id) + '.p'
        file.save(p_file)

        p = np.genfromtxt(p_file, delimiter=',')  # read the predictions

        result = models[job_id].predict(p)

        print(result)

        res_file = OUTPUT_DIR + "/" + str(job_id) + ".out"
        np.savetxt(res_file, result, delimiter=",")

        return send_file(res_file)

    else:
        abort(500, "model not found for job id " + str(job_id))
        return


def upload_file(file=None):
    filename = file.filename

    in_file = INPUT_DIR + '/' + filename
    if not os.path.exists(in_file):
        file.save(in_file)  # save the input file

    if in_file not in inputs_r:
        job_id = len(inputs)
        inputs.update({job_id: in_file})
        inputs_r.update({in_file: job_id})
    else:
        job_id = inputs_r[in_file]

    return jsonify({'job_id': job_id, 'filename': filename})

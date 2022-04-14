import logging
from flask import Flask, request, Response, jsonify
from parsers import parse_evidence

app = Flask(__name__)


@app.route("/parse", methods=["POST"])
def parse():
    try:
        parser = request.json["parsing_configuration"]
        payload = request.json["payload"]
        table = dict()
        table["evidence_id"] = payload["evidence_id"]
        table["headers"] = list(parser.keys())
        table["rows"] = []
        evidence_data = payload["evidence_data"]
        for data in evidence_data:
            parsed_data = parse_evidence(data, parser)
            table["rows"].append(parsed_data)

        response = jsonify(table)
        response.status_code = 200
        return response
    except:
        app.logger.exception("Parsing error")
        return Response("Parsing error", 501)


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=5000)

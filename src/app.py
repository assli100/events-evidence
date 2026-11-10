import logging
from flask import Flask, request, jsonify
from parsers import parse_evidence, validate_configuration, ConfigurationError

app = Flask(__name__)


def bad_request(message):
    return jsonify({"error": message}), 400


@app.route("/parse", methods=["POST"])
def parse():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return bad_request("request body must be a JSON object")
    try:
        parser = body["parsing_configuration"]
        payload = body["payload"]
        evidence_id = payload["evidence_id"]
        evidence_data = payload["evidence_data"]
    except (KeyError, TypeError) as e:
        return bad_request("missing field: {}".format(e))
    if not isinstance(evidence_data, list):
        return bad_request("payload.evidence_data must be a list")
    try:
        validate_configuration(parser)
    except ConfigurationError as e:
        return bad_request(str(e))

    try:
        table = {
            "evidence_id": evidence_id,
            "headers": list(parser.keys()),
            "rows": [parse_evidence(data, parser) for data in evidence_data],
        }
    except Exception:
        app.logger.exception("Parsing error")
        return jsonify({"error": "parsing error"}), 500

    return jsonify(table), 200


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=5000)

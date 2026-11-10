MISSING = ""


class ConfigurationError(ValueError):
    """Raised when the parsing configuration has the wrong shape."""


def validate_configuration(parser):
    """Check that the configuration is {header: [[key, ...], ...]}."""
    if not isinstance(parser, dict):
        raise ConfigurationError("parsing_configuration must be an object")
    for header, paths in parser.items():
        if not isinstance(paths, list) or not all(isinstance(p, list) for p in paths):
            raise ConfigurationError(
                'value of "{}" must be a list of key lists, e.g. [["user_details", "id"]]'.format(header))


def get_value(data, keys_list):
    """Follow keys_list into data. Returns MISSING if the path doesn't exist."""
    for key in keys_list:
        try:
            data = data[key]
        except (KeyError, IndexError, TypeError):
            return MISSING
    return data


def parse_evidence(data, parser):
    result = {}
    for key, paths in parser.items():
        extracted_values = [get_value(data, keys_list) for keys_list in paths]

        if len(extracted_values) == 1:
            result[key] = extracted_values[0]
        elif len(extracted_values) > 1:
            # combined field, e.g. first name + last name
            result[key] = " ".join(str(v) for v in extracted_values if v != MISSING)
        else:
            result[key] = None

    return result

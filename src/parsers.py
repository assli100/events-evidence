
def get_value(data, keys_list):
    for key in keys_list:
        try:
            data = data[key]
        except KeyError:
            return ""
    return data


def parse_evidence(data, parser):
    result = {}
    for key,value in parser.items():
        # key = str, value = list of lists
        extracted_values = []
        for keys_list in value:
            extracted_values.append(get_value(data, keys_list))

        if len(extracted_values) == 1:
            result[key] = extracted_values[0]
        elif len(extracted_values) > 1:
            result[key] = " ".join(extracted_values)
        else:
            result[key] = None

    return result

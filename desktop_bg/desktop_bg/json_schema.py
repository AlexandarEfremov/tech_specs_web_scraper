import jsonschema
from jsonschema import validate

computer_schema = {
    "type": "object",
    "properties": {
        "processor": {"type": "string"},
        "gpu": {"type": "string"},
        "motherboard": {"type": "string"},
        "ram": {"type": "string"},
    },
    "required": ["processor", "gpu", "motherboard", "ram"]
}


def validate_computer(data):
    try:
        validate(instance=data, schema=computer_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False, err.message
    return True, None

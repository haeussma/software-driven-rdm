from datetime import date, datetime
from pydantic_core import Url


def test_dataset_creation(model_all, model_all_dataset):
    """Tests whether the data that is passed to the model is correctly parsed"""

    expected = {
        "id": "id",
        "str_value": "string",
        "float_value": 1.5,
        "int_value": 1,
        "bool_value": True,
        "date_value": date(2023, 12, 17),
        "datetime_value": datetime(2023, 12, 17, 15, 55, 44, 245441),
        "posfloat_value": 1.5,
        "posint_value": 2,
        "http_url_value": Url("https://www.google.com/"),
        "email_value": "max.mustermann@muster.de",
        "bytes_value": b"this_is_bytes",
        "multiple_primitives": [1.5, 1.7, 1.9],
        "enum_value": "value1",
        "nested_single_obj": {
            "id": "id",
            "str_value": "string",
            "float_value": 1.5,
            "int_value": 1,
        },
        "nested_multiple_obj": [
            {
                "id": "id",
                "str_value": "string",
                "float_value": 1.5,
                "int_value": 1,
            }
        ],
        "referenced_value": "id",
    }

    # Create a dataset with the given library
    nested = model_all.Nested(
        id="id",
        str_value="string",
        float_value=1.5,
        int_value=1,
    )

    dataset = model_all.Root(
        id="id",
        str_value="string",
        float_value=1.5,
        int_value=1,
        bool_value=True,
        date_value=date(2023, 12, 17),
        datetime_value=datetime(2023, 12, 17, 15, 55, 44, 245441),
        posfloat_value=1.5,
        posint_value=2,
        http_url_value="https://www.google.com",
        email_value="max.mustermann@muster.de",
        bytes_value="this_is_bytes".encode(),
        multiple_primitives=[1.5, 1.7, 1.9],
        enum_value=model_all.enums.SomeEnum.VALUE1,
        nested_single_obj=nested,
        nested_multiple_obj=[nested],
        referenced_value=nested,
    )

    assert (
        dataset.to_dict(mode="python") == expected
    ), "Dataset does not match expected values"

# Research Project

## Objects

### Experiment

- title
    - Type: string
    - Description: Title of the experiment.
- measurements
    - Type: Measurement
    - Description: Measurements of the experiment experiment.
    - Multiple: True

### Measurement

- creator
    - Type: Creator
    - Description: Information on the creator of the experiment.
- time_stamp
    - Type: datetime
    - Description: Time point at which the measumrent was performed.
- data
    - Type: float
    - Multiple: True
    - Description: Information on the creator of the experiment.
- data_unit
    - Type: UnitTypes
    - Description: Unit of the measured data.

### Creator

- first_name
    - Type: string
    - Description: First name of the creator.
- last_name
    - Type: string
    - Description: Last name of the creator.
- email_address
    - Type: Email
    - Description: E-mail address of the creator.

## Enums

### UnitTypes

```python
KILOGRAM = "KILOGRAM"
GRAM = "GRAM"
MILLIGRAM = "MILLIGRAM"
MICROGRAM = "MICROGRAM"
NANOGRAM = "NANOGRAM"
```

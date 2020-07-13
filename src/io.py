import pandas as pd
import json


def csv(file_name, table):
    (columns, data) = table
    dataFrame = pd.DataFrame(data=data, columns=columns)
    dataFrame.to_csv(file_name)
    return 'The csv was created successfully!'


def JSON(file_name, table):
    (columns, data) = table
    with open(file_name, 'w') as file:
        json_string = json.dumps(
            [{columns[i]: row[i]
              for i in range(len(columns))} for row in data], default=lambda o: o.__dict__,  indent=2)
        file.write(json_string)
    return 'The JSON was created successfully!'


## TODO: Add some console table styling
def string(table):
    (columns, data) = table
    dataFrame = pd.DataFrame(data=data, columns=columns)
    return dataFrame.to_string()

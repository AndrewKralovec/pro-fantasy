import pandas as pd

## TODO: Add some console table styling
def string(table):
    (columns, data) = table
    dataFrame = pd.DataFrame(data=data, columns=columns)
    return dataFrame.to_string()


def csv(file_name, table):
    (columns, data) = table
    dataFrame = pd.DataFrame(data=data, columns=columns)
    dataFrame.to_csv(file_name)
    return 'The csv was created successfully!'

import pandas as pd


def get_df(path, file_format='json'):
    if file_format == 'json':
        return pd.read_json(path, encoding="cp1251")
    else:
        raise ValueError(f'We are working only with .json file formats, not .{file_format}!')

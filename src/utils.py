import pandas as pd
import numpy as np
import os
from typing import Dict, Any
import json


def get_df(path, file_format='json'):
    if file_format == 'json':
        try:
            return pd.read_json(path, encoding="cp1251")
        except UnicodeDecodeError:
            return pd.read_json(path)
    else:
        raise ValueError(f'We are working only with .json file formats, not .{file_format}!')


def create_empty_column(df, name):
    df[name] = pd.NA


def add_subcategory(df, sub_category_name):
    df['SubCategory'] = sub_category_name


def add_category(df, category_name):
    df['Category'] = category_name


def get_data_folder_info(data_folder, allowed_file_formats=['json', 'xlsx', 'xml']) -> Dict[str, Any]:
    data_folder_info = {}
    for group_name in os.listdir(data_folder):
        group_folder = os.path.join(data_folder, group_name)

        if os.path.isdir(group_folder):

            for file_name in os.listdir(group_folder):
                file_format = file_name.split('.')[-1]

                if file_format in allowed_file_formats:
                    file_path = os.path.join(group_folder, file_name)
                    data_folder_info[group_name] = data_folder_info.get(group_name, [])
                    data_folder_info[group_name].append(file_path)

    return data_folder_info


def get_district_type_name(df):
    def parse(district):
        if isinstance(district, str):
            for district_type in ['поселение', 'район']:
                if district_type in district:
                    district_name = ''.join(district.split(district_type)).strip()
                    return [district_type, district_name]

        else:
            return [None, None]

    district_types_names = list(zip(*df['District'].apply(parse).values))
    df['DistrictType'] = district_types_names[0]
    df['DistrictName'] = district_types_names[1]
    del df['District']


def parse_coordinates(df):
    def parse(row):
        # Словарь
        if type(row['geoData']) == dict:
            geoData = row['geoData']
        # Лист с 2-мя координатами
        elif type(row['geoData']) == list and len(row['geoData']) == 2:
            return row['geoData']
        # Возможно словарь
        elif type(row['geoData']) == str:
            geoData = json.loads(row['geoData'])

        if len(geoData['coordinates']) == 2 and geoData['type'] == 'Point':
            return geoData['coordinates']
        elif geoData['type'] == 'MultiPoint':
            return geoData['coordinates'][0]
        elif geoData['type'] == 'Polygon':
            pass

    geo_data = list(zip(*df[['geoData']].apply(parse, axis=1)))
    df['geoDataLatitude'] = geo_data[1]
    df['geoDataLongitude'] = geo_data[0]
    del df['geoData']

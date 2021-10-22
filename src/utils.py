import pandas as pd
import os
from typing import Dict, Any

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


def add_id(df, id_column='ID', category_column='Category', subcategory_column='SubCategory'):
    df['ID'] = df[category_column].map(str) + '.' + df[subcategory_column].map(str) + '.' + df[id_column].map(str)


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


def get_district(df, in_district_column, out_district_column_name, out_district_column_type):
    allowed_district_types = ['район', 'поселение']
    district_names = []
    district_types = []

    districts_data = df[in_district_column].to_numpy()
    for district_data in districts_data:
        for word in district_data.split():
            if word in allowed_district_types:
                district_types.append(word)


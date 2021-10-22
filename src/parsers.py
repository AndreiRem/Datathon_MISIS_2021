import pandas as pd
import os

from src.utils import (get_df,
                       add_subcategory,
                       add_category,
                       add_id)


def parse_df(data_info, group_name, allowed_file_name, allowed_file_format, rename_columns_method):
    df = None
    file_paths = data_info.get(group_name, [])
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        file_name, file_format = file_name.split('.')

        if file_name == allowed_file_name and file_format == allowed_file_format:
            df = get_df(file_path)
            break

    if df is None:
        raise ValueError(f"There is no '{allowed_file_name}.{allowed_file_format}' in '{group_name}' group!")

    if isinstance(rename_columns_method, dict):
        rename_columns_method = {v: k for k, v in rename_columns_method.items()}
        try:
            df = df[list(rename_columns_method.keys())].rename(columns=rename_columns_method)
        except KeyError:
            exists_rename_columns = set(rename_columns_method.keys()).intersection(set(df.columns))
            non_exists_columns = set(rename_columns_method.keys()).difference(exists_rename_columns)

            exists_rename_columns = {k: v for k, v in rename_columns_method.items() if k in exists_rename_columns}
            non_exists_columns = [v for k, v in rename_columns_method.items()if k in non_exists_columns]

            df = df[list(exists_rename_columns.keys())].rename(columns=exists_rename_columns)
            for column_name in non_exists_columns:
                df[column_name] = None
    else:
        df = rename_columns_method(df, file_name)

    add_category(df, group_name)
    add_subcategory(df, allowed_file_name)
    add_id(df)

    return df.reset_index(drop=True)


def parse_object_address(raw_df, object_address_column='ObjectAddress'):
    def get_object_address(items):
        admareas, districts, address = [], [], []
        for idx, item in enumerate(items):
            df = pd.DataFrame(item)
            adm = list(filter(lambda x: x, df['AdmArea'].unique())) if 'AdmArea' in df.columns else [None]
            dis = list(filter(lambda x: x, df['District'].unique())) if 'District' in df.columns else [None]
            add = list(filter(lambda x: x, df['Address'].unique())) if 'Address' in df.columns else [None]

            if not (adm[0] and dis[0]):
                el = add[0].split(', ')
                dis_temp = list(filter(lambda i: 'район' in item, el))
                add_temp = list(filter(lambda i: not ('область' in item or 'район' in i), el))

                dis[0] = dis_temp[0] if len(dis_temp) else None
                add[0] = ', '.join(add_temp)

            admareas.append(adm[0])
            districts.append(dis[0] if len(dis) else None)
            address.append(add[0])

        return pd.DataFrame({
            'District': districts,
            'Address': address,
            'AdmArea': admareas
        })

    temp_df = get_object_address(raw_df[object_address_column]) ## Получение района, округа и адресса, т.к. каждое мед.учреждение это комплекс зданий
    for column in temp_df.columns:
        raw_df[column] = temp_df[column]

    return raw_df


def parse_sport(raw_df, file_name):
    raw_df = parse_object_address(raw_df, 'ObjectAddress')
    return pd.DataFrame({
        'geoData': raw_df['geodata_center'],
        'Name': raw_df['FullName'],
        'District': raw_df['District'],
        'Address': raw_df['Address'],
        'AdmArea': raw_df['AdmArea'],
        'ID': raw_df['global_id'],
    })


def parse_med(raw_df, file_name):
    def get_df_polyclinic(polyclinic_df):
        temp_df = []
        for idx, item in enumerate(polyclinic_df['properties']):
            df = pd.DataFrame.from_dict(item['Attributes'], orient='index')
            df = df.transpose()
            temp_df.append(df)
        res_df = pd.concat(temp_df, ignore_index=True)
        res_df['geoData'] = polyclinic_df['geometry']

        return res_df

    if file_name == 'Поликлиническая помощь взрослым':
        raw_df = get_df_polyclinic(raw_df)
    raw_df = parse_object_address(raw_df, 'ObjectAddress') ## Получение района, округа и адресса, т.к. каждое мед.учреждение это комплекс зданий
    return pd.DataFrame({
        'geoData': raw_df['geoData'],
        'Name': raw_df['FullName'],
        'District': raw_df['District'],
        'Address': raw_df['Address'],
        'AdmArea': raw_df['AdmArea'],
        'ID': raw_df['global_id'],
    })

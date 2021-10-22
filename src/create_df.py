import pandas as pd
from src.parsers import (parse_df,
                         parse_med,
                         parse_sport)


def create_edu_df(data_info):
    allowed_columns = {'AdmArea': 'AdmArea', 'geodata_center': 'geoData', 'CommonName': 'Name', 'District': 'District',
                       'Address': 'Address', 'global_id': 'ID'}
    universities_df = parse_df(data_info, 'Образование', 'Вузы', 'json', allowed_columns)

    allowed_columns = {'AdmArea': 'AdmArea', 'geodata_center': 'geoData', 'ShortName': 'Name', 'District': 'District',
                       'LegalAddress': 'Address', 'global_id': 'ID'}
    school_df = parse_df(data_info, 'Образование', 'Образовательные учреждения', 'json', allowed_columns)

    edu_df = pd.concat((universities_df, school_df), ignore_index=True)

    return edu_df


def create_med_df(data_info):
    med1_df = parse_df(data_info, 'Медицина', 'Больницы взрослые', 'json', parse_med)
    med2_df = parse_df(data_info, 'Медицина', 'Больницы детские и специализированные', 'json', parse_med)
    med3_df = parse_df(data_info, 'Медицина', 'Поликлиническая помощь взрослым', 'json', parse_med)
    med_df = pd.concat((med1_df, med2_df, med3_df), ignore_index=True)

    return med_df


def create_sport_df(data_info):
    sport_df = parse_df(data_info, 'Спорт', 'Спортивные объекты Москвы', 'json', parse_sport)

    return sport_df

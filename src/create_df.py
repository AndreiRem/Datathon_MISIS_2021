import pandas as pd
from src.parsers import (parse_df,
                         parse_med,
                         parse_sport)


def create_edu_df(data_info):
    allowed_columns = {'ID': 'global_id',
                       'Name': 'CommonName',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    universities_df = parse_df(data_info, 'Образование', 'Вузы', 'json', allowed_columns)

    allowed_columns = {'ID': 'global_id',
                       'Name': 'ShortName',
                       'Address': 'LegalAddress',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
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


def create_religion_df(data_info):
    allowed_columns = {'ID': 'global_id',
                       'Name': 'ObjectName',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    catholics_df = parse_df(data_info, 'Религия', 'Католические храмы', 'json', allowed_columns)

    allowed_columns = {'ID': 'global_id',
                       'Name': 'ObjectName',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    mosques_df = parse_df(data_info, 'Религия', 'Мечети', 'json', allowed_columns)

    allowed_columns = {'ID': 'global_id',
                       'Name': 'NameOfReligiousOrganization',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    monasteries_df = parse_df(data_info, 'Религия', 'Монастыри', 'json', allowed_columns)

    allowed_columns = {'ID': 'global_id',
                       'Name': 'Name',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    rpc_df = parse_df(data_info, 'Религия', 'Религиозные объекты РПЦ', 'json', allowed_columns)

    allowed_columns = {'ID': 'global_id',
                       'Name': 'ObjectName',
                       'Address': 'Address',
                       'AdmArea': 'AdmArea',
                       'District': 'District',
                       'geoData': 'geodata_center'}
    synagogues_df = parse_df(data_info, 'Религия', 'Синагоги', 'json', allowed_columns)

    religion_df = pd.concat((catholics_df, mosques_df, monasteries_df, rpc_df, synagogues_df), ignore_index=True)

    return religion_df

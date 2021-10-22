import pandas as pd
import os

from src.utils import get_data_folder_info, parse_coordinates, get_district_type_name, set_types
from src.create_df import (create_edu_df,
                           create_med_df,
                           create_sport_df,
                           create_religion_df,
                           create_transport_df,
                           create_service_df,
                           create_animals_df,
                           create_culture_df,
                           create_entertainment_df)

ROOT_FOLDER = '../'
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_INFO = get_data_folder_info(DATA_FOLDER)

edu_df = create_edu_df(DATA_INFO)
med_df = create_med_df(DATA_INFO)
sport_df = create_sport_df(DATA_INFO)
religion_df = create_religion_df(DATA_INFO)
transport_df = create_transport_df(DATA_INFO)
service_df = create_service_df(DATA_INFO)
animals_df = create_animals_df(DATA_INFO)
culture_df = create_culture_df(DATA_INFO)
entertainment_df = create_entertainment_df(DATA_INFO)

res_df = pd.concat((edu_df,
                    med_df,
                    sport_df,
                    religion_df,
                    transport_df,
                    service_df,
                    animals_df,
                    culture_df), ignore_index=True)

parse_coordinates(res_df)
get_district_type_name(res_df)
set_types(res_df)

res_df.to_csv(os.path.join(ROOT_FOLDER, 'dataset.csv'), index=False)

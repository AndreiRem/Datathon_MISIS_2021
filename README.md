# datathon2021
Данный датасет собран для соревнования Дататон 2021 от команды "Team Meldonium".

## Цели создания
Проект преследует цель агрегирования данных по разным общественным местам, привязанным к районам или иным геометкам на карте г. Москвы. Таким образом одновременно решается сразу несколько задач, в том числе:

### Цель 1
Создание выборки районов, где потенциальные жильцы смогут оценить наличие необходимых им объектов благоустройства. Типы объектов при этом определяются возрастом, социальной группой и иными факторами, поэтому могут отличаться для каждого пользователя датасета.

### Цель 2
Общая оценка благосостояния различных районов г. Москвы для привлечения внимания администрации города, стимулируя развитие отстающих районов.

### Цель 3
Оценка спроса на услуги коммерческих организаций, предоставляющих услуги в области образования, медицины, т.д.

## Используемые данные

| Категория  | Тип объекта  | Количество | Ссылка  |
| :------------| :------------ |:---------------:| :-----|
| Образование      | Университеты      | 295 | https://data.mos.ru/opendata/7710878000-obrazovatelnye-organizatsii-vysshego-obrazovaniya-osushchestvlyayushchie-deyatelnost-na-territorii-goroda-moskvy-i-predostavlyayushchie-pravo-na-besplatnoe-oformlenie-sotsialnoy-karty |
| Образование      | Школы_1      | 590 | https://data.mos.ru/opendata/7719028495-obrazovatelnye-uchrejdeniya-goroda-moskvy |
| Образование      | Школы_2      | 149 | https://data.mos.ru/opendata/7719028495-perechen-negosudarstvennyh-doshkolnyh-obrazovatelnyh-organizatsiy-goroda-moskvy |
| Образование      | Детские сады      | WIP | https://data.mos.ru/opendata/detskie-sady |
| Медицина      | Взрослые больницы      | 44        |   https://data.mos.ru/opendata/7707089084-bolnitsy-vzroslye |
| Медицина      | Детские и спец. больницы      | 16        |   https://data.mos.ru/opendata/7707089084-bolnitsy-detskie |
| Медицина      | Поликлиники      | 276        |   https://data.mos.ru/opendata/7707089084-poliklinicheskaya-pomoshch-vzroslym |
| Транспорт | Вестибюли метро | 1020        |    https://data.mos.ru/opendata/7704786030-vhody-i-vyhody-vestibyuley-stantsiy-moskovskogo-metropolitena |
| Транспорт | Остановки наземное общественного транспорта | 12197        |    https://data.mos.ru/opendata/7704786030-marshruty-i-ostanovki-nazemnogo-gorodskogo-passajirskogo-transporta-ostanovki |
| Культура | Объекты культурного наследия | 8330        |    https://data.mos.ru/opendata/7705021556-obekty-kulturnogo-naslediya-i-vyyavlennye-obekty-kulturnogo-naslediya |
| Культура | Учреждения культуры | 1834       |    https://data.mos.ru/opendata/7702155262-interaktivnaya-karta-uchrejdeniy-kultury-goroda-moskvy |
| Спорт| Спортивные объекты | 320        |    https://data.mos.ru/opendata/7708308010-sportivnye-obekty-goroda-moskvy |
| Религия | Православие | 551        |    https://data.mos.ru/opendata/7704253498-religioznye-obekty-russkoy-pravoslavnoy-tserkvi |
| Религия | Католицизм | 3        |    https://data.mos.ru/opendata/7704253498-katolicheskie-hramy |
| Религия | Ислам | 4        |    https://data.mos.ru/opendata/7704253498-mecheti |
| Религия | Синагоги | 5        |    https://data.mos.ru/opendata/7704253498-sinagogi |
| Торговля | Стационарные торговые объекты | 42586        |    https://data.mos.ru/opendata/7710881420-statsionarnye-torgovye-obekty |
| Торговля | Бытовые услуги | 12579        |    https://data.mos.ru/opendata/7710881420-bytovye-uslugi-na-territorii-moskvy |
| Торговля | Общественное питание | 17454        |    https://data.mos.ru/opendata/7710881420-obshchestvennoe-pitanie-v-moskve |
| Досуг | Парковые зоны | 1134        |    https://data.mos.ru/opendata/7710878000-parkovye-territorii |
| Животные | Площадки выгула собак | 505        |    https://data.mos.ru/opendata/7710878000-ploshchadki-dlya-vygula-dressirovki-sobak |

## Принцип конкатенации

1. Обновление геоданных по шаблону.
2. Создание классификации по типу объекта.
3. Последовательное соединение отформатированных.

## Пример финального датасета

| ID  | geoData  | Name | AdmArea  | District | Address | Category
| :------------| :------------ |:---------------| :-----| :-----| :-----| :-----|
| 1	| [37.758028, 55.698198] | Храм Елисаветы прмц. при школе-интернате № 55 | Юго-Восточный административный округ | район Кузьминки | улица Маршала Чуйкова, дом 26, строение 1 | Религия |
| 2	| [37.51639, 55.805098] | "Сокол, вход-выход 3 в восточный вестибюль" | Северный административный округ | район Аэропорт | NaN | Транспорт |
| 3 | [37.4178186288665, 55.7075930211458] | "Могила Филина Федота Петровича, (1908-1982 гг.), филолога, языковеда, член-корреспондента АН СССР" | Западный административный округ | Можайский район | "город Москва, Рябиновая улица, дом 16; ЗАО, муниципальный округ Можайский, Рябиновая ул., д., 16 (Новокунцевское кладбище, уч.10)" | Культура | 
| 4 | [37.4025436329438, 55.8474402107015] | "- Овощехранилище, 1-я пол. XIX в." | Северо-Западный административный округ | район Южное Тушино | "город Москва, Светлогорский проезд, дом 13, строение 1" | Культура |
| 5 | [37.764851, 55.631513] | Храм Троицы Живоначальной в Братееве | Южный административный округ | район Братеево | "Ключевая улица, дом 5" | Религия |


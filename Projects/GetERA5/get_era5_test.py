#!/usr/bin/env python3.7
#---------------------------------------------------------------------------
# Please check the version of Python in which cdsapi is installed 
# by following the command:
#
#> pip show cdsapi
# * check "pythonX.X" written in "Location: /usr/lib/pythonX.X/site-packages"
#
# Executable command (if pythonX.X = python3.7)
#> python3.7 get_era5_atm.py
#---------------------------------------------------------------------------
import os
import cdsapi
#
# Geographical and Grid parameters --------
#
#                 ______ (Rlon,Tlat)
#                |      |
#                |      |
#                |______|
#     (Llon,Blat)                     
#
Llon = 118    # Longitude (degrees) of the bottom-left corner of the grid. 
Rlon = 127    # Longitude (degrees) of the top-right corner of the grid. 
Blat = 9      # Latitude  (degrees) of the bottom-left corner of the grid.
Tlat = 15     # Latitude  (degrees) of the top-right corner of the grid.

Year='2019'

OUTPUT_DIR = '../../Data/era5/Panay'

FILE_NAME_prefix='era5_wave'

#---------------------------------------------------------------------------
if not os.path.isdir(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

FILE_NAME = OUTPUT_DIR + '/' + FILE_NAME_prefix + '_' + Year + '.nc'

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            'mean_wave_direction', 
            'mean_wave_period', 
            'significant_height_of_combined_wind_waves_and_swell',
        ],
        'year': Year,
        'month': [
            '01',        
        ],
        'day': [
            '01',        
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            Tlat,  Llon,
            Blat,  Rlon,
        ],
        'format': 'netcdf',
    },
    FILE_NAME )
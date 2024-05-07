

import geopandas as gpd 
import numpy as np
from osgeo import gdal 

# SUBSET AND REPROJ GPKG
input_shape = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3.gpkg" 
output_shape = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
iso_gdf = gpd.read_file(input_shape)
gha_gdf = iso_gdf[iso_gdf['iso3']=='GHA']
gha_gdf = gha_gdf.to_crs('ESRI:54030')
gha_gdf.to_file(output_shape, driver='GPKG')

# CLIP ESACCI TO GHANA
input_raster = "/Users/mbraaksma/Files/base_data/lulc/esa/lulc_esa_2017.tif" 
mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
output_raster="/Users/mbraaksma/Files/base_data/lulc/esa/lulc_esa_2017_ghana.tif" 
gdal.Warp(output_raster, input_raster, dstSRS='ESRI:54030',
            cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)


from osgeo import gdal 

# REPROJ SEALS
scenario_list = ['ssp1_rcp26', 'ssp2_rcp45','ssp5_rcp85']
year_list = [2030, 2035, 2040]
seals_lulc_path = '/Users/mbraaksma/Files/seals/projects/ghana_policy_forest/intermediate/stitched_lulc_simplified_scenarios/'

for scenario in scenario_list:
    for year in year_list:
        input_raster = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
        output_raster= seals_lulc_path + f'reprojected/lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
        gdal.Warp(output_raster, input_raster, dstSRS='ESRI:54030')

# REPROJ/CLIP ANNUAL WATER YIELD TIFFS
# average annual precipitation
mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/baseline_bio12_Annual_Precipitation.tif', 
          '/Users/mbraaksma/Files/base_data/mesh/worldclim/baseline/5min/baseline_bio12_Annual_Precipitation.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)
# evapotranspiration
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/pet.tif', 
          '/Users/mbraaksma/Files/base_data/mesh/cgiar_csi/pet.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)
# root restricting layer depth
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/depth_to_root_restricting_layer.tif', 
          '/Users/mbraaksma/Files/base_data/mesh/isric/depth_to_root_restricting_layer.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)
# plant available water content
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/pawc_30s.tif', 
          '/Users/mbraaksma/Files/base_data/mesh/soil/pawc_30s.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)
# watersheds
input_shape = "/Users/mbraaksma/Files/base_data/mesh/hydrosheds/hydrobasins/hybas_af_lev01-06_v1c/hybas_af_lev06_v1c.shp" 
output_shape = "/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/hybas_af_lev06_v1c.gpkg" 
ws_gdf = gpd.read_file(input_shape)
ws_gdf = ws_gdf.to_crs('ESRI:54030')
ws_gdf.rename(columns={'HYBAS_ID':'ws_id'}, inplace=True)
ws_gdf.to_file(output_shape, driver='GPKG')


# NDR TIFFS 
# DEM
mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/nutrient_delivery/alt_m.tif', 
          '/Users/mbraaksma/Files/base_data/seals/static_regressors/alt_m.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)


# SDR TIFFS 
# Erosivity
mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/GlobalR_NoPol-002.tif', 
          '/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/Global Erosivity/GlobalR_NoPol-002.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)
# Soil Erodibility
mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
gdal.Warp('/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/RUSLE_KFactor_v1.1_25km.tif', 
          '/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/Global Soil Erodibility/Data_25km/RUSLE_KFactor_v1.1_25km.tif', 
          dstSRS='ESRI:54030',
          cutlineDSName=mask_vector_path, cropToCutline=True, dstNodata=np.nan)





# import pygeoprocessing as pygeo

# input_raster = "/Users/mbraaksma/Files/base_data/lulc/esa/lulc_esa_2017.tif" 
# mask_vector_path = "/Users/mbraaksma/Files/base_data/pyramids/countries_iso3_ghana.gpkg" 
# output_raster="/Users/mbraaksma/Files/base_data/lulc/esa/lulc_esa_2017_ghana.tif" 

# gdal.Warp(output_raster, input_raster, dstSRS='ESRI:54030')
# pygeo.warp_raster(base_raster_path=input_raster,
#                     target_pixel_size=pygeo.get_raster_info(input_raster)['pixel_size'],
#                     target_raster_path=output_raster, 
#                     resample_method='near', 
#                     target_bb=pygeo.get_vector_info(mask_vector_path)['bounding_box'], 
#                     base_projection_wkt=None, 
#                     target_projection_wkt='ESRI:54030', 
#                     n_threads=None, 
#                     vector_mask_options={'mask_vector_path': mask_vector_path}, 
#                     gdal_warp_options=None, 
#                     working_dir=None, 
#                     use_overview_level=-1, 
#                     raster_driver_creation_tuple=('GTIFF', ('TILED=YES', 'BIGTIFF=YES', 'COMPRESS=LZW', 'BLOCKXSIZE=256', 'BLOCKYSIZE=256')), 
#                     osr_axis_mapping_strategy=0)



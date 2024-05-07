# Plot the raster for output from InVEST Model 

# Dependencies
# import os 
# from osgeo import gdal 
import os
import pygeoprocessing as pygeo
import matplotlib.pyplot as plt 

# # Reused content
# scenario_list = ['ssp1', 'ssp5']
# year_list = [2030, 2035, 2045]
# output_path = os.path('C:\Users\ryanm\Dropbox (Personal)\Files\apec_8601\env8601_project\invest')

# ## Model Output: Carbon 
# for scenario in scenario_list:
#     for year in year_list:
#         output_file = os.path(output_path + f'carbon-{scenario}-{year}\tot_c_cur.tif')
#         img = np.dstack((b1, b2, b3)) 
#         f = plt.figure() 
#         plt.imshow(img) 
#         plt.savefig(os.path(output_path + f'carbon-{scenario}-{year}\tot_c_cur.png') )
                    

if __name__ == '__main__':
    # Run scenarios
    scenario_list = ['ssp1_rcp26', 'ssp2_rcp45','ssp5_rcp85']
    year_list = [2030, 2035, 2040]
    invest_output_path = '/Users/mbraaksma/Files/apec8601_project/apec8601_project/invest_output'
    plots_path = '/Users/mbraaksma/Files/apec8601_project/apec8601_project/plots'


    for scenario in scenario_list:
        for year in year_list:
            # CARBON
            raster_path = os.path.join(invest_output_path, f'carbon/{scenario}_{year}/tot_c_cur.tif')
            png_path = os.path.join(plots_path, f'carbon/{scenario}_{year}_tot_c_cur.png')
            raster_array = pygeo.raster_to_numpy_array(raster_path)
            plt.imshow(raster_array)
            cbar = plt.colorbar(orientation='vertical')
            cbar.set_label('metric tons')
            plt.axis('off')
            plt.savefig(png_path, format="png")
            plt.close()

            # POLLINATION
            raster_path = os.path.join(invest_output_path, f'pollination/{scenario}_{year}/total_pollinator_abundance_spring.tif')
            png_path = os.path.join(plots_path, f'pollination/{scenario}_{year}_total_pollinator_abundance_spring.png')
            raster_array = pygeo.raster_to_numpy_array(raster_path)
            plt.imshow(raster_array)
            cbar = plt.colorbar(orientation='vertical')
            cbar.set_label('total pollinator abundance across all species per season')
            plt.axis('off')
            plt.savefig(png_path, format="png")
            plt.close()

            # ANNUAL WATER YIELD 
            raster_path = os.path.join(invest_output_path, f'annual_water_yield/{scenario}_{year}/output/per_pixel/wyield.tif')
            png_path = os.path.join(plots_path, f'annual_water_yield/{scenario}_{year}_wyield.png')
            raster_array = pygeo.raster_to_numpy_array(raster_path)
            plt.imshow(raster_array)
            cbar = plt.colorbar(orientation='vertical')
            cbar.set_label('mm')
            plt.axis('off')
            plt.savefig(png_path, format="png")
            plt.close()

            # NDR
            raster_path = os.path.join(invest_output_path, f'nutrient_delivery/{scenario}_{year}/p_surface_export.tif')
            png_path = os.path.join(plots_path, f'nutrient_delivery/{scenario}_{year}_p_surface_export.png')
            raster_array = pygeo.raster_to_numpy_array(raster_path)
            plt.imshow(raster_array)
            cbar = plt.colorbar(orientation='vertical')
            cbar.set_label('kg/year')
            plt.axis('off')
            plt.savefig(png_path, format="png")
            plt.close()

            # SDR
            raster_path = os.path.join(invest_output_path, f'sediment_delivery/{scenario}_{year}/avoided_export.tif')
            png_path = os.path.join(plots_path, f'sediment_delivery/{scenario}_{year}_avoided_export.png')
            raster_array = pygeo.raster_to_numpy_array(raster_path)
            plt.imshow(raster_array)
            cbar = plt.colorbar(orientation='vertical')
            cbar.set_label('tons')
            plt.axis('off')
            plt.savefig(png_path, format="png")
            plt.close()



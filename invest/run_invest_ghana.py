
import logging
import sys
import os

import natcap.invest.carbon
import natcap.invest.pollination
import natcap.invest.annual_water_yield
import natcap.invest.ndr.ndr
import natcap.invest.sdr.sdr
import natcap.invest.utils

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])


args_carbon = {
    'calc_sequestration': False,
    'carbon_pools_path': '/Users/mbraaksma/Files/base_data/global_invest/carbon/seals_biophysical_table.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': '',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': '',
}

pollination_args = {
    'farm_vector_path': '',
    'guild_table_path': '/Users/mbraaksma/Files/base_data/global_invest/pollination/guild_table.csv',
    'landcover_biophysical_table_path': '/Users/mbraaksma/Files/base_data/global_invest/pollination/landcover_biophysical_table.csv',
    'landcover_raster_path': '',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': '',
}

water_args = {
    'biophysical_table_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/biophysical_table_gura.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/depth_to_root_restricting_layer.tif',
    'eto_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/pet.tif',
    'lulc_path': '',
    'n_workers': '-1',
    'pawc_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/pawc_30s.tif',
    'precipitation_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/baseline_bio12_Annual_Precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/hybas_af_lev06_v1c.gpkg',
    'workspace_dir': '',
}

ndr_args = {
    'biophysical_table_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/biophysical_table_gura.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': '/Users/mbraaksma/Files/base_data/global_invest/nutrient_delivery/alt_m.tif',
    'k_param': '2',
    'lulc_path': '',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/baseline_bio12_Annual_Precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/hybas_af_lev06_v1c.gpkg',
    'workspace_dir': '',
}

sdr_args = {
    'biophysical_table_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/biophysical_table_gura.csv',
    'dem_path': '/Users/mbraaksma/Files/base_data/global_invest/nutrient_delivery/alt_m.tif',
    'drainage_path': '',
    'erodibility_path': '/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/RUSLE_KFactor_v1.1_25km.tif',
    'erosivity_path': '/Users/mbraaksma/Files/base_data/global_invest/sediment_delivery/GlobalR_NoPol-002.tif',
    'ic_0_param': '0.5',
    'k_param': '2',
    'l_max': '122',
    'lulc_path': '',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': '/Users/mbraaksma/Files/base_data/global_invest/annual_water_yield/hybas_af_lev06_v1c.gpkg',
    'workspace_dir': '',
}

if __name__ == '__main__':
    # Run scenarios
    scenario_list = ['ssp1_rcp26', 'ssp2_rcp45','ssp5_rcp85']
    year_list = [2030, 2035, 2040]
    seals_lulc_path = '/Users/mbraaksma/Files/seals/projects/ghana_policy_forest/intermediate/stitched_lulc_simplified_scenarios/reprojected/'
    base_data_path = '/Users/mbraaksma/Files/base_data/invest_ghana/'

    for scenario in scenario_list:
        for year in year_list:
            # CARBON
            output_dir = base_data_path + f'carbon/{scenario}_{year}'
            os.makedirs(output_dir, exist_ok=True)
            args_carbon['workspace_dir'] = output_dir
            args_carbon['lulc_cur_path'] = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
            natcap.invest.carbon.execute(args_carbon)

            # POLLINATION
            output_dir = base_data_path + f'pollination/{scenario}_{year}'
            os.makedirs(output_dir, exist_ok=True)
            pollination_args['workspace_dir'] = output_dir
            pollination_args['landcover_raster_path'] = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
            natcap.invest.pollination.execute(pollination_args)

            # ANNUAL WATER YIELD
            output_dir = base_data_path + f'annual_water_yield/{scenario}_{year}'
            os.makedirs(output_dir, exist_ok=True)
            water_args['workspace_dir'] = output_dir
            water_args['lulc_path'] = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
            natcap.invest.annual_water_yield.execute(water_args)

            # NDR: PHOSPHORUS
            output_dir = base_data_path + f'nutrient_delivery/{scenario}_{year}'
            os.makedirs(output_dir, exist_ok=True)
            ndr_args['workspace_dir'] = output_dir
            ndr_args['lulc_path'] = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
            natcap.invest.ndr.ndr.execute(ndr_args)

            # SDR
            output_dir = base_data_path + f'sediment_delivery/{scenario}_{year}'
            os.makedirs(output_dir, exist_ok=True)
            sdr_args['workspace_dir'] = output_dir
            sdr_args['lulc_path'] = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
            natcap.invest.sdr.sdr.execute(sdr_args)


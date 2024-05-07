import os
import pygeoprocessing as pygeo
import matplotlib.pyplot as plt 


def generate_plot(policy):
    # Calculate the number of scenarios and years
    scenario_list = ['ssp1_rcp26', 'ssp2_rcp45', 'ssp5_rcp85']
    year_list = [2030, 2035, 2040]
    seals_output_path = f'/Users/mbraaksma/Files/seals/projects/{policy}/intermediate/stitched_lulc_simplified_scenarios'
    plots_path = '/Users/mbraaksma/Files/apec8601_project/apec8601_project/plots/'

    num_scenarios = len(scenario_list)
    num_years = len(year_list)

    # Create a figure and axes for the grid
    fig, axes = plt.subplots(num_years, num_scenarios, figsize=(12, 12), sharex=True, sharey=True)

    # Loop through each scenario and year
    for i, year in enumerate(year_list):
        for j, scenario in enumerate(scenario_list):
            # 
            raster_path = os.path.join(seals_output_path, f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif')
            raster_array = pygeo.raster_to_numpy_array(raster_path)

            # Plot the raster in the appropriate subplot
            im = axes[i, j].imshow(raster_array)
            # axes[i, j].axis('off')
            axes[i, j].tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)

    for ax, col in zip(axes[0, :], scenario_list):
        ax.set_title(col, size=14)
    for ax, row in zip(axes[:, 0], year_list):
        ax.set_ylabel(row, size=14)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Create a colorbar
    cbar_ax = fig.add_axes([0.92, 0.1, 0.02, 0.8])  # [left, bottom, width, height]
    cbar = fig.colorbar(im, cax=cbar_ax, orientation='vertical')
    # cbar.set_label(unit)

    # Save the combined plot
    combined_png_path = os.path.join(plots_path, policy+'.png')
    print(combined_png_path)
    plt.savefig(combined_png_path, format="png")


if __name__ == '__main__':

    generate_plot(policy='ghana_policy_forest')
    # generate_plot(policy='ghana_standard')



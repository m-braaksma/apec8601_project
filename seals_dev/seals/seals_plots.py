
import os
import pygeoprocessing as pygeo
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap


def generate_plot(policy):
    # Calculate the number of scenarios and years
    scenario_list = ['ssp1_rcp26', 'ssp2_rcp45', 'ssp5_rcp85']
    year_list = [2030, 2035, 2040]
    seals_output_path = f'/Users/mbraaksma/Files/seals/projects/{policy}/intermediate/stitched_lulc_simplified_scenarios'
    plots_path = '/Users/mbraaksma/Files/apec8601_project/apec8601_project/plots/'

    num_scenarios = len(scenario_list)
    num_years = len(year_list)

    # Create a figure and axes for the grid
    fig, axes = plt.subplots(num_years, num_scenarios, figsize=(14, 14), sharex=True, sharey=True)

    # Define discrete colormap with distinct colors for each category
    cmap = ListedColormap(['red', 'orange', 'springgreen', 'darkgreen', 'yellow', 'tab:blue', 'white'])

    # Loop through each scenario and year
    for i, year in enumerate(year_list):
        for j, scenario in enumerate(scenario_list):
            # Load raster data
            raster_path = os.path.join(seals_output_path, f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}.tif')
            raster_array = pygeo.raster_to_numpy_array(raster_path)

            # Plot the raster in the appropriate subplot
            im = axes[i, j].imshow(raster_array, cmap=cmap)
            axes[i, j].tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)

    # Define legend labels
    legend_labels = {1: 'Urban', 2: 'Cropland', 3: 'Grassland', 4: 'Forest', 5: 'Othernat', 6: 'Water', 7: 'Other'}

    # Create legend patches with correct colors from the colormap
    legend_patches = [mpatches.Patch(color=cmap(i-1), label=label) for i, label in legend_labels.items()]

    # Add legend
    fig.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5), facecolor="white")

    for ax, col in zip(axes[0, :], scenario_list):
        ax.set_title(col, size=14)
    for ax, row in zip(axes[:, 0], year_list):
        ax.set_ylabel(row, size=14)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the combined plot
    combined_png_path = os.path.join(plots_path, policy+'.png')
    print(combined_png_path)
    plt.savefig(combined_png_path, format="png", bbox_inches='tight')  # Adjusted to include legend
    plt.close()

if __name__ == '__main__':

    # PLOT SCENARIOS
    generate_plot(policy='ghana_policy_forest')
    generate_plot(policy='ghana_standard')

    # PLOT BASELINE
    # raster_path = '/Users/mbraaksma/Files/base_data/lulc/esa/lulc_esa_2017_ghana.tif'
    # png_path = '/Users/mbraaksma/Files/apec8601_project/apec8601_project/plots/baseline.png'
    # raster_array = pygeo.raster_to_numpy_array(raster_path)
    # cmap = ListedColormap(['red', 'orange', 'springgreen', 'darkgreen', 'yellow', 'tab:blue', 'white'])
    # plt.imshow(raster_array, cmap=cmap)
    # plt.axis('off')
    # legend_labels = {1: 'Urban', 2: 'Cropland', 3: 'Grassland', 4: 'Forest', 5: 'Othernat', 6: 'Water', 7: 'Other'}
    # legend_patches = [mpatches.Patch(color=cmap(i-1), label=label) for i, label in legend_labels.items()]
    # plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5), facecolor="white")

    # print(png_path)
    # plt.savefig(png_path, format="png", bbox_inches='tight')  # Adjusted to include legend



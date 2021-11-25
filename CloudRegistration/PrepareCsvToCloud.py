import pandas as pd
import numpy as np
import os


def separate_csv_cloud_frames(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    csv_header = ['Timestamp', 'X', 'Y', 'Z']
    pcl_data = pd.read_csv(input_file, usecols=csv_header).to_numpy()
    pcl_data = pcl_data[np.any(pcl_data[:, 1:], axis=1)]
    time_stamps = np.unique(pcl_data[:, 1])

    for time in time_stamps:
        pd.DataFrame(pcl_data[pcl_data[:, 1] == time], columns=csv_header).to_csv(
            os.path.join(output_dir, f'{time}.csv'))

    print('')


if __name__ == '__main__':
    in_file = r'C:\dev\hackaton\3d-files\csv\gerstenfall1.csv'
    out_folder = r'C:\dev\hackaton\3d-files\csv\out'
    separate_csv_cloud_frames(in_file, out_folder)

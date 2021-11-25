import pandas as pd
import numpy as np
import os


def separate_csv_cloud_frames(input_file, output_dir, start):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    csv_header = ['Timestamp', 'X', 'Y', 'Z']
    pcl_data = pd.read_csv(input_file, usecols=csv_header).to_numpy()
    pcl_data = pcl_data[np.any(pcl_data[:, 1:], axis=1)]
    len_data = len(pcl_data[:, 1])
    sec_frames = int(len_data / 15)
    for i in range(int((len_data / sec_frames) - 1)):
        pd.DataFrame(pcl_data[i * sec_frames:(i + 1) * sec_frames], columns=csv_header).to_csv(
            os.path.join(output_dir, f'{start + i}.csv'))

    print('')


if __name__ == '__main__':
    in_file = r'C:\dev\hackaton\3d-files\csv\gerstenfall3.csv'
    out_folder = r'C:\dev\hackaton\3d-files\Frames'
    separate_csv_cloud_frames(in_file, out_folder, 28)

import copy

import open3d as o3d
import numpy as np


def draw_registration_result(source, target, transformation, zoom=1,
                             front=[1, 0, 0],
                             lookat=[1, 0, 0],
                             up=[0, 0, 1]):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


def read_pcl_file(source, target):
    threshold = 0.02
    trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                             [-0.139, 0.967, -0.215, 0.7],
                             [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])
    draw_registration_result(source, target, trans_init)


if __name__ == '__main__':
    target = o3d.io.read_point_cloud(r"C:\dev\hackaton\3d-files\2las.las", format='las')
    source = o3d.io.read_point_cloud(r"C:\dev\hackaton\3d-files\1las.las", format='las')

    read_pcl_file(source, target)

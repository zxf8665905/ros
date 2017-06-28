import os
import numpy as np
# import cv2
import sys
import time

sys.path.append(os.path.join(sys.path[0],"../../detector/MV3D/src"))
sys.path.append(os.path.join(sys.path[0],"../../detector/scripts"))

#from config import cfg
#import mv3d
#import py2utils

# global predict
# global front

# def init():
#     global predict
#     global front
#
#     tag = "v0.2.1"
#     print("init the network ", tag)
#     LIDAR_TOP_SHAPE = (500, 300, 15) # to be decided (400, 400, 8)
#     LIDAR_FRONT_SHAPE = (0,)  # to be decided.
#     RGB_SHAPE = (596, 1368, 3)  # to be decided (1096, 1368, 3)
#
#     # predict = mv3d.Predictor(LIDAR_TOP_SHAPE, LIDAR_FRONT_SHAPE, RGB_SHAPE, log_tag=tag)
#     front = np.zeros((0,), dtype=np.float32)
#
# def testCase():
#     global predict
#     global front
#
#     print("testing predict:")
#     dir = os.path.join(cfg.RAW_DATA_SETS_DIR, "suburu_driving_past_it/suburu07")
#     rgb_path = os.path.join(dir, "image_02/data", "1492888603962510690.png")
#     print(rgb_path)
#     rgb = py2utils.crop_image(cv2.imread(rgb_path))
#     print(rgb.shape)
#     lidar_path = os.path.join(dir, "velodyne_points/data", "1492888603962510690.bin")
#     lidar =np.fromfile(lidar_path, np.float32)
#     lidar = lidar.reshape((-1, 4))
#     top = py2utils.g_lidar_to_top(lidar)
#
#     start = time.time()
#     boxes3d, probs = predict([top], [front], [rgb])
#     timestamp = time.time()-start
#     print("predict boxes len=%d use %f seconds" % (len(boxes3d),timestamp))

def predict(top : np.array, rgb : np.array):
    #start = time.time()
    # boxes3d, probs = predict([top], [front], [rgb])
    # print("predict boxes len: {} use time {}".format(boxes3d.shape[0], time.time() - start))
    # return boxes3d.tolist()
    print("call python predict")
    print(top.shape)
    print(rgb.shape)

    print("-------------")
    print(top)
    #print(rgb)

def func(_a, _b, _c):
    print(_a.shape)
    print(_b.shape)
    print(_c.shape)
    print("=============func================")
    x = _b * _a.T
    _d = np.zeros(_c.shape)
    _d[:, :, 0] = _b
    _d[:, :, 1] = -_b
    y = _c ** _d
    print("y.shape : ")
    print(y.shape)
    print(y)
    return _c ** _d

#init()
#testCase()
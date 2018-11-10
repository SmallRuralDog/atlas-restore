# coding=utf-8
import json
import os
import sys
import shutil
from PIL import Image

try:
    name = sys.argv[1]
    atlas = open(name, 'r')
    data = json.loads(atlas.read())
    image_name = data['meta']['image']
    path = data['meta']['prefix']
    print image_name
    print path
    # 删除文件夹
    shutil.rmtree(path)
    # 创建文件夹
    os.makedirs(path)
    # 加载图片
    im = Image.open(image_name)
    frames = data['frames']
    for frame in frames:
        frame_info = frames[frame]
        x = frame_info['frame']['x']
        y = frame_info['frame']['y']
        w = frame_info['frame']['w']
        h = frame_info['frame']['h']
        print frame, x, y, w, h
        box = (x, y, x + w, y + h)
        region = im.crop(box)
        region.save(path + frame)

except IOError:
    print '未找到文件'
else:
    atlas.close()

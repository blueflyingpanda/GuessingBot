from ImgShapeBuilder import ImgShapeBuilder
import os
import sys

data_dir = 'data'
new_data_dir = 'new_data'

for shape_dir in os.listdir(new_data_dir):
    for pic in os.listdir(new_data_dir+'/'+shape_dir):
        os.replace(new_data_dir+'/'+shape_dir+'/'+pic, data_dir+'/'+shape_dir+'/'+pic)


if len(sys.argv) == 2 and sys.argv[1] == 'gen':
    isb = ImgShapeBuilder(data_dir, 28, 28)
    isb.generate_all(100)

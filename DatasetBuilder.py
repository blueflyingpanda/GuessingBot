from ImgShapeBuilder import ImgShapeBuilder
import os
import sys

data_dir = 'data'
new_data_dir = 'new-data'

for shape_dir in os.listdir(new_data_dir):
    for pic in os.listdir(new_data_dir+'/'+shape_dir):
        os.replace(new_data_dir+'/'+shape_dir+'/'+pic, data_dir+'/'+shape_dir+'/'+pic)


# with open("e.txt", "w") as current:
#     current.write('0')
# with open("t.txt", "w") as current:
#     current.write('0')
# with open("r.txt", "w") as current:
#     current.write('0')
isb = ImgShapeBuilder(data_dir, 28, 28)
if len(sys.argv) == 2 and sys.argv[1] == 'gen':
    isb.generate_all(100)

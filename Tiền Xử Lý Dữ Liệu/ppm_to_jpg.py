from PIL import Image
from os import walk, makedirs 
from os.path import exists 

folder = "./train"
save_path = "./trainxong"

files = []
for (dirpath, dirnames, filenames) in walk(folder): 
	files += list(map(lambda x: dirpath+"/"+x,filenames)) 

files = [f for f in files if f.endswith(".ppm")] 

count=1
for i in files:
	im = Image.open(i) # mở ảnh file định dạng là .ppm
	save_file_name = save_path + '/' + ((i.split('/',4)[-1]).split(".")[0]) + ".jpg"

	im.save(save_file_name)
	print("File #",count,":",save_file_name)
	count+=1
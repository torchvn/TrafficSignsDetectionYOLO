import os
max_width = 1360
max_height = 800

with open('gt.txt') as fp:
    for l in fp:
        l=l.rstrip('\n')
        words = l.split(";") 
        words[0] = words[0].replace(".ppm", "")

        filename = words[0]+".txt"

        name = words[0]
        left_col = int(words[1])
        up_row = int(words[2])
        right_col = int(words[3])
        down_row = int(words[4])
        class_no = int(words[5])

        box_width = float(right_col - left_col)
        box_height = float(down_row - up_row)

        op = str(class_no) + " " + str((left_col+(right_col-left_col)/2)/max_width) + " " + str((up_row+(down_row - up_row)/2)/max_height) + " " + str(box_width/max_width) + " " + str(box_height/max_height)+"\n"

        # Open a file
        fo = open(filename, "a")
        fo.write(op)

        # Close opend file
        fo.close()
	


"""
In this project, functions that will enable the application of image transformation techniques on a particular image have been realized.
"""
import random

#This function will generate an image with random values for each channel. 
def generate_random(row, column):
    rowl= []
    for i in range(row):
        rowl.append([])
        for j in range(column):
            pixelc = {'red': 0, 'green': 0, 'blue': 0}
            pixelc['red'] = random.randint(0,255)  #The random values should be integers between 0 and 255.
            pixelc['green'] = random.randint(0,255)  #The random values should be integers between 0 and 255.
            pixelc['blue'] = random.randint(0,255)   #The random values should be integers between 0 and 255.
            rowl[-1].append(pixelc)
    image = []
    for i in rowl:
        image.append(i)
    return image

#This function will take the image and check if each pixel is valid in the image
def is_valid(img):
    values = []
    for i in img:
        for j in i:
            values.append(j['red'])
            values.append(j['green'])
            values.append(j['blue'])
    valuescopy= values[:]
    for i in valuescopy:
        if int(i) != i:
            return False
        if 0 <= i <= 255:
            values.remove(i)
    if len(values) != 0:
        return False
    else:
        return True

#This function will read the given file with the filename as input, convert the hex strings to the given image format.   
def read_from_file(filename):
    listvalue = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            listvalue.append(line.strip("\n").split(","))
    
    for i in range(len(listvalue)):
        for j in range(len(listvalue[0])):
            hexing = hextorgb(listvalue[i][j])
            listvalue[i][j] = hexing[0]
    return listvalue

def hextorgb(hexE):
    endlist = []
    ls=[]
    hexE = hexE.lstrip('#')
    lv = len(hexE)
    a = (tuple(int(hexE[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))
    
    count=0
    for i in a:
        ls.append(i)
        count += 1
        if count == 3:
            pixel = ['red', 'green', 'blue']
            endlist.append( dict(zip(pixel,ls)) )
            ls=[]
    return endlist 

def rgb_to_hex(rgbd):
    return '%02x%02x%02x' % rgbd

#This function will take two parameters, img as image and filename as the filename to be written, then write the given image to the given file using hex strings.
def write_to_file(img, filename):
    with open(filename, "a") as f:
        count = 0
        dimension = 0
        for i in img:
            dimension += 1
        for i in img:
            for j in i:
                rgb = (j["red"], j["green"], j["blue"])
                
                if (count%dimension) != 0:
                    f.write(rgb_to_hex(rgb) + ',')
                else:
                    f.write('\n')
                count +=1
    return None

#This function will set each channel to 0.        
def clear(img):
    for i in img:
        for j in i:
            j['red']= 0
            j['green']= 0
            j['blue']= 0
    return None

#This function will set the specified channel to the given value.
def set_value(img, value, channel='rgb'):
    for i in img:
        for j in i:
            if 'r' in channel:
                j['red']= value
            if 'g' in channel:
                j['green']= value
            if 'b' in channel:
                j['blue']= value
    return None

#This function will take an image, go through pixels and correct the pixel values if any of them is not valid. 
def fix(img):
    for i in img:
        for j in i:
            
            if int(j['red']) != j['red']:
                j['red'] = round(j['red'])
            if int(j['green']) != j['green']:
                j['green'] = round(j['green'])
            if int(j['blue']) != j['blue']:
                j['blue'] = round(j['blue'])
                
            if 0 <= j['red'] <= 255:
                pass
            if 0 <= j['green'] <= 255:
                pass
            if 0 <= j['blue'] <= 255:
                pass
            
            if j['red'] < 0:
                j['red'] = 0
            if j['green'] < 0:
                j['green'] = 0  
            if j['blue'] < 0:
                j['blue'] = 0
                   
            if j['red'] > 255:
                j['red'] = 255
            if j['green'] > 255:
                j['green'] = 255
            if j['blue'] > 255:
                j['blue'] = 255
                
    return None

#This function will rotate the image to the right 90°, and return the new image.
def rotate90(img):
    new_image = []
    for i in range(len(img[0])):
        li = list(map(lambda x: x[i], img))
        li.reverse()
        new_image.append(li)
    return new_image

#This function will rotate the image to the right 180°, and return the new image.
def rotate180(img):
    new_image = []
    for i in range(len(img[0])):
        li = list(map(lambda x: x[i], img))
        li.reverse()
        new_image.append(li)
    return rotate90(new_image)

#This function will rotate the image to the right 270°, and return the new image.    
def rotate270(img):    
    new_image = []
    for i in range(len(img[0])):
        li = list(map(lambda x: x[i], img))
        li.reverse()
        new_image.append(li)
    return rotate180(new_image)

#This function will take the mirror of the image with respect to the first dimension.
def mirror_x(img):
    for i in img:
        i.reverse()
    return None

#This function will take the mirror of the image with respect to the second dimension.
def mirror_y(img):
     img.reverse()
     for i in img:
        i.reverse()
     return None

#This function will enhance the specified channel by multiplying that channel with the given value.
def enhance(img, value, channel='rgb'):
    for i in img:
        for j in i:
            if 'r' in channel:
                j['red']= round(value*j['red'])
            if 'g' in channel:
                j['green']= round(value*j['green'])
            if 'b' in channel:
                j['blue']= round(value*j['blue'])
    return None

#This function will convert the image to a grayscale image.
def grayscale(img, mode=1):
    if mode == 1:    #(default) uniformly weighted average (𝑝𝑖,𝑗 = (𝑟𝑖,𝑗 + 𝑔𝑖,𝑗 + 𝑏𝑖,𝑗)/3)
        for i in img:
            for j in i:
                p = (j['red'] + j['green'] + j['blue'])/3
                j['red'] = round(p)
                j['green'] = round(p)
                j['blue'] = round(p)
                fix(img)
    if mode == 2:     #ITU-R BT 601 Standard  (𝑝𝑖,𝑗 = 0.299𝑟𝑖,𝑗 + 0.587𝑔𝑖,𝑗 + 0.114𝑏𝑖,𝑗)
        for i in img:
            for j in i:
                p = (0.299*j['red']) + (0.587*j['green']) + (0.114*j['blue'])
                j['red'] = round(p)
                j['green'] = round(p)
                j['blue'] = round(p)
                fix(img)
    if mode == 3:    #ITU-R BT.709 Standard   (𝑝𝑖,𝑗 = 0.2126𝑟𝑖,𝑗 + 0.7152𝑔𝑖,𝑗 + 0.0722𝑏𝑖,𝑗)
        for i in img:
            for j in i:
                p = (0.2126*j['red']) + (0.7152*j['green']) + (0.0722*j['blue'])
                j['red'] = round(p)
                j['green'] = round(p)
                j['blue'] = round(p)
                fix(img)
    if mode == 4:    #ITU-R BT.2100 Standard   (𝑝𝑖,𝑗 = 0.2627𝑟𝑖,𝑗 + 0.6780𝑔𝑖,𝑗 + 0.0593𝑏𝑖,𝑗)
        for i in img:
            for j in i:
                p = (0.2627*j['red']) + (0.6780*j['green']) + (0.0593*j['blue'])
                j['red'] = round(p)
                j['green'] = round(p)
                j['blue'] = round(p)
                fix(img)
    return None        
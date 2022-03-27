# import os
# from PIL import Image
# from skimage import color
# import numpy
# def createMatrix(loadedImages):
# 	for img in loadedImages:
# 		pix_val = img.getdata()
# 		srcArray = numpy.asarray(pix_val)/255
# 		srcArray = color.rgb2lab(srcArray, illuminant='D50')
# 		# end = color.lab2rgb(srcArray)*255
# 		end = srcArray.astype(numpy.uint8)
# 		print(end)

# def loadImages(path):
#     imagesList = os.listdir(path)
#     loadedImages = []
#     for image in imagesList:
#         if image[-3:] in ["png", "jpg"]:
#             img = Image.open(path + "/" + image)
#             loadedImages.append(img)
#     return loadedImages

# lst = loadImages("/Users/jerrysun/Downloads/omik/JPEG")
# createMatrix(lst)
from skimage import io, color
import os
import numpy as np
##global variables
lab = [21, -8, 14]
tolerance = 6
#


def loadFolder(path):
    colorlist = []
    imagesList = os.listdir(path)
    count = 0
    for image in imagesList:
        if image[-3:] in ["png", "jpg"] and count < 2:
            rgb = io.imread(path + "/" + image)
            lab = color.rgb2lab(rgb)
            colorlist.append(lab)
            print(type(lab))
        count += 1
    print((colorlist[0]))
    print(type((colorlist[0][0][0])))
    # print(colorlist)
    return colorlist


def counter(grid):
    for pic in grid:
        count = 0
        for i in range(len(pic)):
            for j in range(len(pic[0])):
                t = pic[i][j]
                if condition(t[0], 0) and condition(t[1], 1) and condition(t[2], 2):
                    count += 1
        print(count)


# def area(grid):
# 	print(grid[0][1])
# 	m, n = len(grid), len(grid[0])

# 	def dfs(i, j):
# 	    if 0 <= i < m and 0 <= j < n and grid[i][j] is not None:
# 	        grid[i][j] = None
# 	        return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
# 	    return 0

# 	areas = [dfs(i, j) for i in range(m) for j in range(n) if condition(grid[i][j][0], 0) and condition(grid[i][j][1], 1) and condition(grid[i][j][2], 2)]
# 	return max(areas) if areas else 0

# def numIslands(grid):
#     count = 0
#     lst = []
#     for pic in grid:
#         visited = [[False for c in range(len(pic[0]))]
#                    for r in range(len(pic))]
#         for i in range(len(pic) // 2):
#             for j in range(len(pic[0]) // 3):
#                 t = pic[i][j]
#                 if condition(t[0], 0) and condition(t[1], 1) and condition(t[2], 2) and visited[i][j] == False:
#                     dfs(pic, i, j, visited)
#                     count += 1
#     return count


def condition(val, index):
    return lab[index] - tolerance < val < lab[index] + tolerance


def dfs(grid, i, j, visited):
    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] == True):
        return
    visited[i][j] = True
    dfs(grid, i + 1, j, visited)
    dfs(grid, i - 1, j, visited)
    dfs(grid, i, j + 1, visited)
    dfs(grid, i, j - 1, visited)


xd = loadFolder("/Users/jerrysun/Downloads/omik/JPEG")
# print(xd[1])
# print(xd)
# print(xd[0][0][0])
# counter(xd)
# retards(list(loadFolder))
# print(area(xd[0]))
# print(numIslands(xd))

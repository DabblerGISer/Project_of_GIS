from osgeo import gdal, gdalconst
import os
import numpy as np
import matplotlib.pyplot as plt

inputpath = 'E:\\geoinfosys\\Lab\\ProccessedData\\s1\\NDVI_clip.tif'
outputpath = 'E:\\geoinfosys\\Lab\\ProccessedData\\s1\\NDVI_clip_res.tif'
ds = gdal.Open(inputpath)
array = ds.GetRasterBand(1).ReadAsArray()
plt.imshow(array)
plt.colorbar()
print(ds.GetGeoTransform())
print(ds.GetProjection())

dsRes = gdal.Warp(outputpath,ds,xRes = 5, yRes = 5, 
                  resampleAlg = 'mode')
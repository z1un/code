# 图片信息获取
# Author: zjun
# Github: bestreder
# Data: 2020.04.08

from PIL import Image
from PIL.ExifTags import TAGS
import exifread
from geopy.geocoders import Nominatim
import sys
# import re
# from geopy.geocoders import Baidu


def GetImageInfo(imagename):
    with open(imagename, 'rb') as f:
        tags = exifread.process_file(f)
        print('已获取如下数据：')
        for tag in tags.keys():
            print(tag, tags[tag])
        print(' ')

        try:
            ImageWidth = tags['Image ImageWidth']
            ImageLength = tags['Image ImageLength']
            print('图片长宽: %s x %s' % (ImageLength, ImageWidth))
        except:
            print('No Width Length')

        try:
            Make = tags['Image Make']
            Model = tags['Image Model']
            print('拍摄设备: %s, %s' % (Make, Model))
        except:
            print('No Model')

        try:
            Date = tags['EXIF DateTimeOriginal']
            print('拍摄时间: %s' % Date)
        except:
            print('No Date')

        try:
            Date = tags['EXIF DateTimeOriginal']
            Lon = tags['GPS GPSLongitude']
            Lat = tags['GPS GPSLatitude']
            return Lat, Lon
        except:
            return None


def ConvertGps(Lat):
    # 转十进制经纬度
    arr = str(Lat).replace('[', '').replace(']', '').split(', ')
    d = float(arr[0])
    m = float(arr[1])
    s = float(arr[2].split('/')[0]) / float(arr[2].split('/')[1])
    return float(d) + (float(m) / 60) + (float(s) / 3600)


def GetPosition(LL):
    # 由经纬度获取地理地址
    geolocator = Nominatim(user_agent="test")
    location = geolocator.reverse(LL, timeout=200)
    print('拍摄地点: {}'.format(location.address))


if __name__ == '__main__':
    try:
        LatLon = GetImageInfo(sys.argv[1])
        if LatLon != None:
            LL = '%s,%s' % (ConvertGps(LatLon[0]), ConvertGps(LatLon[1]))
            # print('经纬度：  %s' % LL)
            GetPosition(LL)
        else:
            print('No GPS')
    except:
        print('No Image')

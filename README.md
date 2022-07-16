# OfflineMap: a simple html file to visualize offline tiles


* [Introduction](##introduction)
* [Procedure](##Procedure)
* [How to for Android and iOS](##How-to-for-Android-and-iOS)




## Introduction

The project was developped for field purposes. When on the field in Asia to perform hydrologic surveys in remote place with no connection to internet I wrote an html file to hande tiles offline using leaflet and added some useful functionnalities like
 * GPS location,
 * Tracking --- when on a jeep in the middle of nowhere and you wish to now where your heading to---,
 * center ---useful when the road is bumpy and you want to re-center the map on where you are in one click !---
 * lat/lon measurements of points on click.

I'm now using it for different locations and in order to help I wrote a simple function that adapts the file.

OfflineMap does not help you gather the tile files. For this I strongly recommand Map Tiles Downloader


## Procedure

* clone the project directory
* Get The Tiles
* Group them into a tiledir of your choice,
* Get the location (lat,lon) of your map center
* Notice the maxzoom level of your tiles
* Notice the start zoom level
* Create a short script in the main directory that looks like

```python
from   OfflineMap  import *

create_html(
  offlineName="IPGPOffline",
  sitename="IPGP Offline",
  tiledir="ve_tiles",
  center_lon=48.844740,
  center_lat=2.356265,
  zoom_level=6,
  max_native_zoom=19,
)
```
In the case of the example given you should now have an IPGPOffline directory and witin it
* an IPGPOffline.html file
* a copy of the lib directory.

Eventually move your tiledir inside the offlineName directory and enjoy.

## How to for Androing and iOS

You first need to download the OfflineMap directory with all its sub-directories and tiles to your phone/pad  then it depends and the system.


### Android
it's reasonably simple because if you open chrome or Firefox you only need to type

```
file:///sdcard/
```

Normally you'll have access to the directory treefile and you can go and find your directory and html source.

### iOS

iOS is more tricky as Apple does all it can to prevent you from knowing your direcotry structure (to prevent you from doing silly and dangerous things I suppose)!

The trick I found was to install the Html viewer app and open the site file with it. The buttons appears but not the images. If you then go into the log  you'll discover that html viewer does not have the permission to access the location of your html file and bingo ! the entire treefile is written.

Just copy / paste it in firefox or chrome and the site shall be ready and running.

in my case (iphone 8) it looks like
```
file:///private/var/mobile/Containers/Data/Application/
BD4EB054-5DE4-4E61-A422-070D1233C8B9/Documents/
OfflineName/OfflineName.html
```
I suspect the weard code comes from your SD-card.  Anyway it's hacked. Have fun !

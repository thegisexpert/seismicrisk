# create layer from text
#_vlayer = QgsVectorLayer(_ur1, "raw", "delimitedtext")
vlayer =  QgsMapLayerRegistry.instance().mapLayersByName("QueryLayer")[0]

#works fine but:

# export layer to shape
#writer = QgsVectorFileWriter.writeAsVectorFormat\
#(vlayer,"C:\Data\Python\generato\savedfromqgis.shp","utf-8",None,"ESRI Shapefile")

error = QgsVectorFileWriter.writeAsVectorFormat(vlayer, "C:\Data\Python\generato\savedfromqgis.shp",
                                                "4326", None,
                                                "ESRI Shapefile")

if error == QgsVectorFileWriter.NoError:
    print("success!")




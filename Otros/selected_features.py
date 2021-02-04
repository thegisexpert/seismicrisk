print " in selected feature "
#layer = iface.activeLayer()

layer = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

layer.selectAll()
#layer = QgsMapLayerRegistry.instance().mapLayersByName("inter")[0]


selected_features = layer.selectedFeatures()
for i in selected_features:
    attrs = i.attributes()

        # attrs is a list. It contains all the attribute values of this feature
    print attrs


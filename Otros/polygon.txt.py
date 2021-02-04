'POLYGON((' + tostring($x - 1) +  ' ' + tostring($y - 1) + ','
+ tostring($x - 1) +  ' ' + tostring($y + 1) +  ','
+ tostring($x + 1) +  ' ' + tostring($y + 1) +  ','
+ tostring($x + 1) +  ' ' + tostring($y - 1) +  ','
+ tostring($x - 1) +  ' ' + tostring($y - 1) +  '))'


QgsGeometry.fromPolygon([[QgsPoint(1, 1), QgsPoint(2, 2),
                                    QgsPoint(2, 1)]])
SELECT gid, name, ST_Distance_Sphere(geom, ST_MakePoint(13,42))
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom, ST_MakePoint(13,42)) < 71308


SELECT gid, name, ST_Distance_Sphere(geom, ST_MakePoint(13,42))
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom, ST_MakeLine(ST_Geom_From_Text('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))'))) < 71308


"MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.17397362204247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))"732 0 0,13.8329987341189 42.1740039646402 0 0,13.83343364ùù

#query pxoximidad geogrsafica a la strada '?'

SELECT gid, name,
ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')
)
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')) < 20


create table interdependencies as
SELECT gid, name, geom,
ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')
)
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')) < 20

alter table interdependencies  add primary key (gid);


SELECT gid, name, geom,
ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')
) INTO interdependencies
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom,  ST_GeomFromText('MULTILINESTRING ZM ((13.832189598997 42.1740916209451 0 0,13.8323143406616 42.1739736220732 0 0,13.8329987341189 42.1740039646402 0 0,13.833433644247 42.1741185921159 0 0,13.8334134158689 42.1742905333293 0 0,13.8333839161509 42.1742703049512 0 0))')) < 20



SELECT gid, name, geom,
ST_Distance_Sphere(geom,  ST_GeomFromText( ST_AsText('01050000C00100000001020000C003000000085D1D5B2AAA2B40C13A8E1F2A16454000000000000000000000000000000000A9E4524B29AA2B4077AA32422E164540000000000000000000000000000000001F590A9288AA2B40FBD97EE83816454000000000000000000000000000000000'))
) INTO interdependencies
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom,
ST_GeomFromText(ST_AsText('01050000C00100000001020000C003000000085D1D5B2AAA2B40C13A8E1F2A16454000000000000000000000000000000000A9E4524B29AA2B4077AA32422E164540000000000000000000000000000000001F590A9288AA2B40FBD97EE83816454000000000000000000000000000000000'))) < 20





select ST_AsText('01050000C00100000001020000C003000000085D1D5B2AAA2B40C13A8E1F2A16454000000000000000000000000000000000A9E4524B29AA2B4077AA32422E164540000000000000000000000000000000001F590A9288AA2B40FBD97EE83816454000000000000000000000000000000000')
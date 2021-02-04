CREATE TABLE pts AS
WITH rands AS (
  SELECT generate_series as id, random() AS u1, random() AS u2 FROM generate_series(1,100)
)
SELECT
  id,
  ST_SetSRID(ST_MakePoint(
    50 * sqrt(-2 * ln(u1)) * cos(2*pi()*u2),
    50 * sqrt(-2 * ln(u1)) * sin(2*pi()*u2)),4326) AS geom
FROM rands;



SELECT ST_MakePolygon(
		ST_MakeLine(point_geom1,point_geom2,point_geom3,point_geom1)) as poly
		FROM geom_points


--- mio

CREATE TABLE pts AS
WITH rands AS (
  SELECT generate_series as id, random() AS u1, random() AS u2 FROM generate_series(1,100)
)
SELECT
  id,
  SELECT ST_Buffer(ST_SetSRID(ST_MakePoint(
    50 * sqrt(-2 * ln(u1)) * cos(2*pi()*u2),
    50 * sqrt(-2 * ln(u1)) * sin(2*pi()*u2)),4326), 5, 'quad_segs=2') AS geom
FROM rands;


-- segundo intento

-- definitivo --
CREATE TABLE pts AS
WITH rands AS (
  SELECT generate_series as id, random() AS u1, random() AS u2 FROM generate_series(1,100)
)
SELECT
  id,
  (SELECT ST_Buffer(ST_SetSRID(ST_MakePoint(
    50 * sqrt(-2 * ln(u1)) * cos(2*pi()*u2),
    50 * sqrt(-2 * ln(u1)) * sin(2*pi()*u2)),4326), 5, 'quad_segs=1')) AS geom
FROM rands;
-- fin definitivo ---

SELECT ST_MakePolygon(ST_MakeLine(ARRAY[b, c, d, b]))
FROM point a, point_location b, point_location c, point_location d
WHERE a.p1=b.point_id and a.p2=c.point_id and a.p3=d.point_id


SELECT ST_Buffer(
 ST_GeomFromText('POINT(100 90)'),
 50, 'quad_segs=2');



 ST_Project(geography g1, float distance, float azimuth);

 ST_Project(select geom from popoliforpostgres where gid=1, 30,  10);

 select
 ST_Translate((select geom from popoliforpostgres where gid=1), 30,  10)



-- creacion de random point

CREATE TABLE pts2 AS
WITH rands AS (
  SELECT generate_series as id, random() AS u1, random() AS u2 FROM generate_series(10,100)
)
SELECT
  id,
   (select
 ST_Translate((select geom from popoliforpostgres where gid=57), 200 * sqrt(-2 * ln(u1)) * cos(2*pi()*u2) ,
  200 * sqrt(-2 * ln(u1)) * sin(2*pi()*u2))) AS geom
FROM rands;


 select
 ST_Translate((select geom from popoliforpostgres where gid=1), 200 * sqrt(-2 * ln(u1)) * cos(2*pi()*u2) ,
  200 * sqrt(-2 * ln(u1)) * sin(2*pi()*u2))

  ---
  MULTIPOLYGON ZM (((13.8330036383 42.175016704 0 0,13.8336740861 42.1748281406 0 0, 13.8333179107 42.1745714848 0 0, 13.8329984005 42.1748124269 0 0, 13.8329250702 42.1749276601 0 0)))
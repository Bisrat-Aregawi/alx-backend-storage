-- SQL script list all bands with `Glam rock` style
SELECT band_name,
  CASE WHEN split is NULL THEN
    (YEAR(CURRENT_TIMESTAMP) - formed) ELSE (split - formed) END as lifespan
  FROM metal_bands WHERE FIND_IN_SET("Glam rock", style)
  ORDER BY lifespan DESC;

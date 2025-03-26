import fiona
import rasterio
import rasterio.mask

#Diretório da pasta da sub-bacia
path = r'D:\projetos_qswatmod\corumbatai'

#Diretório para o MDE
src_raster_path = r'D:\projetos_qswatmod\codigo_py_modflow_outputs\MDE_UTM.tif'

#Shape dos limites
shp_file_path = path + r'\boundaries.shp'

#MDE cortado
output_raster_path = path + '\mde_clipped.tif'

with fiona.open(shp_file_path, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]

with rasterio.open(src_raster_path) as src:

    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})


with rasterio.open(output_raster_path, "w", **out_meta) as dest:
    dest.write(out_image)

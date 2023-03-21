import requests
from pathlib import Path

points ='91.715, 25.2622, -42.32, 75.1, -42.32, 75.1, 140.1465, 35.2943, 17.1348, 39.0385, 14.2035, 37.1469, 13.4933, 37.2889, 13.2806, 37.3917, -6.8125, 33.9369, 13.5694, 43.5867, 14.3361, 35.9139, 8.8364, 44.6589, 12.4677, 43.6466, 13.6011, 43.5328, 11.918, 45.9142, -3.0143, 43.3796, 32.5311, 25.5, -2.2594, 43.3006, -2.2594, 43.3006, 8.6486, 36.1537, -1.1133, 43.6795, -2.1968, 42.8668, 10.3295, 52.1243, -104.7275, 38.2822, 5.5119, 44.3925, 5.3118, 44.4966, 5.4437, 44.4694, -6.2455, 57.661, 6.3153, 43.9606, -8.9042, 40.1992, -1.8333, 41.1708, -9.3853, 39.3708, -0.4975, 54.4069, -3.2364, 51.1909, 11.5306, 47.4839, 11.9303, 46.5269, 10.471, 45.8193, 28.8022, 45.0742, 78.0246, 31.9654, 119.7058, 31.0798, 119.7064, 31.0819, 109.3211, 23.6953, -104.7892, 31.9091, -104.8328, 31.8658, -104.8768, 31.8767, 56.5162, 53.8885, 56.7287, 53.9247, 57.8914, 50.2458, -114.7778, 36.7333, 109.45, 24.4333, 3.3573, 43.5555, 3.0403, 43.4613, 3.0868, 43.5032, -4.3541, 31.2374, 6.4716, 50.1496, 67.3056, 39.2, 14.3726, 50.0147, 14.3249, 50.0277, -2.7772, 52.3592, -2.7772, 52.3592, -2.5647, 52.6156, -2.6389, 52.5811, -3.79, 51.97, -3.7, 52.03, -3.27, 55.44, 111.4197, 30.9841, -96.0746, 34.4305, 13.3255, 55.7137, 118.4897, 28.8539, 110.374, 30.8605, 12.5024, 58.3589, -57.9653, 49.6829, 109.5257, 28.3895, 109.9647, 28.72, -112.9915, 39.5117, -55.831, 47.0762'
url = "https://gws.gplates.org/reconstruct/coastlines/?&time={time}&model={model}"
# create a folder to save the data
model = "MULLER2022"
saving_path = Path("./coastlines_data/", model)
Path(saving_path).mkdir(parents=True, exist_ok=True)

for year in range(213, 1001):
    # download the data
    url = url.format(time = str(year), model = model)
    coastline_data = requests.get(url).text
    coastline_file_name = str(year) + "ma_coastlines" + ".geojson"
    coastline_file_path = Path(saving_path, coastline_file_name)
    # save the data
    with open(coastline_file_path, 'w') as f:
        f.write(coastline_data)
        print(coastline_file_name + " is saved in " + model + "!")

    # just for test
    #break

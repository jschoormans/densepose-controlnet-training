# load metadata.csv
# make sure the image column is image data type
#%%

from datasets import Dataset, Image
import os
metadata = Dataset.from_csv("data.csv")
image_dataset = metadata.cast_column("file_name", Image())
image_dataset = image_dataset.cast_column("conditioning_image", Image())


#%%

os.chdir('data_folder/train')
image_dataset.push_to_hub('jschoormans/humanpose_densepose')
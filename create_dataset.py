import pandas as pd 
import os 
from PIL import Image
import requests
from transformers import AutoProcessor, BlipForConditionalGeneration
from transformers import AutoProcessor, BlipModel
import time
from tqdm import tqdm
import torch 

begin_time = time.time()

# find all images in /images, 
imgs = os.listdir('data_folder/train')
# keep the jpg without _densepose.jpg
imgs = [i for i in imgs if '_densepose.jpg' not in i]

# create an empty dataframe
df = pd.DataFrame(columns=['file_name', 'conditioning_image', 'caption'])

# process images in batches of 100

STEPSIZE = 250
for i in tqdm(range(0, len(imgs), STEPSIZE)):
    batch_imgs = imgs[i:i+STEPSIZE]

    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    batch_image_paths = ['data_folder/train/' + imagepath for imagepath in batch_imgs]
    batch_images = [Image.open(image_path) for image_path in batch_image_paths]
    inputs = processor(images=batch_images, return_tensors="pt", text=["A picture of" for i in range(len(batch_imgs))])



    # GPU acceleration
    if torch.cuda.is_available():
        device = torch.device("cuda")
        model = model.to(device)  # Move the model to GPU
        inputs = {k: v.to(device) for k, v in inputs.items()}  # Move inputs to GPU
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Using CPU instead.")


    # Generate captions for the batch
    outputs = model.generate(**inputs, max_new_tokens=50 )
    # print(outputs)
    # captions = processor.decode(model.generate(**processor(images=batch_images, text="A picture of", return_tensors="pt"))[0], skip_special_tokens=True, max_new_tokens=50)
    captions = [processor.decode(output, skip_special_tokens=True) for output in outputs]
    print(captions)

    conditioning_images = [imagepath.replace('.jpg', '_densepose.jpg') for imagepath in batch_imgs]
    
    # for imagepath in batch_imgs:
        # caption = processor.decode(model.generate(**processor(images=Image.open('data_folder/train/' + imagepath), text="A picture of", return_tensors="pt", max_new_tokens=50))[0], skip_special_tokens=True)
        # conditioning_image = imagepath.replace('.jpg', '_densepose.jpg')
        
        # batch_captions.append(caption)
        # batch_conditioning_images.append(conditioning_image)
    
    batch_df = pd.DataFrame(list(zip(batch_imgs, conditioning_images, captions)), columns=['file_name', 'conditioning_image', 'caption'])
    df = pd.concat([df, batch_df], ignore_index=True)
    # save dataframe as csv
    
    # SLOW and overwrites the csv
    df.to_csv('data_blip2.csv', index=False)
    print('Batch processed and saved to csv. Time elapsed: ', time.time() - begin_time)

print('Done. Time elapsed: ', time.time() - begin_time)

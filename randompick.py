# open a few random files in directory images. 
# Copy to a new folder called image_inspaction, make that one first.
# Also copy the image with the same name but with _densepose.jpg to the same folder.

# Path: random.py



def main(input_path, output_path):
    # Open a few random files in directory images. 
    # Copy to a new folder called image_inspaction, make that one first.
    # Also copy the image with the same name but with _densepose.jpg to the same folder.
    import os
    import shutil
    import numpy as np 
    # Get all files in input_path
    files = os.listdir(input_path)
    
    # make output_path if it doesn't exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    # Get a random sample of 10 files
    random_files = np.random.choice(files, 10, replace=False)
    # only keep the files that are images and not densepose images
    random_files = [file for file in random_files if file.endswith('.jpg') and not file.endswith('_densepose.jpg')]
    
    # Copy the files to output_path
    for file in random_files:
        shutil.copy(os.path.join(input_path, file), output_path)
        shutil.copy(os.path.join(input_path, file.split('.')[0] + '_densepose.jpg'), output_path)
    
    print('Done.')


if __name__ == "__main__":
    input_path = "images"
    output_path = "image_inspection"
    main(input_path, output_path)
    
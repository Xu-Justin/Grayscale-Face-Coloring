# If this code failed to download the dataset,
# refer to the following link to manually download the dataset.
# https://www.kaggle.com/almightyj/person-face-dataset-thispersondoesnotexist

import kaggle, os, shutil
import cv2
import numpy as np

np.random.seed(42)

def download_kaggle_dataset(dataset_name, path):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, force=True, path=path, quiet=False, unzip=True)

def split(arr, size):
    np.random.shuffle(arr)
    return arr[:int(len(arr)*size)], arr[int(len(arr)*size):]

def create(source, target, file_names):
    os.makedirs( target )
    for i, file_name in enumerate(file_names):
        print('creating data from %s to %s (%d/%d)'%(source, target, i+1, len(file_names)), end='\r')
        image = cv2.imread( os.path.join(source, file_name) )
        image = cv2.resize( image, (256, 256) )
        cv2.imwrite( os.path.join(target, file_name), image )
    print('Successfully created data from %s to %s (%d)'%(source, target, len(file_names)))
        
def remove(path):
    if(os.path.exists(path)):
        shutil.rmtree(path)
        
if __name__ == '__main__':
    remove('raw/')
    download_kaggle_dataset('almightyj/person-face-dataset-thispersondoesnotexist', 'raw/')
    
    source = 'raw/thispersondoesnotexist.10k/'
    file_names = os.listdir(source)
    file_names.sort()
    train, test = split(file_names, 0.8)
    
    remove('train/')
    create(source, 'train/', train)
    
    remove('test/')
    create(source, 'test/', test)
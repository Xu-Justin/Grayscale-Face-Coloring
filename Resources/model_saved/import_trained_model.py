# If this code failed to download the model,
# refer to the following link to manually download the model.
# https://drive.google.com/drive/folders/1PEytwY6AxPYfTmaXY2bwwCap-8KEiUe6?usp=sharing

import os, shutil
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_model(model_name, id, unzip=True):
    print('Downloading %s model from %s'%(model_name, id))
    if (os.path.exists('%s/'%model_name)):
       shutil.rmtree('%s/'%model_name)
    gdd.download_file_from_google_drive(file_id=id, dest_path='./%s.zip'%(model_name), unzip=unzip, showsize=True)
    os.remove('./%s.zip'%(model_name))
    print('Successfully downloaded %s model from %s'%(model_name, id))

if __name__ == '__main__':
    download_model('v1-pix2pix', '1goHw6q7qOUou1qIjC2QLeSQzLGGcy9h5')
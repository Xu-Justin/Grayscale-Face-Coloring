root = '../'

# Model
input_shape = (256, 256) # Height, Width
output_shape = (256, 256, 3) # Height, Wdith, Channel (BGR)
patch_shape = (16, 16) # Height, Width

# Dataset
dir_train = root + 'Dataset/train/'
dir_test = root + 'Dataset/test/'

# Resources
dir_model_saved = root + 'Resources/model_saved/'
dir_model_plot = root + 'Resources/model_plot/'
dir_model_summary = root + 'Resources/model_summary/'
dir_progress_image = root + 'Resources/progress_image/'
dir_progress_image_sample = dir_progress_image + 'sample/'
dir_progress_loss = root + 'Resources/progress_loss/'
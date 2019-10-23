# The dataset is https://www.kaggle.com/ciplab/real-and-fake-face-detection

# Kaggle notebook: https://www.kaggle.com/anastasia484/face-anti-spoofing

# Configuration

DATASET_DIR = '/kaggle/input/real-and-fake-face-detection/real_and_fake_face_detection/real_and_fake_face'
TRAIN_DIR = '/kaggle/train_dataset'
TEST_DIR = '/kaggle/test_dataset'

RATE = 0.2 # splitting proportion for training and test datasets


# Split folders with images into training, validation and test folders.
# OPTION 1 (using split-folders)

#pip install split-folders

#import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
#split_folders.ratio('input_folder', output="output", seed=1337, ratio=(.8, .1, .1)) # default values


# Split image files into test and training set 
# OPTION 2 (copying files into newly created folders)
files_real = os.listdir(f'{DATASET_DIR}/training_real')
files_fake = os.listdir(f'{DATASET_DIR}/training_fake')


# sample from each class to create a test set
np.random.seed(100)
files_real_test = np.random.choice(
    files_real,
    size=round(len(files_real) * RATE),
    replace=False,
    p=None)

files_real_train = list(set(files_real) - set(files_real_test)) #[file for file in files_real if file not in files_real_test] 

files_fake_test = np.random.choice(
    files_fake,
    size=round(len(files_fake) * RATE),
    replace=False,
    p=None)

files_fake_train = list(set(files_fake) - set(files_fake_test)) #[file for file in files_fake if file not in files_fake_test] 

[shutil.copyfile(DATASET_DIR+'/training_real/'+file, TRAIN_DIR+'/real/'+file)  
  for file in files_real_train]
[shutil.copyfile(DATASET_DIR+'/training_fake/'+file, TRAIN_DIR+'/fake/'+file)  
  for file in files_fake_train]

[shutil.copyfile(DATASET_DIR+'/training_real/'+file, TEST_DIR+'/real/'+file)  
  for file in files_real_test]
[shutil.copyfile(DATASET_DIR+'/training_fake/'+file, TEST_DIR+'/fake/'+file)  
  for file in files_fake_test]

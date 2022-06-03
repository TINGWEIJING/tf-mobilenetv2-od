import os
from pathlib import Path

_parent_path = ''
_owner_path = '/content/drive/MyDrive/Shared 01/MobileNetv2'
_shared_path = '/content/drive/MyDrive/MobileNetv2'
if os.path.isdir(_owner_path):
    _parent_path = _owner_path
else:
    _parent_path = _shared_path

# Training
TRAIN_WIDER_PATH = f"{_parent_path}/WIDER_Face_Datasets/raw/WIDER_train/"

# Validation
# VAL_WIDER_PATH = f"{_parent_path}/WIDER_Face_Datasets/raw/WIDER_val/"
VAL_WIDER_PATH = None

# Testing
# TEST_WIDER_PATH = f"{_parent_path}/WIDER_Face_Datasets/raw/WIDER_test/"
TEST_WIDER_PATH = None

# Ground Truth
GROUND_TRUTH_PATH = f"{_parent_path}/WIDER_Face_Datasets/raw/wider_face_split/"

# Output
# OUTPUT_PATH = f"{_parent_path}/WIDER_Face_Datasets/tfrecords_2"
OUTPUT_PATH = f"/content/tfrecords_2"
Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

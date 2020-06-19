from .coco import CocoDataset
from .registry import DATASETS
from .xml_style import XMLDataset
### IMPORT YOUR DATASET FORMAT AND PASS IT IN MYDATASET FUNC
from .builder import DATASETS

@DATASETS.register_module
class MyDataset(XMLDataset):

    CLASSES = ('RBC') ## ADD ALL YOUR CLASSES

# Pascal VOC to Yolo txt format
Conversion tool for object detection tasks. Convert PascalVOC xml's to yolov5txt


## Install
### Dependencies
Python3, tested on 3.7.9, however should work on 3.6+

Uses python package virtualenv, to install run the following:
```pip install virtualenv```

To create a virtualenv, run the following command in the root of the directory
```virtualenv venv```

To activate the virtualenv run:
###### On Windows OS
```venv\Scripts\activate```
###### On Linux/Mac
```source venv/bin/activate```

To install dependencies, run the following command
```pip install -r requirements.txt```

To run the program, ensure all xmls are in a single directory you can reference, and you have created an empty output directory for the txt files. Then run
```python app.py --input path/to/your/xmls --output path/to/where/you/want/your/txt/files```

## Further information
For information on dataset format and training information.
Please refer to: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
This will cover how pixel dimensions are converted to normalised xywh format.

### Improvement list
- [ ] Implement progress bar
- [ ] Train/test splitting
- [ ] Add check for corresponding image
- [ ] Check for duplicate files
- [ ] Ability to set class numbers + class id's (e.g. dog is class id 0)
- [ ] Pytests + github testing + badges
import os
import json
from lxml import etree
# from glob import iglob
from pathlib import Path
import argparse

def convert(img_size, coords):
    """Convert from xmin,xmax,ymin,ymax to xywh normalised format
    Args:
        img_size(array): array of (img_width, img_height)
        coords(array): Array of class_id, xmin, xmax, ymin, ymax
    Returns:
        xywh(array): Array of normalised xywh coords
    """
    img_width = img_size[0]
    img_height = img_size[1]
    #Calculate Bounding box dimensions from xml
    class_id = str(coords[0])
    x_centre = str(((coords[1]+coords[2])/2)/img_width)
    y_centre = str(((coords[3]+coords[4])/2)/img_height)
    height = str((coords[4]-coords[3])/img_height)
    width = str((coords[2]-coords[1])/img_width)
    
    xywh = (class_id, x_centre, y_centre, width, height)
    return xywh
def main():
    """Main processing loop that converts pascal voc xmls to yolov5 txt files.
    """
    labels = {}
    categories = {}
    ##NOTE: May need to ensure it doesn't overwrite existing. not needed 
    # as functionality right now. Onus on user to ensure original xml files
    # don't have duplicates names.
    for xml_file in os.scandir(args.input):
        with open(os.path.join(args.output, f'{Path(xml_file).stem}.txt'), 'w') as txtfile:
            with open(xml_file.path) as file:
                print(f'Processing file {xml_file.name}...')
                #create annotations object
                annotations = etree.fromstring(file.read())
                #extract elements that are needed 
                image_size = annotations.find('size')
                image_width = float(image_size.find('width').text)
                image_height = float(image_size.find('height').text)
                boxes = annotations.iterfind('object')
                for box in boxes:
                    annotation_list = []
                    #Extract bounding box pixel data
                    bndbox = box.find('bndbox')
                    xmin = float(bndbox.find('xmin').text)
                    ymin = float(bndbox.find('ymin').text)
                    xmax = float(bndbox.find('xmax').text)
                    ymax = float(bndbox.find('ymax').text)

                    label_name = box.find('name').text
                    if label_name not in labels:
                        labels[label_name] = len(labels)
                    class_id = labels[label_name]
                    categories[class_id] = label_name
                    # send off for conversion
                    xywh = convert((image_width, image_height), (class_id, xmin, xmax, ymin, ymax))
                    annotation_list.extend(xywh)
                    line = ' '.join(annotation_list)
                    txtfile.write(f'{line}\n')
        txtfile.close()
    print(categories)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        default='data/input',
                        help='Directory location of your input xmls',
                        required=True)
    parser.add_argument('--output', type=str,
                        default='data/output',
                        help='Directory location you want your output txts',
                        required=True)
    args = parser.parse_args()
    main()

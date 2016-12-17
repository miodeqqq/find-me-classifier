#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys
import cv2

from utils import create_output_directory_for_resized_images, get_data_images

def resize_images():
    """
    General method to resize images into 100x100 px objects.
    """

    # create directories for resized images
    create_output_directory_for_resized_images()

    # get images
    get_images = get_data_images(sys.argv[1])

    img_number = 1

    for i, img_item in enumerate(get_images):

        print('Resizing image {index}/{total}'.format(
            index=i+1,
            total=len(get_images)
        ))

        try:
            img = cv2.imread(img_item, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))

            curr_name, new_name = os.path.basename(img_item), img_number

            output_dir = '{dir}/{file_name}{ext}'.format(
                dir='resized_negative_images',
                file_name=new_name,
                ext='.jpg',
            )

            cv2.imwrite(output_dir, resized_image)
            img_number += 1

        except IOError as io:
            print('Error --> {}'.format(io))

def create_negative_bg_file():

    # get images from negative dir and resize into 100x100 px
    # resize_images()

    # get currently resized negative data
    resized_negative_data = get_data_images('resized_negative_images')

    lines = [img_item.strip() for img_item in resized_negative_data]

    with open ('bg.txt', 'w') as neg_file:
        neg_file.write('\n'.join(lines))

    print('Successfully saved bg.txt file!')

create_negative_bg_file()
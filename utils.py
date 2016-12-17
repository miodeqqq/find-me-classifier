#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os

RESIZED_NEGATIVE_PATH = 'resized_negative_images'
RESIZED_POSITIVE_PATH = 'resized_positive_images'


def create_output_directory_for_resized_images():
    """
    General method to create directories for negative images.
    """

    try:
        if not os.path.isdir(RESIZED_NEGATIVE_PATH):
            return os.makedirs(RESIZED_NEGATIVE_PATH)
        elif not os.path.isdir(RESIZED_POSITIVE_PATH):
            return os.makedirs(RESIZED_POSITIVE_PATH)
    except OSError as e:
        print('Error --> {}'.format(e))


def get_data_images(path):
    """
    General method to prepare images.
    """

    return sorted(
        [os.path.join(root, filename) for root, dirnames, filenames in os.walk(path) for filename in
         filenames if
         filename.endswith('.jpg') and os.path.getsize(os.path.join(root, filename)) > 0]
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Michael Raftelis
# DATE CREATED:               9/19/19                   
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    #Get list of files from image directory
    
    filename_list = listdir(image_dir)

# Create empty dictionary for the results
    results_dic = dict()
    
# Create for loop to determine name
    for x in range(0, len(filename_list), 1):
#Turn to lower case and divide filename by _
        pet_img = filename_list[x].lower().split("_")
        pet_name = ""
        for word in pet_img:
            
#If word is alpha only add it to string            
            if word.isalpha():
                pet_name += word + " "
                
 #Strip off leading / trailing whitespace characters
        pet_name = pet_name.strip()

#Check for duplicates and add to results dictionary    
        if filename_list[x] not in results_dic:
            results_dic[filename_list[x]] = [pet_name]
        else:
            print("Duplicate filename")
  
#return results dictionary
    
    return results_dic

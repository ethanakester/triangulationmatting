## CSC320 Winter 2019 
## Assignment 1
## (c) Kyros Kutulakos
##
## DISTRIBUTION OF THIS CODE ANY FORM (ELECTRONIC OR OTHERWISE,
## AS-IS, MODIFIED OR IN PART), WITHOUT PRIOR WRITTEN AUTHORIZATION 
## BY THE INSTRUCTOR IS STRICTLY PROHIBITED. VIOLATION OF THIS 
## POLICY WILL BE CONSIDERED AN ACT OF ACADEMIC DISHONESTY

##
## DO NOT MODIFY THIS FILE ANYWHERE EXCEPT WHERE INDICATED
##

# import basic packages
import numpy as np
# import scipy.linalg as sp
import cv2

# If you wish to import any additional modules
# or define other utility functions, 
# include them here

#########################################
## PLACE YOUR CODE BETWEEN THESE LINES ##
#########################################


#########################################

#
# The Matting Class
#
# This class contains all methods required for implementing 
# triangulation matting and image compositing. Description of
# the individual methods is given below.
#
# To run triangulation matting you must create an instance
# of this class. See function run() in file run.py for an
# example of how it is called
#
class Matting:
    #
    # The class constructor
    #
    # When called, it creates a private dictionary object that acts as a container
    # for all input and all output images of the triangulation matting and compositing 
    # algorithms. These images are initialized to None and populated/accessed by 
    # calling the the readImage(), writeImage(), useTriangulationResults() methods.
    # See function run() in run.py for examples of their usage.
    #
    def __init__(self):
        self._images = { 
            'backA': None, 
            'backB': None, 
            'compA': None, 
            'compB': None, 
            'colOut': None,
            'alphaOut': None, 
            'backIn': None, 
            'colIn': None, 
            'alphaIn': None, 
            'compOut': None, 
        }

    # Return a dictionary containing the input arguments of the
    # triangulation matting algorithm, along with a brief explanation
    # and a default filename (or None)
    # This dictionary is used to create the command-line arguments
    # required by the algorithm. See the parseArguments() function
    # run.py for examples of its usage
    def mattingInput(self): 
        return {
            'backA':{'msg':'Image filename for Background A Color','default':None},
            'backB':{'msg':'Image filename for Background B Color','default':None},
            'compA':{'msg':'Image filename for Composite A Color','default':None},
            'compB':{'msg':'Image filename for Composite B Color','default':None},
        }
    # Same as above, but for the output arguments
    def mattingOutput(self): 
        return {
            'colOut':{'msg':'Image filename for Object Color','default':['color.tif']},
            'alphaOut':{'msg':'Image filename for Object Alpha','default':['alpha.tif']}
        }
    def compositingInput(self):
        return {
            'colIn':{'msg':'Image filename for Object Color','default':None},
            'alphaIn':{'msg':'Image filename for Object Alpha','default':None},
            'backIn':{'msg':'Image filename for Background Color','default':None},
        }
    def compositingOutput(self):
        return {
            'compOut':{'msg':'Image filename for Composite Color','default':['comp.tif']},
        }
    
    # Copy the output of the triangulation matting algorithm (i.e., the 
    # object Color and object Alpha images) to the images holding the input
    # to the compositing algorithm. This way we can do compositing right after
    # triangulation matting without having to save the object Color and object
    # Alpha images to disk. This routine is NOT used for partA of the assignment.
    def useTriangulationResults(self):
        if (self._images['colOut'] is not None) and (self._images['alphaOut'] is not None):
            self._images['colIn'] = self._images['colOut'].copy()
            self._images['alphaIn'] = self._images['alphaOut'].copy()



    # If you wish to create additional methods for the 
    # Matting class, include them here

    #########################################
    ## PLACE YOUR CODE BETWEEN THESE LINES ##
    #########################################

    #########################################
            
    # Use OpenCV to read an image from a file and copy its contents to the 
    # matting instance's private dictionary object. The key 
    # specifies the image variable and should be one of the
    # strings in lines 54-63. See run() in run.py for examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # leave the matting instance's dictionary entry unaffected and return
    # False, along with an error message
    def readImage(self, fileName, key):
        success = False
        msg = 'Placeholder'




        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        img = cv2.imread(fileName)
        if img is not None:
            self._images[key] = cv2.imread(fileName)
            success = True
            return success
        msg = 'There is no image in that file!'
        #########################################
        return success, msg

    # Use OpenCV to write to a file an image that is contained in the 
    # instance's private dictionary. The key specifies the which image
    # should be written and should be one of the strings in lines 54-63. 
    # See run() in run.py for usage examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # return False, along with an error message
    def writeImage(self, fileName, key):
        success = False
        msg = 'Placeholder'




        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        if self._images[key] is not None:
            cv2.imwrite(fileName, self._images[key])
            success = True
            return success

        msg = "The image you're trying to write does not exist!"
        #########################################
        return success, msg

    # Method implementing the triangulation matting algorithm. The
    # method takes its inputs/outputs from the method's private dictionary 
    # ojbect. 
    def triangulationMatting(self):
        """
success, errorMessage = triangulationMatting(self)
        
        Perform triangulation matting. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """


        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        if self._images['compA'] is None or self._images['compB'] is None or self._images['backA'] is None \
            or self._images['backB'] is None:
            msg = "You're missing one of: compA, compB, backA, backB!"
            return success, msg

        # Retrieve pictures to be matted
        fimg1 = self._images['compA']
        fimg2 = self._images['compB']
        bimg1 = self._images['backA']
        bimg2 = self._images['backB']
        
        # Retrieve each colour from composite images
        CAR = fimg1[:, :, 0]
        CAB = fimg1[:, :, 1]
        CAG = fimg1[:, :, 2]
        CBR = fimg2[:, :, 0]
        CBB = fimg2[:, :, 1]
        CBG = fimg2[:, :, 2]

        # Retrieve each colour from background images
        BAR = bimg1[:, :, 0]
        BAB = bimg1[:, :, 1]
        BAG = bimg1[:, :, 2]
        BBR = bimg2[:, :, 0]
        BBB = bimg2[:, :, 1]
        BBG = bimg2[:, :, 2]

        # All images are the same size
        img_shape = fimg1.shape

        # Initialize 3-dim matrix with zeroes to be filled
        colOut = np.zeros(img_shape)

        # Initialize 2-dim matrixx with zeroes to be filled
        alphaOut = np.zeros(img_shape[:2])

        # Create matrix for the linear equation
        mult_mat = np.array([[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1],
                             [1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]])

        # Go through each pixel
        for i in img_shape[0]:
            for j in img_shape[1]:
                temp_a = np.array([[CAR[i, j]],
                                  [CAB[i, j]],
                                  [CAG[i, j]],
                                  [CBR[i, j]],
                                  [CBB[i, j]],
                                  [CBG[i, j]]])

                temp_b = np.array([[BAR[i, j]],
                                  [BAB[i, j]],
                                  [BAG[i, j]],
                                  [BBR[i, j]],
                                  [BBB[i, j]],
                                  [BBG[i, j]]])
                # Create matrix for linear equation
                temp_c = np.hstack(mult_mat, -1*temp_a)
                # result = np.clip(np.dot(np.linalg.pinv(temp_c), temp_b), 0, 1)
                result = np.dot(np.linalg.pinv(temp_c), temp_b)
                colOut[i, j] = np.array([result[0][0], result[1][0], result[2][0]])

                # Only care about alpha values for greyscale
                alphaOut = np.array([result[3]])
        self._images['alphaOut'] = alphaOut
        self._images['colOut'] = colOut

        success = True


        #########################################

        return success

    def createComposite(self):
        """
success, errorMessage = createComposite(self)

        Perform compositing. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
"""

        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################

        #########################################

        self.triangulationMatting()
        self.useTriangulationResults()
        if self._images['alphaIn'] is not None and self._images['backIn'] is not None \
                and self._images['colIn'] is not None:
            self._images['compOut'] = self._images['colIn'] + (1-self._images['alphaIn']) * self._images['backIn']
            success = True
            return success

        msg = "You're missing one of: colIn, alphaIn, or backIn!"

        return success, msg



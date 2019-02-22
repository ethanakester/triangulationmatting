# triangulationmatting
Implementation of triangulation matting technique described in the paper Blue Screen Matting by Alvy Ray Smith and James F. Blinn.
This generates the greyscale image containing the alpha values of the foreground object, and an image containing the full colour of the foreground object. This triangulation matting requires 4 images: compA, compB, backA, and backB. compA and compB must be the foreground object in the exact same position in front of two different backgrounds, and backA and backB must be those backgrounds identically as they were in compA and compB but without any foreground object.
This is coursework for the first assignment of the CSC320 course at University of Toronto.

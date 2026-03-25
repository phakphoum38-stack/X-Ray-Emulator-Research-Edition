import numpy as np

class ImageReconstruction:

    def normalize(self,image):

        image = image / np.max(image)

        return image

    def enhance(self,image):

        image = np.sqrt(image)

        return image

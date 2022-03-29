#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part is an introduction to PCA

# In this example, we will load a kitten picture from the web and apply PCA on it with different numbers of
# components to observe the effect of smoothing

import numpy as np
import requests as requests
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

pic_link = "https://cdn.royalcanin-weshare-online.io/0uc5Q3cBaPOZra8qpKOJ/v1/ede7t-image-finding-a-kitten-on-the-street"
r = requests.get(pic_link)

with open("kitten.jpg", "wb") as f:
    f.write(r.content)

with Image.open("kitten.jpg").convert("L") as im:
    im_array = np.array(im)  # noqa
    plt.imshow(im_array, cmap="gray")
    plt.show()

for n in [100, 50, 40, 30, 20, 10, 4]:
    pca = PCA(n_components=n)
    pca.fit(im_array)
    plt.title(f"PCA on Image with {n} components")
    plt.imshow(pca.inverse_transform(pca.transform(im_array)), cmap="gray")
    plt.savefig(f"kitten_pca_{n}.png")
    plt.show()

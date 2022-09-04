import matplotlib.pyplot as plt
from skimage import data
from skimage.util import img_as_ubyte
import skimage
import skimage.io, skimage.color
import skimage.morphology

I = skimage.io.imread('ImgProcBasics/img/MorphoImage.jpg')
I = skimage.color.rgb2gray(I)
I = (I > 0.5).astype('uint8')
plt.imshow(I, cmap='gray')

plt.figure()
elem = skimage.morphology.disk(2)
Idil = skimage.morphology.dilation(I, elem)
plt.imshow(Idil, cmap=plt.cm.gray)

# dilated = dilation(orig_phantom, footprint)
# plt.figure()
# plt.imshow(dilated, cmap=plt.cm.gray)

# orig_phantom = img_as_ubyte(data.shepp_logan_phantom())
# orig_phantom = I
# fig, ax = plt.subplots()
# ax.imshow(orig_phantom, cmap=plt.cm.gray)

# def plot_comparison(original, filtered, filter_name):

#     fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
#                                    sharey=True)
#     ax1.imshow(original, cmap=plt.cm.gray)
#     ax1.set_title('original')
#     ax1.axis('off')
#     ax2.imshow(filtered, cmap=plt.cm.gray)
#     ax2.set_title(filter_name)
#     ax2.axis('off')

# from skimage.morphology import (erosion, dilation, opening, closing,  # noqa
#                                 white_tophat)
# from skimage.morphology import black_tophat, skeletonize, convex_hull_image  # noqa
# from skimage.morphology import disk  # noqa

# footprint = disk(2)
# eroded = erosion(orig_phantom, footprint)
# plot_comparison(orig_phantom, eroded, 'erosion')

# dilated = dilation(orig_phantom, footprint)
# plt.figure()
# plt.imshow(dilated, cmap=plt.cm.gray)
# #plot_comparison(orig_phantom, dilated, 'dilation')

plt.show()
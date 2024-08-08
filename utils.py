import matplotlib.pyplot as plt
import numpy as np

def print_images(data_samples, figsize=(10, 20)):
    fig, axes = plt.subplots(len(data_samples), 1, figsize=figsize)
    mean = np.array([0.5, 0.5, 0.5])
    std = np.array([0.5, 0.5, 0.5])

    for sample in data_samples:
        idx, img = sample[0], sample[1]
        img = img[0] # torch.squeeze(img, 0)
        img = img.numpy().transpose(1, 2, 0)
        img = img * std + mean
        # img = np.clip(img, 0, 1)
        axes[idx].imshow(img)
        axes[idx].axis('off')
        axes[idx].set_title(f'sample_{idx}')

    plt.show()
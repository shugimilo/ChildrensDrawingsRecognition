import os
import random
import shutil

project_dir = r"C:\Users\Win11\PycharmProjects\pythonProject"
images_dir = os.path.join(project_dir, 'data', 'images', 'train')
labels_dir = os.path.join(project_dir, 'data', 'labels', 'train')
val_images_dir = os.path.join(project_dir, 'data', 'images', 'val')
val_labels_dir = os.path.join(project_dir, 'data', 'labels', 'val')

assert os.path.exists(images_dir), f"Images directory not found: {images_dir}"
assert os.path.exists(labels_dir), f"Labels directory not found: {labels_dir}"

os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

all_images = [f for f in os.listdir(images_dir) if f.endswith(('.jpeg', '.jpg'))]

all_labels = [f.replace('.jpg', '.txt').replace('.jpeg', '.txt') for f in all_images]

assert all(len(all_images) == len(all_labels) for l in all_labels), "Number of images and labels do not match."

val_size = 0.15
val_count = int(len(all_images) * val_size)

combined_list = list(zip(all_images, all_labels))
random.shuffle(combined_list)

val_list = combined_list[:val_count]

for img, label in val_list:
    shutil.move(os.path.join(images_dir, img), os.path.join(val_images_dir, img))
    shutil.move(os.path.join(labels_dir, label), os.path.join(val_labels_dir, label))

print(f'Moved {val_count} images and labels to validation set.')

import os
import shutil
from sklearn.model_selection import train_test_split

DATASET_PATH = './dataset'
DESTINATION_PATH = './dataset/stratification'

os.makedirs(os.path.join(DESTINATION_PATH, 'images'))
os.makedirs(os.path.join(DESTINATION_PATH, 'labels'))

dataset = [item for item in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, item))]
for folder in dataset:
    images = os.listdir(os.path.join(DATASET_PATH, folder, 'images'))
    for image in images:
        image_src = os.path.join(DATASET_PATH, folder, 'images', image)
        image_dst = os.path.join(DESTINATION_PATH, 'images', image)
        if not os.path.exists(image_dst):
            shutil.move(image_src, image_dst)
    labels = os.listdir(os.path.join(DATASET_PATH, folder, 'labels'))
    for label in labels:
        label_src = os.path.join(DATASET_PATH, folder, 'labels', label)
        label_dst = os.path.join(DESTINATION_PATH, 'labels', label)
        if not os.path.exists(label_dst):
            shutil.move(label_src, label_dst)

images = os.listdir(os.path.join(DESTINATION_PATH, 'images'))
labels = os.listdir(os.path.join(DESTINATION_PATH, 'labels'))
images.sort()
labels.sort()

print('Stratification: ')
print(f'total: {len(images)} images {len(labels)} labels')

(train_images, valid_images,
 train_labels, valid_labels) = train_test_split(images, labels, test_size=0.2, random_state=1)
(valid_images, test_images,
 valid_labels, test_labels) = train_test_split(valid_images, valid_labels, test_size=0.5, random_state=1)

result = {
    'train_images': train_images, 'train_labels': train_labels,
    'valid_images': valid_images, 'valid_labels': valid_labels,
    'test_images': test_images, 'test_labels': test_labels
}


def move_labels_and_images(dst: str, images: list, labels: list) -> None:
    for image in images:
        try:
            shutil.move(os.path.join(DESTINATION_PATH, 'images', image), os.path.join(DATASET_PATH, dst, 'images', image))
        except Exception as e:
            print(image, e)
    for label in labels:
        try:
            shutil.move(os.path.join(DESTINATION_PATH, 'labels', label), os.path.join(DATASET_PATH, dst, 'labels', label))
        except Exception as e:
            print(label, e)


for folder in dataset:
    if folder == 'stratification':
        continue
    print(f'{folder}: {len(result.get(f'{folder}_images'))} images {len(result.get(f'{folder}_labels'))} labels')
    move_labels_and_images(folder, result.get(f'{folder}_images'), result.get(f'{folder}_labels'))

os.removedirs(os.path.join(DESTINATION_PATH, 'images'))
os.removedirs(os.path.join(DESTINATION_PATH, 'labels'))

import os
import shutil
from sklearn.model_selection import train_test_split

PERCENT_TRAIN = 80
DATASET_PATH = './dataset2'
DESTINATION_PATH = './dataset2/stratification'

dataset = [item for item in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, item))]


def before_all() -> None:
    os.makedirs(os.path.join(DESTINATION_PATH, 'images'))
    os.makedirs(os.path.join(DESTINATION_PATH, 'labels'))


def after_all() -> None:
    os.removedirs(os.path.join(DESTINATION_PATH, 'images'))
    os.removedirs(os.path.join(DESTINATION_PATH, 'labels'))


def unify_from_yolov8() -> None:
    for folder in dataset:
        images = os.listdir(os.path.join(DATASET_PATH, folder, 'images'))
        for image in images:
            image_src = os.path.join(DATASET_PATH, folder, 'images', image)
            image_dst = os.path.join(DESTINATION_PATH, 'images', image)
            if not os.path.exists(image_dst):
                try:
                    shutil.move(image_src, image_dst)
                except Exception as e:
                    print(image, e)
        labels = os.listdir(os.path.join(DATASET_PATH, folder, 'labels'))
        for label in labels:
            label_src = os.path.join(DATASET_PATH, folder, 'labels', label)
            label_dst = os.path.join(DESTINATION_PATH, 'labels', label)
            if not os.path.exists(label_dst):
                try:
                    shutil.move(label_src, label_dst)
                except Exception as e:
                    print(label, e)


def stratify() -> dict:
    images = os.listdir(os.path.join(DESTINATION_PATH, 'images'))
    labels = os.listdir(os.path.join(DESTINATION_PATH, 'labels'))
    images.sort()
    labels.sort()
    print('Stratification: ')
    print(f'total: {len(images)} images {len(labels)} labels')
    percent = (100 - PERCENT_TRAIN) / 100
    (train_images, valid_images,
     train_labels, valid_labels) = train_test_split(images, labels, test_size=percent, random_state=1)
    (valid_images, test_images,
     valid_labels, test_labels) = train_test_split(valid_images, valid_labels, test_size=0.5, random_state=1)
    return {
        'train_images': train_images, 'train_labels': train_labels,
        'valid_images': valid_images, 'valid_labels': valid_labels,
        'test_images': test_images, 'test_labels': test_labels
    }


def distribute_for_yolov8(result: dict) -> None:
    for folder in dataset:
        if folder == 'stratification':
            continue
        print(f'{folder}: {len(result.get(f'{folder}_images'))} images {len(result.get(f'{folder}_labels'))} labels')
        for image in result.get(f'{folder}_images'):
            try:
                shutil.move(os.path.join(DESTINATION_PATH, 'images', image),
                            os.path.join(DATASET_PATH, folder, 'images', image))
            except Exception as e:
                print(image, e)
        for label in result.get(f'{folder}_labels'):
            try:
                shutil.move(os.path.join(DESTINATION_PATH, 'labels', label),
                            os.path.join(DATASET_PATH, folder, 'labels', label))
            except Exception as e:
                print(label, e)


if __name__ == '__main__':
    before_all()
    unify_from_yolov8()
    data = stratify()
    distribute_for_yolov8(data)
    after_all()


from pixellib.instance import instance_segmentation


def object_detection_on_an_image():
    segment_image = instance_segmentation()
    segment_image.load_model(
        '/workspaces/object_detection_in_an_image/IMG_20230920_144955.jpg')
    'output_image_name' == "output.jpg"


if __name__ == '__main__':
    object_detection_on_an_image()

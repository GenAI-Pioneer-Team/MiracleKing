import image_stitching.read_images as read_images
import image_stitching.recursion as recursion
import sys
import cv2
import os
import glob


def main(image_folder):
    """
    Main function of the repository.
    Takes in an image folder, loads all image files in the folder,
    runs the complete image stitching pipeline to create and export 
    a panoramic image in the /outputs/ folder.

    Args:
        image_folder (str): Path to the folder containing images.
    """
    print(os.path.join(image_folder[0], "*.*"))
    image_dir_list = glob.glob(os.path.join(image_folder[0], "*.[jpJP][pnPN][gG]"))
    
    if not image_dir_list:
        print("No images found in the specified folder.")
        return
    
    images_list, no_of_images = read_images.read(image_dir_list)
    result, mapped_image = recursion.recurse(images_list, no_of_images)
    
    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite("outputs/panorama_image.jpg", result)
    cv2.imwrite("outputs/mapped_image.jpg", mapped_image)

    print(f"Panoramic image saved at: outputs/panorama_image.jpg")
    print("Mapped image saved at: outputs/mapped_image.jpg")


if __name__ == "__main__":
    image_list = []
    for i in range(1, len(sys.argv)):
        image_list.append(sys.argv[i])
    main(image_list)

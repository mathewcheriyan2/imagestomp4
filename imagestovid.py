import cv2
import os


def images_to_video(image_folder, output_file, fps):
    image_files = sorted([f for f in os.listdir(
        image_folder) if f.endswith('.jpg') or f.endswith('.png')])

    # Read the first image to get the dimensions
    first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Loop through the image files and write each frame to the video
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        video.write(frame)

    # Release the video writer and close any open windows
    video.release()
    cv2.destroyAllWindows()


# Usage example
# Folder containing input images
image_folder = r'workspace\data_src'
# Output video file name
output_file = r'workspace\data_src\output.mp4'
fps = 30                         # Frames per second

images_to_video(image_folder, output_file, fps)

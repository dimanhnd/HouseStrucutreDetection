import os
from PIL import Image

def resize_and_concatenate_images(mador_folder, result_folder, merge_folder):
    # Create merge folder if it doesn't exist
    if not os.path.exists(merge_folder):
        os.makedirs(merge_folder)

    # Get list of files in both mador and result folders
    mador_files = os.listdir(mador_folder)
    result_files = os.listdir(result_folder)

    # Resize and concatenate images
    for mador_file in mador_files:
        if mador_file in result_files:
            # Open and resize mador image
            mador_path = os.path.join(mador_folder, mador_file)
            mador_img = Image.open(mador_path)
            mador_img = mador_img.resize((256, 256))

            # Open and resize result image
            result_path = os.path.join(result_folder, mador_file)
            result_img = Image.open(result_path)
            result_img = result_img.resize((256, 256))

            # Create a new image with width = 512 and height = 256
            merged_img = Image.new('RGB', (512, 256))

            # Paste mador image on the left side
            merged_img.paste(mador_img, (0, 0))

            # Paste result image on the right side
            merged_img.paste(result_img, (256, 0))

            # Save the merged image
            merged_img.save(os.path.join(merge_folder, f'merged_{mador_file}'))

# Example usage
mador_folder = './madori'
result_folder = './result'
merge_folder = './mergeImg'

resize_and_concatenate_images(mador_folder, result_folder, merge_folder)

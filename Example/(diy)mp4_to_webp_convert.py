#A lot of files cant be pushed into github because of the file size limit. This script is used to convert a video file into a sequence of optimized .webp frames, 
#which can be easily pushed to github and used in the HTML file.
#For inspecting the example, you can run the script and it will generate the frames in the "frames" folder.
# You can then use these frames in the HTML file to create the animation. 

import os
import cv2


def extract_video_frames(
    video_path, output_folder="frames", quality=80, frame_skip=1
):
    """Converts a video file into a sequence of optimized .webp frames.

    :param video_path: Path to your input video file (e.g., 'orange_cola.mp4')
    :param output_folder: Folder where the webp images will be saved
    :param quality: WebP compression quality (1-100). 80 is ideal for web
    :param frame_skip: 1 means extract every frame. 2 means extract every second
    frame.
    """
    # Open the video file
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"❌ Error: Could not open video file '{video_path}'")
        return

    # Automatically create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Created folder: {output_folder}")

    total_video_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print(f"🎬 Video loaded successfully!")
    print(f"   - Total Frames in Video: {total_video_frames}")
    print(f"   - Original FPS: {fps}")
    print(f"⏳ Processing frames... Please wait.")

    video_frame_id = 0
    saved_frame_id = 0

    while True:
        success, frame = video.read()

        # Break the loop when the video reaches the end
        if not success:
            break

        # Process frame based on frame_skip rate
        if video_frame_id % frame_skip == 0:
            # Generate the exact sequential filename required by the HTML file
            output_filename = f"{saved_frame_id}.webp"
            output_filepath = os.path.join(output_folder, output_filename)

            # CV2 uses [Quality Parameter, Value] for WebP compression
            # cv2.IMWRITE_WEBP_QUALITY key value is 64
            cv2.imwrite(
                output_filepath, frame, [int(cv2.IMWRITE_WEBP_QUALITY), quality]
            )

            saved_frame_id += 1

        video_frame_id += 1

    # Clean up memory resources
    video.release()

    print("\n✅ Extraction Complete!")
    print(f"📦 Total WebP frames generated: {saved_frame_id}")
    print(f"📂 Saved location: ./{output_folder}/")


# =========================================================================
# 🔥 CONFIGURATION & EXECUTION
# =========================================================================
if __name__ == "__main__":
    # Change 'orange_cola.mp4' to your actual video filename
    INPUT_VIDEO = "orange_cola.mp4"

    # Settings optimized for premium web scrollytelling
    OUTPUT_DIR = "frames"  # Folder name
    WEBP_QUALITY = 85  # Balance between crisp visuals and tiny file sizes
    FRAME_SKIP = 1  # Keep at 1 for ultra-smooth animations

    extract_video_frames(
        video_path=INPUT_VIDEO,
        output_folder=OUTPUT_DIR,
        quality=WEBP_QUALITY,
        frame_skip=FRAME_SKIP,
    )
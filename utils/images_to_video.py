import cv2
import os

def create_video(image_folder, output_video, fps=30):

    images = sorted([
        img for img in os.listdir(image_folder)
        if img.endswith(".jpg")
    ])

    first_frame = cv2.imread(
        os.path.join(image_folder, images[0])
    )

    height, width, _ = first_frame.shape

    writer = cv2.VideoWriter(
        output_video,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    for image in images:
        frame = cv2.imread(
            os.path.join(image_folder, image)
        )
        writer.write(frame)

    writer.release()
    print(f"Saved: {output_video}")

create_video("data/View_006", "videos/cam6.mp4")
# create_video("data/View_005", "videos/cam2.mp4")
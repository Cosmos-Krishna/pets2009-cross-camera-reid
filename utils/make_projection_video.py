import cv2
import os

def create_video(image_folder, output_video, fps=5):

    images = sorted([
        img for img in os.listdir(image_folder)
        if img.endswith(".jpg")
    ])

    if not images:
        print("No images found!")
        return

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
    print(f"Frames used: {len(images)}")


create_video(
    "outputs/batch_check",
    "projection_result.mp4",
    fps=3
)
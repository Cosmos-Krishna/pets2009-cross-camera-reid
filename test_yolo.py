from ultralytics import YOLO

VIDEOS = [
    "videos/cam6.mp4",
]

model = YOLO("models/yolov8n.pt")

for video in VIDEOS:

    print(f"Processing {video}")

    model.track(
        source=video,
        classes=[0],          # person only
        conf=0.4,             # ignore weak detections
        save=True,
        persist=True,
        tracker="bytetrack.yaml",

        project="outputs/tracking",
        name="view006",
        exist_ok=True
    )

print("Done!")
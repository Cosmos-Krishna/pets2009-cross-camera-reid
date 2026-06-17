# PETS2009 Cross-Camera Re-Identification POC

## Pipeline

YOLOv8n
→ ByteTrack
→ Homography Calibration
→ Projection
→ Hungarian Matching
→ Failure Analysis

## Results

- Matched: 2292
- Rejected: 195
- Mean Match Error: 29 px
- Median Match Error: 23.4 px

## Tech Stack

- Python
- OpenCV
- NumPy
- SciPy
- Ultralytics YOLOv8
- ByteTrack

## Next Step

ReID embeddings as tie-breaker for ambiguous geometry matches.
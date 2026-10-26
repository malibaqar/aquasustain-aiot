import argparse
from ultralytics import YOLO
if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--weights',required=True);p.add_argument('--video',required=True);a=p.parse_args()
    # Supply a legitimately obtained fish-specific checkpoint; generic weights do not establish fish accuracy.
    model=YOLO(a.weights)
    for result in model.track(source=a.video, tracker='bytetrack.yaml', stream=True):
        print({'detections':len(result.boxes), 'track_ids':None if result.boxes.id is None else result.boxes.id.tolist()})

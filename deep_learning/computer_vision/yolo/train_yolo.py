"""
train_yolo.py

A clean, configurable YOLOv8 training script.
Uses Ultralytics YOLOv8 and a YAML dataset config.

Requirements:
    pip install ultralytics
"""

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train YOLOv8 model")

    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="Base YOLOv8 model (e.g., yolov8n.pt, yolov8s.pt)",
    )
    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to dataset YAML (e.g., data/yolo_dataset.yaml)",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=50,
        help="Number of training epochs",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Image size for training",
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=16,
        help="Batch size",
    )
    parser.add_argument(
        "--project",
        type=str,
        default="runs/train",
        help="Directory to save training runs",
    )
    parser.add_argument(
        "--name",
        type=str,
        default="yolov8_experiment",
        help="Experiment name",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        help="Device: 'cpu', 'cuda', or 'auto'",
    )

    return parser.parse_args()


def validate_paths(model_path: Path, data_path: Path) -> None:
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset YAML not found: {data_path}")


def train_yolo(
    model_path: str,
    data_path: str,
    epochs: int,
    imgsz: int,
    batch: int,
    project: str,
    name: str,
    device: str,
) -> None:
    model_path = Path(model_path)
    data_path = Path(data_path)

    validate_paths(model_path, data_path)

    print(f"[INFO] Loading model: {model_path}")
    model = YOLO(str(model_path))

    print(f"[INFO] Starting training:")
    print(f"       data   = {data_path}")
    print(f"       epochs = {epochs}")
    print(f"       imgsz  = {imgsz}")
    print(f"       batch  = {batch}")
    print(f"       device = {device}")
    print(f"       project= {project}")
    print(f"       name   = {name}")

    model.train(
        data=str(data_path),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        project=project,
        name=name,
        device=device,
    )

    print("[INFO] Training completed.")


def main() -> None:
    args = parse_args()
    train_yolo(
        model_path=args.model,
        data_path=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        project=args.project,
        name=args.name,
        device=args.device,
    )


if __name__ == "__main__":
    main()

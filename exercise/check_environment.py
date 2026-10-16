"""使用中のPythonを表示し、正弦波の図と数値を保存する。"""

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    """実行したフォルダによらず、このリポジトリのoutputs/setupへ保存する。"""
    repository_dir = Path(__file__).resolve().parent.parent
    output_dir = repository_dir / "outputs" / "setup"
    output_dir.mkdir(parents=True, exist_ok=True)

    time_s = np.linspace(0.0, 1.0, 201)
    values = np.sin(2.0 * np.pi * time_s)

    figure, axes = plt.subplots()
    axes.plot(time_s, values)
    axes.set_xlabel("Time [s]")
    axes.set_ylabel("Amplitude")
    axes.set_title("Environment check: 1 Hz sine wave")
    figure.tight_layout()
    figure.savefig(output_dir / "sine.png", dpi=150)
    plt.close(figure)

    np.savetxt(
        output_dir / "sine.csv",
        np.column_stack((time_s, values)),
        delimiter=",",
        header="time_s,value",
        comments="",
    )

    print(f"Python: {sys.executable}")
    print(f"Figure: {output_dir / 'sine.png'}")
    print(f"Values: {output_dir / 'sine.csv'}")
    print("Environment check completed.")


if __name__ == "__main__":
    main()

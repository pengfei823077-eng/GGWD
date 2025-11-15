

## <div align="center">Geometry-aware Gaussian WassersteinDistance for Acne Detection</div>
### Introduction
This is the official repository for our recently submitted paper "Geometry-aware Gaussian WassersteinDistance for Acne Detection", where more implementation details are presented.

### Abstract
Automated detection of skin lesions plays an
important role in interpretative diagnosis and precise treatment of acne vulgaris. However, most existing methods
for acne detection are unaware of the geometry variations
of proposal’s bounding boxes, so as to produce the suboptimal bounding box predictions. To effectively improve
the acne detection performance, a new similarity metric
method, called Geometry-aware Gaussian Wasserstein Distance (GGWD), is proposed in this paper. The novelty of the
proposed GGWD lies on the introduction of geometry properties of bounding boxes into the Gaussian Wasserstein
Distance based similarity metric. For that, the proposed
GGWD first integrates an aspect ration error term to better
measure the geometry deviation between each proposal’s
bounding box and its corresponding ground truth, this
enables detection models that are trained with the GGWDbased losses to be aware of the geometry variations of
bounding boxes. Beyond that, the proposed GGWD also
incorporates a dynamic normalization factor to adaptively
normalize the Gaussian Wasserstein distance according
to the proposals and their corresponding ground truths.
Our proposed GGWD metric can be easily formulated as
the loss functions for training multiple detection models,
including one-stage and two-stage ones. Extensive experiments conducted on two public datasets ROBOflow3.0 and
ACNE04 have demonstrated the effectiveness and superiority of the proposed GGWD metric for acne detection.




Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://www.pepy.tech/projects/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
pip install ultralytics
```

For alternative installation methods including [Conda](https://anaconda.org/conda-forge/ultralytics), [Docker](https://hub.docker.com/r/ultralytics/ultralytics), and Git, please refer to the [Quickstart Guide](https://docs.ultralytics.com/quickstart/).

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ultralytics?logo=condaforge)](https://anaconda.org/conda-forge/ultralytics) [![Docker Image Version](https://img.shields.io/docker/v/ultralytics/ultralytics?sort=semver&logo=docker)](https://hub.docker.com/r/ultralytics/ultralytics) [![Ultralytics Docker Pulls](https://img.shields.io/docker/pulls/ultralytics/ultralytics?logo=docker)](https://hub.docker.com/r/ultralytics/ultralytics)

</details>

<details open>
<summary>Usage</summary>

### CLI

YOLO may be used directly in the Command Line Interface (CLI) with a `yolo` command:

```bash
yolo predict model=yolo11n.pt source='https://ultralytics.com/images/bus.jpg'
```

`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See the YOLO [CLI Docs](https://docs.ultralytics.com/usage/cli/) for examples.

### Python

YOLO may also be used directly in a Python environment, and accepts the same [arguments](https://docs.ultralytics.com/usage/cfg/) as in the CLI example above:

### 1. Prepare the dataset
We have prepared an acne dataset, and its URL is" url:  [ACNE dataset](https://universe.roboflow.com/skripsijerawatviranti/acne_detection_2/dataset/1")

### 2. Train the model
```
train_results = model.train(
    data="acnedata.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
```

### 3. Evaluate model performance on the validation set
```
metrics = model.val()
```

### 4. Perform object detection on an image
```
results = model("path/to/image.jpg")
results[0].show()
```

### 5. Test the model
```
if __name__ == "__main__":
    model = YOLO(r"best.pt") \
    results = model.val(data=r'data.yaml',
                           imgsz=640, split='test')
```


### 6. Results
<details>
<summary><strong>Comparison of detection performance</strong> (click to expand) </summary>
<p align="center"><img src = "image/one stage.png"> </p>
  <p align="center"><img src = "image/two stage.png"> </p>
  <p align="center"><img src = "image/Comparison of performance among different models.png"> </p>
</details>



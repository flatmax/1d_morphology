# Morphological Filters

A Python implementation of simple morphological filters in one dimension.

## Overview

This library provides implementations of fundamental morphological operations:

- **Baseline** - Compute baseline of a signal
- **Dilation** - Morphological dilation operation
- **Erosion** - Morphological erosion operation
- **Opening** - Morphological opening (erosion followed by dilation)
- **Closing** - Morphological closing (dilation followed by erosion)

## Installation

```bash
pip install git+https://github.com/flatmax/1d_morphology.git
```

Or clone the repository and install locally:

```bash
git clone https://github.com/flatmax/1d_morphology.git
cd 1d_morphology
pip install -e .
```

## Usage

```python
from 1d_morphology import baseline, dilation, erosion, opening, closing
```

## Reference

This code is based on the following unpublished work:

> Holmes, W. Harvey. (2020, May 18). *Simple Morphological Filters in One Dimension* [Unpublished manuscript].

See `Morphology.pdf` for the full document.

### BibTeX

```bibtex
@unpublished{holmes2020morphology,
  author = {Holmes, W. Harvey},
  title  = {Simple Morphological Filters in One Dimension},
  year   = {2020},
  month  = {May},
  note   = {Unpublished manuscript}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

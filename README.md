# tvtsplit

[![PyPI - Version](https://img.shields.io/pypi/v/tvtsplit.svg)](https://pypi.org/project/tvtsplit)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tvtsplit.svg)](https://pypi.org/project/tvtsplit)

-----

Split polars DataFrame into training data, validation data and test data.

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install tvtsplit
```

## Usage

```python
import polars as pl
import tvtsplit

params = {"shuffle": False, "seed": 0, "val_size": 0.25, "test_size": 0.25}
sample_df = pl.DataFrame(
    data=["aaa", "bbb", "ccc", "ddd", "eee", "fff"],
    schema=[("txt", pl.String)],
    )
```

```
print(sample_df.tvtsplit.train(params))
shape: (4, 1)
┌─────┐
│ txt │
│ --- │
│ str │
╞═════╡
│ aaa │
│ bbb │
│ ccc │
│ ddd │
└─────┘
```

```
print(sample_df.tvtsplit.val(params))
shape: (1, 1)
┌─────┐
│ txt │
│ --- │
│ str │
╞═════╡
│ eee │
└─────┘
```

```
print(sample_df.tvtsplit.test(params))
shape: (1, 1)
┌─────┐
│ txt │
│ --- │
│ str │
╞═════╡
│ fff │
└─────┘
```

## License

`tvtsplit` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

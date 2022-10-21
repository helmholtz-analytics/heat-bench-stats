# Heat data
This repository contains performance data for the heat library. The performance data hosted in this repository is regularly updated to reflect the latest version of the library via the CI system.

## Benchmarking with Pytest

The purpose of Benchmarking with pytest is to provide a scaling pipeline which can assist in rapid detection of performance degradation in HeAT via a CI/CD system. The basis of this project is based on the three related pilars to performance measurement. The first is that a given benchmark can be represented in a function call, This function call can then be tested against various forms of datasets as parametes using a mature python testing library called pytest.

## Ginko performance explorer

1. Navigate to https://ginkgo-project.github.io/gpe/

2. Copy the data url into "Step 1: Select benchmark results"

Data url: (https://raw.githubusercontent.com/helmholtz-analytics/heat-bench-stats/main/data)

3. Select a benchmark

4. Copy the plot url into "Step 2: Transform results"

Plot url: ( https://raw.githubusercontent.com/helmholtz-analytics/heat-bench-stats/main/plots )

5. Select Plot type from dropdown menu

6. On the right pannel, the data and plots should become available


## run_benchmarks.sh

```python
#calls benchmark for all the pytest encapsulated workloads in folder
pytest --benchmark-json

#Support for passing working directory as flags is being added for manual activation 

run_benchmarks -d 'dirto/localdata-repository'
```

## aggregate.py

```python
#responsible for parsing generated results and create/update aggregate.
#json of the specified benchmark 

python aggregate.py

```

## buildlist.py

```python
#responsible for collecting results location and their names for ginkgo performance explorer

./build-list . > list.json


```

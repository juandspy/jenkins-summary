# Jenkins summary

Generates a Jenkins summary of our jobs in ci.int.

## How to run

Get the data using `python getter.py > results.csv` and convert the data with
`python data-eng.py`. This will generate a `parsed.csv` like:

| name     | min_duration | mean_duration | max_duration | success | num_builds |
|----------|--------------|---------------|--------------|---------|------------|
| test - 1 | 8.78         | 12.15         | 23.25        | 1.0     | 203        |
| test - 2 | 7.29         | 10.51         | 14.31        | 1.0     | 3          |
| test - 3 | 0.16         | 5.23          | 27.29        | 0.27    | 71         |
| test - 4 | 6.09         | 10.04         | 14.38        | 1.0     | 11         |
| test - 5 | 12.34        | 12.34         | 12.34        | 1.0     | 1          |
| test - 6 | 0.3          | 0.3           | 0.3          | 1.0     | 4          |

The duration is shown in minutes.

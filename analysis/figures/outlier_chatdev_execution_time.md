# Visualization Documentation: outlier_chatdev_execution_time.svg

**Visualization Type**: Outlier Run  
**Metric**: execution_time  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T08:51:35.110878Z

---

## Rationale

This Outlier Run visualization was generated to compare Execution Time (seconds) performance across chatdev. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | chatdev |
| Metric | Execution Time (seconds) |
| Total Runs | 100 |
| Outliers Detected | 11 |
| Outlier Rate | 11.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 1039.516 |
| Q3 (75th percentile) | 1313.354 |
| IQR (Q3 - Q1) | 273.838 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 1039.516 |
| Upper Fence | Q3 + 0.0×IQR = 1313.354 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #87 | 2057.135 | Upper | 743.781 (2.72×IQR) |
| Run #81 | 2055.794 | Upper | 742.440 (2.71×IQR) |
| Run #21 | 1963.917 | Upper | 650.563 (2.38×IQR) |
| Run #30 | 1958.809 | Upper | 645.455 (2.36×IQR) |
| Run #27 | 1895.988 | Upper | 582.634 (2.13×IQR) |
| Run #12 | 1892.655 | Upper | 579.301 (2.12×IQR) |
| Run #18 | 1866.884 | Upper | 553.530 (2.02×IQR) |
| Run #5 | 1848.691 | Upper | 535.337 (1.95×IQR) |
| Run #35 | 1758.188 | Upper | 444.834 (1.62×IQR) |
| Run #77 | 600.241 | Lower | 439.275 (1.60×IQR) |
| Run #70 | 1729.177 | Upper | 415.823 (1.52×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for chatdev.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 11/100 runs (11.0%) as outliers for Execution Time (seconds) in chatdev. The most extreme outlier is Run #87 (2057.135), which is 861.922 above the median (1195.212), representing 2.72×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #5, #12, #18, #21, #27 to determine root causes. **Statistical Recommendation**: With 11 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

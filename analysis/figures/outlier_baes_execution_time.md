# Visualization Documentation: outlier_baes_execution_time.svg

**Visualization Type**: Outlier Run  
**Metric**: execution_time  
**Frameworks**: baes  
**Generated**: 2025-11-03T08:51:34.394386Z

---

## Rationale

This Outlier Run visualization was generated to compare Execution Time (seconds) performance across baes. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | baes |
| Metric | Execution Time (seconds) |
| Total Runs | 100 |
| Outliers Detected | 1 |
| Outlier Rate | 1.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 186.652 |
| Q3 (75th percentile) | 225.766 |
| IQR (Q3 - Q1) | 39.114 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 186.652 |
| Upper Fence | Q3 + 0.0×IQR = 225.766 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #81 | 409.449 | Upper | 183.683 (4.70×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for baes.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 1/100 runs (1.0%) as outliers for Execution Time (seconds) in baes. The most extreme outlier is Run #81 (409.449), which is 199.432 above the median (210.017), representing 4.70×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #81 to determine root causes. **Statistical Recommendation**: With 1 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

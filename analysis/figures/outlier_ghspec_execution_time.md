# Visualization Documentation: outlier_ghspec_execution_time.svg

**Visualization Type**: Outlier Run  
**Metric**: execution_time  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T08:51:33.679065Z

---

## Rationale

This Outlier Run visualization was generated to compare Execution Time (seconds) performance across ghspec. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | ghspec |
| Metric | Execution Time (seconds) |
| Total Runs | 100 |
| Outliers Detected | 5 |
| Outlier Rate | 5.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 885.385 |
| Q3 (75th percentile) | 1065.036 |
| IQR (Q3 - Q1) | 179.651 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 885.385 |
| Upper Fence | Q3 + 0.0×IQR = 1065.036 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #83 | 1440.584 | Upper | 375.548 (2.09×IQR) |
| Run #82 | 1410.592 | Upper | 345.556 (1.92×IQR) |
| Run #54 | 572.157 | Lower | 313.228 (1.74×IQR) |
| Run #76 | 592.635 | Lower | 292.750 (1.63×IQR) |
| Run #78 | 1339.496 | Upper | 274.460 (1.53×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for ghspec.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 5/100 runs (5.0%) as outliers for Execution Time (seconds) in ghspec. The most extreme outlier is Run #83 (1440.584), which is 469.475 above the median (971.109), representing 2.09×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #54, #76, #78, #82, #83 to determine root causes. **Statistical Recommendation**: With 5 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

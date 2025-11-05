# Visualization Documentation: outlier_chatdev_total_cost_usd.svg

**Visualization Type**: Outlier Run  
**Metric**: total_cost_usd  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T08:51:41.089011Z

---

## Rationale

This Outlier Run visualization was generated to compare Total Cost (USD) performance across chatdev. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | chatdev |
| Metric | Total Cost (USD) |
| Total Runs | 100 |
| Outliers Detected | 3 |
| Outlier Rate | 3.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 0.046 |
| Q3 (75th percentile) | 0.058 |
| IQR (Q3 - Q1) | 0.012 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 0.046 |
| Upper Fence | Q3 + 0.0×IQR = 0.058 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #81 | 0.090 | Upper | 0.032 (2.64×IQR) |
| Run #27 | 0.077 | Upper | 0.019 (1.59×IQR) |
| Run #21 | 0.077 | Upper | 0.019 (1.57×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for chatdev.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 3/100 runs (3.0%) as outliers for Total Cost (USD) in chatdev. The most extreme outlier is Run #81 (0.090), which is 0.040 above the median (0.050), representing 2.64×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #21, #27, #81 to determine root causes. **Statistical Recommendation**: With 3 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

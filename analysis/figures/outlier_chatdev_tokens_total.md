# Visualization Documentation: outlier_chatdev_tokens_total.svg

**Visualization Type**: Outlier Run  
**Metric**: tokens_total  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T08:51:39.573168Z

---

## Rationale

This Outlier Run visualization was generated to compare Total Tokens (count) performance across chatdev. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | chatdev |
| Metric | Total Tokens (count) |
| Total Runs | 100 |
| Outliers Detected | 3 |
| Outlier Rate | 3.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 181751.250 |
| Q3 (75th percentile) | 225626.500 |
| IQR (Q3 - Q1) | 43875.250 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 181751.250 |
| Upper Fence | Q3 + 0.0×IQR = 225626.500 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #81 | 365531.000 | Upper | 139904.500 (3.19×IQR) |
| Run #27 | 308867.000 | Upper | 83240.500 (1.90×IQR) |
| Run #30 | 308124.000 | Upper | 82497.500 (1.88×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for chatdev.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 3/100 runs (3.0%) as outliers for Total Tokens (count) in chatdev. The most extreme outlier is Run #81 (365531.000), which is 171752.500 above the median (193778.500), representing 3.19×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #27, #30, #81 to determine root causes. **Statistical Recommendation**: With 3 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

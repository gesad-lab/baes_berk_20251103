# Visualization Documentation: outlier_chatdev_tokens_out.svg

**Visualization Type**: Outlier Run  
**Metric**: tokens_out  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T08:51:38.137609Z

---

## Rationale

This Outlier Run visualization was generated to compare Output Tokens (count) performance across chatdev. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | chatdev |
| Metric | Output Tokens (count) |
| Total Runs | 100 |
| Outliers Detected | 6 |
| Outlier Rate | 6.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 43469.250 |
| Q3 (75th percentile) | 54369.500 |
| IQR (Q3 - Q1) | 10900.250 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 43469.250 |
| Upper Fence | Q3 + 0.0×IQR = 54369.500 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #81 | 83436.000 | Upper | 29066.500 (2.67×IQR) |
| Run #21 | 79993.000 | Upper | 25623.500 (2.35×IQR) |
| Run #18 | 75947.000 | Upper | 21577.500 (1.98×IQR) |
| Run #87 | 75288.000 | Upper | 20918.500 (1.92×IQR) |
| Run #27 | 73425.000 | Upper | 19055.500 (1.75×IQR) |
| Run #12 | 73019.000 | Upper | 18649.500 (1.71×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for chatdev.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 6/100 runs (6.0%) as outliers for Output Tokens (count) in chatdev. The most extreme outlier is Run #81 (83436.000), which is 35419.500 above the median (48016.500), representing 2.67×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #12, #18, #21, #27, #81 to determine root causes. **Statistical Recommendation**: With 6 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

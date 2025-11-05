# Visualization Documentation: outlier_ghspec_tokens_out.svg

**Visualization Type**: Outlier Run  
**Metric**: tokens_out  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T08:51:37.419805Z

---

## Rationale

This Outlier Run visualization was generated to compare Output Tokens (count) performance across ghspec. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | ghspec |
| Metric | Output Tokens (count) |
| Total Runs | 100 |
| Outliers Detected | 2 |
| Outlier Rate | 2.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 47675.250 |
| Q3 (75th percentile) | 56534.250 |
| IQR (Q3 - Q1) | 8859.000 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 47675.250 |
| Upper Fence | Q3 + 0.0×IQR = 56534.250 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #82 | 72642.000 | Upper | 16107.750 (1.82×IQR) |
| Run #57 | 70052.000 | Upper | 13517.750 (1.53×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for ghspec.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 2/100 runs (2.0%) as outliers for Output Tokens (count) in ghspec. The most extreme outlier is Run #82 (72642.000), which is 20999.000 above the median (51643.000), representing 1.82×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #57, #82 to determine root causes. **Statistical Recommendation**: With 2 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

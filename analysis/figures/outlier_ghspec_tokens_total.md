# Visualization Documentation: outlier_ghspec_tokens_total.svg

**Visualization Type**: Outlier Run  
**Metric**: tokens_total  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T08:51:38.866302Z

---

## Rationale

This Outlier Run visualization was generated to compare Total Tokens (count) performance across ghspec. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | ghspec |
| Metric | Total Tokens (count) |
| Total Runs | 100 |
| Outliers Detected | 1 |
| Outlier Rate | 1.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 319176.750 |
| Q3 (75th percentile) | 370940.500 |
| IQR (Q3 - Q1) | 51763.750 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 319176.750 |
| Upper Fence | Q3 + 0.0×IQR = 370940.500 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #57 | 464365.000 | Upper | 93424.500 (1.80×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for ghspec.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 1/100 runs (1.0%) as outliers for Total Tokens (count) in ghspec. The most extreme outlier is Run #57 (464365.000), which is 125578.000 above the median (338787.000), representing 1.80×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #57 to determine root causes. **Statistical Recommendation**: With 1 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

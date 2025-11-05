# Visualization Documentation: outlier_chatdev_cached_tokens.svg

**Visualization Type**: Outlier Run  
**Metric**: cached_tokens  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T08:51:32.980198Z

---

## Rationale

This Outlier Run visualization was generated to compare Cached Tokens (count) performance across chatdev. The time series plot identifies specific runs with anomalous behavior for investigation.

**Interpretation Guidance**: Outliers (>1.5×IQR beyond Q3/Q1) require investigation before exclusion. Decision criteria: (1) Data quality issues (crashes, timeouts) → exclude and document. (2) Genuine extreme performance → retain but analyze separately. (3) Single outlier in N>100 runs → likely random, can exclude. (4) Multiple outliers in same direction → systematic issue, must investigate. Domain threshold: For software benchmarks, ±3 standard deviations is stricter criterion for outlier exclusion if you need to identify only catastrophic failures rather than natural variance.

---

## Data

### Data: Outlier Detection Results

#### Summary Statistics

| Statistic | Value |
|-----------|-------|
| Framework | chatdev |
| Metric | Cached Tokens (count) |
| Total Runs | 100 |
| Outliers Detected | 9 |
| Outlier Rate | 9.0% |

#### IQR Calculation Details

| Parameter | Value |
|-----------|-------|
| Q1 (25th percentile) | 5184.000 |
| Q3 (75th percentile) | 12288.000 |
| IQR (Q3 - Q1) | 7104.000 |
| IQR Factor | 0.0× |
| Lower Fence | Q1 - 0.0×IQR = 5184.000 |
| Upper Fence | Q3 + 0.0×IQR = 12288.000 |

*Outliers are values below the lower fence or above the upper fence.*

#### Outlier Run Details

| Run Index | Value | Bound Violated | Distance from Fence |
|-----------|-------|----------------|---------------------|
| Run #30 | 39424.000 | Upper | 27136.000 (3.82×IQR) |
| Run #81 | 31488.000 | Upper | 19200.000 (2.70×IQR) |
| Run #39 | 31104.000 | Upper | 18816.000 (2.65×IQR) |
| Run #19 | 29696.000 | Upper | 17408.000 (2.45×IQR) |
| Run #18 | 29568.000 | Upper | 17280.000 (2.43×IQR) |
| Run #68 | 28416.000 | Upper | 16128.000 (2.27×IQR) |
| Run #11 | 27520.000 | Upper | 15232.000 (2.14×IQR) |
| Run #27 | 26112.000 | Upper | 13824.000 (1.95×IQR) |
| Run #35 | 25728.000 | Upper | 13440.000 (1.89×IQR) |

*Run indices are 0-based. Values can be traced back to source experiment data for chatdev.*


---

## Analysis

### Analysis

Outlier detection using Tukey's method (0.0×IQR criterion) identified 9/100 runs (9.0%) as outliers for Cached Tokens (count) in chatdev. The most extreme outlier is Run #30 (39424.000), which is 31552.000 above the median (7872.000), representing 3.82×IQR from the nearest fence. **Data Quality Implications**: These outlier runs may indicate: (1) genuine performance anomalies worth investigating, (2) environmental variability (system load, I/O contention), or (3) edge cases in the benchmark implementation. Researchers should inspect source logs for Runs #11, #18, #19, #27, #30 to determine root causes. **Statistical Recommendation**: With 9 outlier(s) present, median and IQR are more robust summary statistics than mean and standard deviation. Consider using non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

**Methodology**: Outliers are identified using Tukey's method: values beyond Q1 - 0.0×IQR (lower fence) or Q3 + 0.0×IQR (upper fence) are flagged. This is a standard, conservative approach that balances sensitivity and specificity. 

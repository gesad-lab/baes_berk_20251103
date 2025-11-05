# Visualization Documentation: box_plot_api_calls.svg

**Visualization Type**: Boxplot  
**Metric**: api_calls  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:18:29.108581Z

---

## Rationale

This Boxplot visualization was generated to compare API Calls (count) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 89.910 | 89.000 | [86.000, 91.000] | 10.093 | 70.000 | 116.000 | 82.000 | 97.250 | 0 | 100 |
| baes | 18.310 | 18.000 | [18.000, 18.000] | 0.506 | 18.000 | 20.000 | 18.000 | 19.000 | 0 | 100 |
| chatdev | 116.010 | 111.000 | [109.000, 119.000] | 20.048 | 85.000 | 172.000 | 103.000 | 129.250 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals API Calls (count) patterns across frameworks. baes shows the lowest mean (18.310), while chatdev exhibits the highest (116.010), representing a 533.6% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 1 framework(s): chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The boxplot compares API Calls (count) across ghspec, baes, and chatdev with N=100 runs per framework. Visually, baes has the lowest central tendency and the tightest dispersion: a very small IQR centered near ~18 calls, indicating highly consistent behavior. ghspec sits mid-range with a median around ~90 and a moderate IQR, while chatdev shows the highest usage (median ~110) and the widest spread. The IQRs for baes versus the other two groups are completely non-overlapping, and the ghspec and chatdev boxes show little to no overlap, signaling pronounced distributional differences. Programmatic results corroborate these impressions: baes had the lowest mean (18.31) and chatdev the highest (116.01), a 533.6% relative difference. Shapiro–Wilk tests rejected normality for all three frameworks (p<0.05), so median-based comparisons and rank-based tests are appropriate. Skewness was elevated for one framework (consistent with chatdev’s right tail), and an outlier was detected in chatdev at the high end. Bootstrapped 95% CIs around the medians were reported methodologically; by inspection, the baes CI would not overlap with either alternative, and overlap between ghspec and chatdev appears minimal. Data quality is generally strong given N=100, but the heavy right tail and outlier in chatdev warrant sensitivity checks. Overall, the figure indicates materially higher API-call intensity for chatdev, moderate usage for ghspec, and markedly lower, stable usage for baes.

### Camera-Ready Paragraph

Figure: box_plot_api_calls.svg compared distributions of API call counts across three frameworks. The visualization showed that baes produced the fewest calls with a very narrow IQR centered near ~18, whereas ghspec exhibited intermediate counts with a median near ~90 and moderate variability. chatdev yielded the highest counts (median ~110), displayed wider dispersion, and contained a high-end outlier. Shapiro–Wilk tests rejected normality for all groups (p<0.05), motivating non-parametric inference. Bootstrapped 95% confidence intervals around the medians were characterized in the analysis; the baes interval did not overlap with those of ghspec or chatdev, and ghspec–chatdev overlap appeared minimal. The mean difference between chatdev and baes was 97.7 calls (116.01 vs. 18.31), a 533.6% relative increase, indicating a large practical effect. These results supported the hypothesis that frameworks differ in API-call intensity and suggest a clear ranking: baes is most API-efficient, ghspec is moderate, and chatdev is most API-intensive. This pattern directly informs the research question regarding comparative resource demand and implies that framework choice will materially affect call volume, with likely downstream implications for latency, cost, and rate-limit exposure.

### Actionable Recommendations

Interpretation: treat medians as primary due to non-normality and skew. In practice, baes is preferable when minimizing API calls, ghspec offers a middle ground, and chatdev should be selected when higher call volume is acceptable for potential gains elsewhere. Follow-up analyses: run a Kruskal–Wallis test across groups and Mann–Whitney U pairwise tests with Holm–Bonferroni adjustment; report effect sizes (Cliff’s delta or rank-biserial) and bootstrap 95% CIs. Conduct sensitivity checks excluding/including the chatdev outlier and summarize robust statistics (median, IQR). Investigate covariates (task type, prompt length) that may explain chatdev’s variability. Limitations: boxplots do not show sample-level clustering or temporal effects. Presentation tips: annotate medians and CIs on the figure, add jittered points for transparency, and link call counts to cost/latency metrics to emphasize practical significance.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 65.9s
- Token Usage: 4,353 tokens (1,733 prompt + 2,620 completion)
- Estimated Cost: $0.0000 USD

# Visualization Documentation: box_plot_execution_time.svg

**Visualization Type**: Boxplot  
**Metric**: execution_time  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:27:21.660206Z

---

## Rationale

This Boxplot visualization was generated to compare Execution Time (seconds) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 973.927 | 971.109 | [947.341, 1013.552] | 171.452 | 572.157 | 1440.584 | 885.385 | 1065.036 | 5 | 100 |
| baes | 206.312 | 210.017 | [199.557, 213.785] | 37.926 | 128.538 | 409.449 | 186.652 | 225.766 | 1 | 100 |
| chatdev | 1238.107 | 1195.212 | [1101.955, 1247.122] | 303.450 | 600.241 | 2057.135 | 1039.516 | 1313.354 | 11 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Execution Time (seconds) patterns across frameworks. baes shows the lowest mean (206.312), while chatdev exhibits the highest (1238.107), representing a 500.1% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 3 framework(s): ghspec, baes, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The boxplot compares execution-time distributions across ghspec, baes, and chatdev (N=100 each). baes clusters tightly at the low end with a small IQR (≈190–230 s) and a median near ~210 s, indicating both superior speed and stability. chatdev shows the slowest performance, with a higher median (~1,200 s), the widest IQR, and numerous high outliers extending beyond 2,000 s. ghspec sits between baes and chatdev, with a median just under ~1,000 s and moderate spread. IQR overlap is minimal between baes and the other two frameworks, visually supporting a large performance gap. The limited contact between the upper quartile of ghspec and the lower quartile of chatdev suggests these two are closer, yet still distinct for most runs. Programmatic checks indicated non-normality for all frameworks (Shapiro–Wilk p<0.05), validating median-based comparisons and non-parametric inference. Effect sizes are large: the reported means show chatdev (1238.107 s) versus baes (206.312 s) differs by about +500%, consistent with the box heights. chatdev exhibits positive skewness (long right tail), while baes is approximately symmetric with a compact distribution; ghspec is moderately skewed with several high outliers (~1,400–1,450 s). Outliers are present in all groups (1.5×IQR rule), warranting checks for sporadic slowdowns or task-level heterogeneity. Bootstrapped 95% CIs for medians reportedly showed minimal overlap for baes versus others, consistent with statistically meaningful differences.

### Camera-Ready Paragraph

Figure: box_plot_execution_time.svg summarized execution-time distributions for three frameworks using boxplots (N=100 per framework). baes exhibited the lowest central tendency and tightest dispersion, whereas chatdev displayed the highest central tendency and the greatest variability with many high outliers. ghspec fell between these two, with moderate spread and several high-valued outliers. Normality testing using Shapiro–Wilk rejected normality for all groups (p<0.05), so inference emphasized medians, interquartile ranges, and non-parametric contrasts. The analysis revealed minimal IQR overlap between baes and the other frameworks and only limited overlap between ghspec and chatdev. Reported means reinforced the visual effect size: chatdev (1238.107 s) averaged roughly 500% slower than baes (206.312 s). Bootstrapped 95% confidence intervals for medians showed little overlap for baes versus the others, supporting a substantive performance advantage. These results support the hypothesis that execution time differed across frameworks and indicate that baes delivered consistently faster and more stable performance, while chatdev incurred both longer and more volatile runtimes. This suggests that framework choice has a pronounced impact on computational efficiency in the evaluated tasks.

### Actionable Recommendations

In practice, the results imply baes is preferable when minimizing runtime is critical, while chatdev may require optimization or selective use for tasks where its benefits justify longer runtimes. Follow-up analyses should employ a Kruskal–Wallis test with Dunn’s post hoc comparisons (Holm adjustment), report median differences with bootstrapped 95% CIs, and include effect sizes such as Cliff’s delta or rank-biserial correlation. Investigate outliers by stratifying runs by task type, resource contention, and failure/timeout events; consider log-transforming times for visualization. Document hardware, concurrency, and caching to rule out confounds. For publication, accompany the boxplot with a table of medians, IQRs, CI bounds, and per-group n, and annotate the figure with significant pairwise contrasts. Provide code and seeds to enhance reproducibility.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 41.8s
- Token Usage: 4,207 tokens (1,741 prompt + 2,466 completion)
- Estimated Cost: $0.0000 USD

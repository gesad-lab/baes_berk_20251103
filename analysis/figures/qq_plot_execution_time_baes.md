# Visualization Documentation: qq_plot_execution_time_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: execution_time  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:30:19.692828Z

---

## Rationale

This Qq Plot visualization was generated to compare Execution Time (seconds) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 206.312 | 210.017 | [199.557, 213.785] | 37.926 | 128.538 | 409.449 | 186.652 | 225.766 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Execution Time (seconds) patterns across frameworks. baes shows the lowest mean (206.312), while baes exhibits the highest (206.312), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 1 framework(s): baes. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for baes compares sample execution-time quantiles to a theoretical normal distribution. The middle quantiles aligned reasonably with the 45° reference line, indicating that the central bulk of runs behaved approximately Gaussian. However, pronounced departures appeared in the upper tail: points curved above the line beginning around the 75th–85th percentile and culminated in a single extreme outlier near 410 s. The lower tail showed milder deviations below the line. Together, these patterns indicated positive skew and heavy right tails. The embedded Shapiro–Wilk test reported p < 0.001, providing strong evidence against normality at α = 0.05. With N = 100 runs, the Central Limit Theorem may temper modest non-normality, but the severe upper-tail divergence and outlier imply that mean-based inference could be biased and confidence intervals overly optimistic. Visual evidence suggested that the mean is pulled upward relative to the median, consistent with the programmatic detection of high skewness and outliers. Data-quality considerations include the possibility of sporadic slowdowns (e.g., system contention or workload heterogeneity) producing the >100 s gap between the largest observation and the theoretical normal line. No missingness was apparent, but tail behavior argues for robust summaries (median, IQR) and non-parametric hypothesis tests. If cross-framework comparisons are planned, heteroscedasticity checks (e.g., Levene’s test) are advisable given the heavy-tail behavior.

### Camera-Ready Paragraph

Figure: qq_plot_execution_time_baes.svg depicted the distributional shape of execution times for baes. The central quantiles were approximately linear; however, the upper tail departed markedly from normality and contained a prominent outlier (~410 s), with the observed value exceeding the reference-line expectation by over 100 s. The Shapiro–Wilk test indicated a significant violation of normality (p < 0.001, α = 0.05). These results suggested a positively skewed distribution with heavy right tails, implying that occasional long-running executions occur. For N = 100 runs, minor deviations would be tolerable, but the magnitude of tail divergence and the extreme observation challenged the normality assumption underlying parametric mean comparisons. Consequently, the figure supported the use of robust estimators (median, IQR) and non-parametric or robust tests in subsequent cross-framework analyses. In the context of the research questions on execution-time performance, the visualization challenged any hypothesis of approximate normality for baes and indicated that inference should focus on median behavior and robust effect sizes (e.g., Cliff’s delta) rather than means, as the latter may be unduly influenced by rare but severe slowdowns.

### Actionable Recommendations

Interpret execution-time performance using robust summaries: report median, IQR, and bootstrap 95% CIs. For inference, prefer Mann–Whitney U (two groups) or Kruskal–Wallis (multi-group), and complement with robust effect sizes (Cliff’s delta or median differences with CIs). Investigate the extreme outlier: review logs for resource contention, caching anomalies, or workload shifts; if justified, analyze with and without the point or apply trimming/winsorization. Consider variance-stabilizing transforms (log or Box–Cox) and model-based alternatives tailored to skewed times (log-normal or Gamma GLMs). Check heteroscedasticity (Levene/Brown–Forsythe) before any parametric comparisons. For publication, accompany the Q–Q plot with density/violin plots and a table of robust statistics, clearly stating the Shapiro–Wilk p-value (p < 0.001) and the chosen analysis pathway to ensure transparency and reproducibility.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 45.1s
- Token Usage: 4,063 tokens (1,747 prompt + 2,316 completion)
- Estimated Cost: $0.0000 USD

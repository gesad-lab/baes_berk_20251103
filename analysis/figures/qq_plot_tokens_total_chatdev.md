# Visualization Documentation: qq_plot_tokens_total_chatdev.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_total  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T11:43:15.363237Z

---

## Rationale

This Qq Plot visualization was generated to compare Total Tokens (count) performance across chatdev. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| chatdev | 205467.960 | 193778.500 | [186545.000, 201611.000] | 41986.351 | 139789.000 | 365531.000 | 181751.250 | 225626.500 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Total Tokens (count) patterns across frameworks. chatdev shows the lowest mean (205467.960), while chatdev exhibits the highest (205467.960), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Total Tokens (count) in chatdev displays a clear right‑tail departure from normality. Points track the 45° reference line through the central quantiles but curve upward markedly in the upper quartile, culminating in several extreme points well above the line. This pattern is consistent with positive skew and heavy tails. The embedded Shapiro–Wilk test reports p < 0.001 (α = 0.05), rejecting the normality assumption. Programmatic diagnostics further indicate high skewness (|skew| > 1), corroborating that the mean is not a reliable measure of central tendency; the median is preferable. Outliers are evident at the highest quantiles (≈300k–360k tokens), suggesting occasional runs with unusually high token usage. With N = 100 runs, the Central Limit Theorem does not alleviate the pronounced non‑normality for inference on raw counts. These findings imply that parametric tests assuming normal residuals (e.g., t‑tests/ANOVA) would be inappropriate without transformation. Robust or non‑parametric approaches (Mann–Whitney U, Kruskal–Wallis) and median-based summaries with bootstrap 95% confidence intervals are advisable. No missingness is visible, but tail inflation and leverage from high-end outliers raise concerns about effect-size stability. Reporting robust effect sizes (e.g., Cliff’s delta or Hodges–Lehmann estimator) would better reflect distributional asymmetry than Cohen’s d under these conditions.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_total_chatdev.svg visualized the distributional conformity of Total Tokens (count) for chatdev using a Q–Q plot against the normal distribution. The sample quantiles aligned with the reference line across central values but diverged upward in the upper tail, indicating positive skew and heavy-tailed behavior. A Shapiro–Wilk test embedded in the figure yielded p < 0.001 (α = 0.05), which rejected normality for N = 100 runs. Programmatic diagnostics reported high skewness (|skew| > 1) and the presence of outliers at the highest quantiles. Together, these results challenged the hypothesis that token counts are approximately normal and suitable for parametric inference on raw data. The pattern suggests that a minority of runs consumed substantially more tokens than typical runs, inflating means and standard deviations. This implies that central tendency should be summarized by the median with bootstrap 95% confidence intervals, and hypothesis testing should rely on robust or non‑parametric procedures. The visualization therefore supports the research objective of assessing distributional assumptions by demonstrating a clear violation of normality and highlighting the need for methods resilient to skewness and outliers.

### Actionable Recommendations

In practice, interpret central tendency with medians and dispersion with IQR or MAD, not means/SDs. For group comparisons, use Mann–Whitney U or Kruskal–Wallis; report robust effect sizes (Cliff’s delta, Hodges–Lehmann shift) with bootstrap 95% CIs. Consider variance‑stabilizing transforms (log or Box–Cox) and re‑assess normality; if transformed data satisfy assumptions, parametric models may be revisited. Conduct sensitivity analyses excluding high-end outliers and compare with robust estimators (trimmed mean, Huber M‑estimator). When modeling, prefer quantile regression or GLMs with appropriate families (e.g., Gamma/log-link) for skewed counts. For publication, present both the Q–Q plot and complementary density/violin plots, explicitly state Shapiro–Wilk p < 0.001 and skewness |skew| > 1, and justify the chosen inferential approach in light of these diagnostics.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 41.5s
- Token Usage: 3,631 tokens (1,749 prompt + 1,882 completion)
- Estimated Cost: $0.0000 USD

# Visualization Documentation: qq_plot_tokens_in_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_in  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:33:59.331512Z

---

## Rationale

This Qq Plot visualization was generated to compare Input Tokens (count) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 294720.580 | 288673.500 | [280733.500, 301019.000] | 32567.513 | 234785.000 | 394313.000 | 269970.750 | 315616.000 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Input Tokens (count) patterns across frameworks. ghspec shows the lowest mean (294720.580), while ghspec exhibits the highest (294720.580), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Outliers**: Detected in 1 framework(s): ghspec. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot of Input Tokens (count) for ghspec compares sample quantiles against a theoretical normal distribution. Most observations in the central region (approximately −1 to +1 theoretical quantiles) lie close to the reference line, indicating approximate normality around the median. However, the extremes deviate systematically. The right tail bends above the line starting near the 80th percentile and culminates in a pronounced outlier around ~3 SDs, signaling a heavier-than-normal upper tail and mild positive skew. The left tail sits slightly above the line, suggesting a comparatively light lower tail. The embedded Shapiro–Wilk test reported p = 0.032 (N ≈ 100), which rejects normality at α = 0.05. While the deviation is modest, significance indicates that parametric procedures relying on strict normality (e.g., t-tests/ANOVA) could be sensitive to these tail behaviors and to the observed high-end outliers. Data quality concerns are limited to tail behavior and a small number of extreme points; no gross artifacts or missingness are visible. For inference on central tendency and dispersion, robust summaries (median, IQR) and bootstrap confidence intervals are advisable. If between-framework comparisons are planned, non-parametric or robust methods are preferable, or a variance-stabilizing transform (e.g., log1p) can be applied to mitigate skew and reduce the influence of outliers.

### Camera-Ready Paragraph

The Q–Q analysis of input-token counts for ghspec (Figure: qq_plot_tokens_in_ghspec.svg) revealed that mid-quantiles were approximately linear with the theoretical normal, whereas the upper tail departed upward from the reference line and contained one or more high-end outliers. The left tail lay slightly above the line, indicating a lighter-than-normal lower tail. A Shapiro–Wilk test confirmed a statistically significant deviation from normality (p = 0.032, N = 100). These results indicated mild positive skew with a heavier right tail. Consequently, the normality assumption required for mean-based parametric comparisons was not fully satisfied. This suggests that subsequent hypothesis tests comparing token counts should employ robust or non-parametric approaches, or apply a variance-stabilizing transformation prior to parametric modeling. In relation to the research questions on comparing input-token usage across frameworks, the figure challenged the use of unadjusted t-tests/ANOVA and supported analyses that emphasize medians, ranks, or trimmed means with bootstrap confidence intervals. The observed deviations were localized primarily to the extreme quantiles, implying that central tendency comparisons may be similar across methods, but tail-sensitive metrics and standard errors could be biased under normal-theory procedures.

### Actionable Recommendations

In practice, treat the distribution as mildly right-skewed with influential upper-tail observations. Before between-framework inference, consider log1p transformation and re-assess normality; alternatively, proceed with rank-based tests (Mann–Whitney U/Kruskal–Wallis) and report robust effect sizes (Cliff’s delta, Hodges–Lehmann median difference) with bootstrap 95% CIs. Conduct sensitivity analyses excluding or winsorizing extreme high values to gauge robustness. If parametric models are essential, use heteroskedasticity-robust SEs or trimmed/Welch procedures. Document the N and the Shapiro–Wilk outcome (p = 0.032) alongside descriptive quantiles. For publication, accompany the Q–Q plot with a histogram/density plot and a table of robust summaries (median, IQR), and consider adding simulated confidence bands around the Q–Q line to visually convey uncertainty.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 54.0s
- Token Usage: 4,550 tokens (1,674 prompt + 2,876 completion)
- Estimated Cost: $0.0000 USD

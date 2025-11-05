# Visualization Documentation: qq_plot_cached_tokens_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: cached_tokens  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:24:43.961646Z

---

## Rationale

This Qq Plot visualization was generated to compare Cached Tokens (count) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 149184.000 | 147008.000 | [140160.000, 154496.000] | 20169.201 | 113920.000 | 201600.000 | 133728.000 | 160992.000 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Cached Tokens (count) patterns across frameworks. ghspec shows the lowest mean (149184.000), while ghspec exhibits the highest (149184.000), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for Cached Tokens (count) under ghspec shows a predominantly linear alignment through the mid-quantiles, indicating approximate normal behavior in the center of the distribution. However, both tails deviate from the reference line, with the upper tail bending upward more strongly. Several high-leverage observations around 195k–202k tokens lie above the line, consistent with a heavier-than-normal right tail and mild positive skew. The Shapiro–Wilk test embedded in the figure reports p = 0.022, which rejects normality at α = 0.05 and corroborates the visual diagnosis. With N ≈ 100 runs, minor central deviations would be tolerable, but the systematic tail departures suggest that parametric tests assuming normal residuals may be sensitive to outliers and inflated Type I error. No obvious gaps or missing segments are visible, and the point density appears uniform across quantiles, reducing concern about incomplete sampling. Data quality concerns center on the extreme upper-tail points; whether they reflect genuine bursty caching behavior or instrumentation artifacts should be verified. Inference should emphasize robust location (median) and dispersion (IQR) with bootstrap 95% CIs. For hypothesis tests comparing frameworks or conditions, non-parametric alternatives (Mann–Whitney U or Kruskal–Wallis) or robust estimators (trimmed means/Winsorization) are preferable. If parametric modeling is required, transformation (e.g., log or Box–Cox) could mitigate skew and stabilize variance.

### Camera-Ready Paragraph

Figure: qq_plot_cached_tokens_ghspec.svg summarized the distributional diagnostics for Cached Tokens (count) under the ghspec framework. The sample quantiles followed the theoretical normal line closely in the central region but diverged systematically in the tails, with a pronounced upward deviation in the upper tail. The embedded Shapiro–Wilk test yielded p = 0.022, providing statistical evidence against normality at α = 0.05. These results indicated mild positive skew and heavier right-tail behavior, driven by several high-leverage observations near 200k tokens. This suggests that analyses relying on normality (e.g., t-tests or ordinary least-squares models without robust adjustments) may be vulnerable to outlier influence. For addressing the research question on cached-token performance, the visualization supported the use of robust or non-parametric procedures and the reporting of median and IQR with bootstrap confidence intervals rather than mean and standard deviation alone. The observed departures from normality challenge the hypothesis of approximately Gaussian token counts for ghspec and motivate either distribution-free comparisons across frameworks or variance-stabilizing transformations prior to parametric modeling.

### Actionable Recommendations

Interpret cached-token results using robust summaries (median, IQR) and bootstrap 95% CIs, given the Shapiro–Wilk p = 0.022 and visible upper-tail inflation. For between-framework comparisons, prefer Mann–Whitney U or Kruskal–Wallis and supplement with effect sizes based on ranks or trimmed means. Investigate the extreme observations (~200k tokens): confirm measurement integrity, assess temporal clustering, and evaluate influence via leave-one-out or robust regression. Consider transformations (log, Box–Cox) to stabilize tails if parametric models are desired; validate with post-transform Q–Q plots and residual checks. Report sensitivity analyses comparing parametric and robust methods. In publication, cite both visual evidence and p-values, annotate figures with sample size, and standardize axes across frameworks to aid comparability.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 53.2s
- Token Usage: 4,116 tokens (1,587 prompt + 2,529 completion)
- Estimated Cost: $0.0000 USD

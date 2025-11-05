# Visualization Documentation: qq_plot_tokens_out_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_out  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:39:04.818465Z

---

## Rationale

This Qq Plot visualization was generated to compare Output Tokens (count) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 9372.010 | 9031.500 | [9023.000, 9046.500] | 576.600 | 8953.000 | 11281.000 | 9010.500 | 10138.500 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Output Tokens (count) patterns across frameworks. baes shows the lowest mean (9372.010), while baes exhibits the highest (9372.010), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for Output Tokens (count) under the baes framework shows pronounced departures from normality. Points do not track the diagonal; instead, they form two distinct, nearly horizontal bands—one around ~9.0–9.1k tokens and a higher band near ~10.1–10.2k—separated by a visible gap. This banding indicates potential bimodality or a mixture of regimes rather than a single Gaussian process. The right tail bends sharply above the reference line, with two extreme observations near ~11.2k tokens, signaling heavy right-tail behavior and positive skew. The embedded Shapiro–Wilk test reported p < 0.001, rejecting the null of normality at α = 0.05. Programmatic diagnostics further suggested large skewness (|skew| > 1), implying the mean is not a robust central tendency. For N ≈ 100 observations, these systematic deviations are substantive and not minor sampling noise. Data quality considerations include: (i) possible ceiling or configuration effects (e.g., changes in max_tokens) producing the two modes; (ii) substantial value ties consistent with discretized counts; and (iii) influential high-end outliers that may reflect atypical prompts or instrumentation artifacts. Taken together, the visualization argues against parametric assumptions for hypothesis tests or interval estimation and favors median/IQR summaries, bootstrap confidence intervals, and rank- or quantile-based inference.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_out_baes.svg visualized the normal quantile–quantile relationship for Output Tokens (count) under the baes framework. The sample quantiles did not align with the theoretical normal line; instead, they exhibited two banded clusters (≈9.0–9.1k and ≈10.1–10.2k tokens) and a pronounced upward divergence in the upper tail with a few extreme values (~11.2k tokens). A Shapiro–Wilk test annotated on the figure yielded p < 0.001, rejecting normality at α = 0.05, and ancillary diagnostics indicated large positive skewness (|skew| > 1). These results challenged the assumption of Gaussian errors underlying parametric comparisons and suggested a heterogeneous or mixture-generating process for output length. The implications are that central-tendency estimates based on the mean are unstable, and parametric t-tests/ANOVA are not appropriate. For addressing the research question on performance comparisons, robust alternatives are preferable: median-based summaries with bootstrap 95% confidence intervals, rank-based tests (Mann–Whitney U/Kruskal–Wallis), or trimmed/quantile methods. The figure thus supported the hypothesis that output-token distributions deviate materially from normality and indicates that subsequent analyses should account for heavy tails, outliers, and potential bimodality.

### Actionable Recommendations

Interpret results using robust statistics: report medians, IQRs, and bootstrap 95% CIs; accompany group comparisons with Mann–Whitney U (pairwise) or Kruskal–Wallis (multi-group) and effect sizes such as Cliff’s delta. Examine the apparent bimodality via mixture modeling or clustering and by conditioning on covariates (prompt category, temperature, max_tokens settings, caching). Treat the two extreme high-end points explicitly: verify data provenance, rerun without them, and consider trimmed means or Huber/quantile regression for modeling. If transformation is desired, assess log or Box–Cox; however, mixture structure may persist post-transform. For publication, present the Q–Q plot alongside a histogram/density and a table of robust estimates and CIs. Predefine non-parametric analysis in the methods, justify it with p < 0.001 from Shapiro–Wilk, and include sensitivity analyses with and without outliers.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 44.5s
- Token Usage: 4,388 tokens (1,663 prompt + 2,725 completion)
- Estimated Cost: $0.0000 USD

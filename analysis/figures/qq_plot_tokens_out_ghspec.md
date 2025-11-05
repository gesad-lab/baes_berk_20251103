# Visualization Documentation: qq_plot_tokens_out_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_out  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:38:15.337465Z

---

## Rationale

This Qq Plot visualization was generated to compare Output Tokens (count) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 52490.180 | 51643.000 | [50609.000, 53956.000] | 6351.669 | 38737.000 | 72642.000 | 47675.250 | 56534.250 | 2 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Output Tokens (count) patterns across frameworks. ghspec shows the lowest mean (52490.180), while ghspec exhibits the highest (52490.180), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Output Tokens (count) under the ghspec framework shows strong adherence to the theoretical normal line across the central quantiles, indicating that the bulk of observations are approximately normally distributed. The Shapiro–Wilk test embedded in the figure reported p = 0.142 (α = 0.05), so normality was not rejected. Visual deviations occur primarily in the extreme right tail, where several points rise above the reference line (≈70k–73k tokens), suggesting a heavier-than-normal upper tail and mild positive skew. The left tail exhibits only slight departure. Such tail behavior implies occasional runs with unusually long outputs that inflate variance while leaving the central tendency largely unaffected. The displayed range spans roughly 38k–73k tokens, with a dense, linear middle segment that supports parametric modeling for mean comparisons if sample sizes are moderate to large. Data quality appears high with no evidence of missingness; however, the few high-end observations function as potential outliers and could exert leverage in mean-based inference. While the p-value supports normality, tail deviations warrant robustness checks (e.g., trimmed means, bootstrap CIs) because parametric tests are sensitive to heavy tails, especially for variance-related hypotheses. Overall, the visualization indicates near-normal behavior with a small set of influential high-count runs that may merit separate investigation.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_out_ghspec.svg presented a Q–Q analysis of Output Tokens (count) for the ghspec framework. The points closely followed the theoretical normal reference line across the central quantiles, and the Shapiro–Wilk test yielded p = 0.142, indicating that normality was not rejected at α = 0.05. Modest departures were observed in the upper tail, where several observations around 70k–73k tokens deviated upward, consistent with a heavier right tail and mild positive skew. These results suggested that the distribution was approximately normal in its core, with a small number of unusually long generations contributing to tail heaviness. Consequently, the normality assumption underlying mean-based parametric comparisons is broadly tenable for ghspec, particularly with N ≈ 100, although tail-sensitive inferences (e.g., variance tests) may be affected. In relation to the research question about distributional adequacy for parametric testing, the figure supported the hypothesis of near-normality while highlighting rare but influential outliers. This implies that standard t-tests or ANOVA can be applied, complemented by robustness checks or bootstrap intervals to ensure conclusions are not driven by extreme observations.

### Actionable Recommendations

In practice, proceed with parametric analyses of mean output tokens for ghspec, but include sensitivity checks. Report both parametric estimates and robust alternatives: trimmed means, Huber M-estimators, or Mann–Whitney tests as confirmations. Provide bootstrap 95% confidence intervals to mitigate tail effects. Examine leverage of the few high-end runs; consider winsorizing or modeling with a log or Yeo–Johnson transform if variance heterogeneity emerges. If comparing frameworks, assess homoscedasticity (e.g., Levene’s test) and inspect Q–Q plots of residuals rather than raw values. Document the Shapiro–Wilk result (p = 0.142) alongside diagnostics, and interpret occasional long generations as rare events that may inflate variance but not central tendency. For publication, include the Q–Q plot, a table of summary statistics, and a brief sensitivity-analysis appendix.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 49.4s
- Token Usage: 4,136 tokens (1,674 prompt + 2,462 completion)
- Estimated Cost: $0.0000 USD

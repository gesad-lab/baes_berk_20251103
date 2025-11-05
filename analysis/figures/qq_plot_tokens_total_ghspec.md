# Visualization Documentation: qq_plot_tokens_total_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_total  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:41:48.530359Z

---

## Rationale

This Qq Plot visualization was generated to compare Total Tokens (count) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 347210.760 | 338787.000 | [332269.000, 356658.000] | 38116.260 | 274758.000 | 464365.000 | 319176.750 | 370940.500 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Total Tokens (count) patterns across frameworks. ghspec shows the lowest mean (347210.760), while ghspec exhibits the highest (347210.760), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Total Tokens (count) in the ghspec framework shows points that align closely with the 45° reference line over the central quantiles, indicating approximate normality in the bulk of the data. The most notable deviations occur in the upper tail (theoretical quantiles > ~1.5), where several observations fall above the line, suggesting a slightly heavier right tail or a few high-end observations with greater token counts than a perfect Gaussian would predict. The left tail exhibits only mild departures. The embedded Shapiro–Wilk test reported p = 0.051, which is marginally above the α = 0.05 threshold; thus, normality cannot be rejected, but the result is borderline. No confidence bands are shown, so the uncertainty around tail deviations is not visually quantified, and effect sizes are not provided in this figure. Data quality appears generally strong, with a dense, monotone progression and no gaps suggestive of missing data; however, the handful of large values may exert leverage on parametric estimates of variance and confidence intervals. Practically, mean- and SD-based summaries are defensible, yet researchers should be attentive to sensitivity: trimming or robust estimators may stabilize inference if those high-end points materially affect results. Overall, the plot supports near-normal behavior with mild right-tail heaviness rather than systematic skew across the full distribution.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_total_ghspec.svg evaluated the normality of Total Tokens (count) for ghspec. The sample quantiles closely followed the theoretical normal quantiles across the central range, with modest upward deviations at the upper tail. A Shapiro–Wilk test yielded p = 0.051, placing the evidence against normality just above the conventional α = 0.05 threshold. Thus, normality was not rejected, although the result was borderline. The pattern indicated approximate Gaussian behavior with a slightly heavier right tail, consistent with a few high-count runs. This supports the use of parametric procedures (e.g., t-based confidence intervals or ANOVA) for group comparisons involving ghspec, while recommending sensitivity checks for tail influence. In relation to the research questions on performance distributional assumptions, the visualization provided affirmative, yet cautious, support: the central tendency and spread appear adequately modeled by a normal distribution, but extreme observations may inflate variance estimates. Consequently, conclusions that rely on parametric inference are likely valid, whereas estimates of uncertainty could benefit from robust or bootstrap approaches to account for the mild tail departures.

### Actionable Recommendations

Interpret the distribution as approximately normal with minor right-tail heaviness. Proceed with parametric analyses (e.g., Welch’s t-test/ANOVA) but run sensitivity checks: (1) re-estimate effects using robust methods (trimmed means, Huber M-estimators) and nonparametric tests (Mann–Whitney or Kruskal–Wallis) to confirm conclusions; (2) assess outlier influence via leverage/DFBETAs and 1.5×IQR rules; and (3) consider log or Box–Cox transformations if variance stabilization is desired. Report effect sizes (Cohen’s d or Hedges’ g; Cliff’s delta for nonparametric) with 95% CIs, ideally via bootstrap to accommodate tail behavior. For publication, add Q–Q confidence bands and annotate sample size to contextualize tail deviations. Predefine α and multiple-comparison controls, and include both parametric and robust estimates in the supplement to demonstrate result stability.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 43.5s
- Token Usage: 3,886 tokens (1,674 prompt + 2,212 completion)
- Estimated Cost: $0.0000 USD

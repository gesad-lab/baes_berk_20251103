# Visualization Documentation: qq_plot_cached_tokens_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: cached_tokens  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:25:37.278319Z

---

## Rationale

This Qq Plot visualization was generated to compare Cached Tokens (count) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 69.120 | 0.000 | [0.000, 0.000] | 402.895 | 0.000 | 2688.000 | 0.000 | 0.000 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Cached Tokens (count) patterns across frameworks. baes shows the lowest mean (69.120), while baes exhibits the highest (69.120), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Cached Tokens (count) in the baes framework shows a pronounced departure from normality. Most sample quantiles lie clustered near zero across a broad span of theoretical quantiles, while a handful of observations rise sharply into the thousands, producing a strongly positively skewed, heavy‑tailed pattern. Points deviate substantially from the reference diagonal and diverge at the upper tail, indicating extreme outliers. The embedded Shapiro–Wilk test reports p < 0.001, confirming non‑normality at α = 0.05. This implies that parametric procedures relying on normal errors (t‑tests/ANOVA) and mean-based summaries are not appropriate. The programmatic diagnostics align with the visual evidence: high skewness (|skew| > 1), outliers by the 1.5×IQR rule, and a distribution better summarized by the median and IQR than by the mean. The pattern suggests zero inflation (frequent zero or near‑zero counts) with rare bursts of very high cached‑token activity. Potential data‑quality considerations include censoring near zero, mixture processes (e.g., distinct operation modes), or logging inconsistencies that could generate the extreme upper tail. Confidence intervals are not shown on the plot; bootstrap 95% CIs for the median or quantiles would provide more reliable uncertainty estimates. Effect sizes should rely on robust, rank‑based metrics (e.g., Cliff’s delta) rather than Cohen’s d in this context.

### Camera-Ready Paragraph

Figure: qq_plot_cached_tokens_baes.svg presented a Q–Q plot of Cached Tokens (count) for the baes framework and revealed a severe deviation from normality. Observations were predominantly concentrated near zero, with a small number of extreme values exceeding approximately 2.6k tokens. Points diverged markedly from the reference line at the upper tail, and the embedded Shapiro–Wilk test indicated p < 0.001, confirming non‑normality at α = 0.05. Outliers were detected under the 1.5×IQR criterion, and programmatic diagnostics reported high skewness (|skew| > 1). As a consequence, the mean (≈69.12) was not representative of central tendency; the median and IQR were more appropriate summaries. These results challenged the assumption of normally distributed errors that underpins parametric inference and suggested that robust or non‑parametric approaches are required. In the context of the research questions on cached‑token behavior, the figure implied a zero‑inflated and heavy‑tailed process, where most runs generated few or no cached tokens but occasional runs produced very large counts. This suggests that comparisons across frameworks or conditions should rely on rank‑based tests and median differences, supplemented by bootstrap confidence intervals for quantiles.

### Actionable Recommendations

In practice, interpret central tendency via the median and dispersion via IQR or MAD; avoid relying on the mean. For hypothesis testing across conditions/frameworks, use Mann–Whitney U (two groups) or Kruskal–Wallis (k groups), and report robust effect sizes (Cliff’s delta or rank‑biserial) with bootstrap 95% CIs. Consider models tailored to counts and zero inflation (hurdle or zero‑inflated Poisson/negative binomial) if explanatory modeling is needed. For visualization, complement the Q–Q plot with empirical CDFs and violin/box plots on a log1p scale to show the heavy tail without masking zeros. Conduct sensitivity analyses with and without extreme runs (or winsorized) and document the rationale. Verify measurement integrity (e.g., logging thresholds, mixed modes) that could create rare spikes. Clearly state assumption checks and justify the chosen robust methods in the manuscript.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 58.3s
- Token Usage: 4,333 tokens (1,747 prompt + 2,586 completion)
- Estimated Cost: $0.0000 USD

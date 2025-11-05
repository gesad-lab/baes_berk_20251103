# Visualization Documentation: qq_plot_tokens_in_chatdev.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_in  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T11:35:49.041123Z

---

## Rationale

This Qq Plot visualization was generated to compare Input Tokens (count) performance across chatdev. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| chatdev | 154917.440 | 146999.500 | [141594.000, 153324.000] | 32749.365 | 102986.000 | 282095.000 | 135513.750 | 173201.750 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Input Tokens (count) patterns across frameworks. chatdev shows the lowest mean (154917.440), while chatdev exhibits the highest (154917.440), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Input Tokens (count) in chatdev shows substantial departure from normality. While mid-quantiles track the reference line moderately well, both tails deviate strongly. The upper tail sits far above the 45° line, indicating a heavy right tail and positive skew; several extreme points exceed ~240k–280k tokens, consistent with outlier behavior. The lower tail exhibits milder deviation. An embedded Shapiro–Wilk test reports p < 0.001, decisively rejecting normality at α = 0.05. Programmatic diagnostics corroborate this: skewness magnitude exceeded |1.0| and outliers were detected via the 1.5×IQR rule. With N = 100 runs, the Central Limit Theorem would tolerate small deviations, but the systematic S-shaped curvature and extreme upper-tail divergence indicate severe violations. Consequently, the mean (~154,917 tokens) is likely upward-biased relative to the central tendency; the median would better represent typical usage. For inference, non-parametric or robust methods (e.g., Mann–Whitney U, Kruskal–Wallis, median-based effect sizes, or trimmed means) are preferable to t-tests/ANOVA. Bootstrapped 95% confidence intervals should be reported for location estimates, as they do not assume normality. Data quality concerns center on high-leverage observations in the right tail; sensitivity analyses with outlier trimming or Winsorization are warranted to assess the stability of conclusions.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_in_chatdev.svg visualized the distributional properties of Input Tokens (count) for the chatdev framework. The Q–Q plot exhibited marked departures from the normal reference line at both tails, with pronounced upward deviations at high theoretical quantiles. The embedded Shapiro–Wilk test indicated non-normality (p < 0.001), and auxiliary diagnostics reported high positive skew (|skew| > 1) and outliers identified via the 1.5×IQR rule. These results suggested a heavy right tail driven by a small number of runs with exceptionally high token counts (≈240k–280k). Mid-quantiles aligned more closely with normal expectations, but the S-shaped pattern confirmed a systematic mismatch rather than random sampling noise. Consequently, the mean (~155k tokens) likely overstated typical usage, whereas the median provided a more robust summary. For hypothesis tests concerning token-count differences or modeling token usage, assumptions of normality and homoscedasticity were not met; non-parametric or robust estimators and bootstrapped confidence intervals are therefore warranted. The visualization directly challenged any hypothesis positing approximately normal token distributions and clarified that inference about chatdev’s input-token behavior should rely on distribution-free or robust methods.

### Actionable Recommendations

- Interpret central tendency with medians (and 95% bootstrap CIs) rather than means; report IQR and possibly 10% trimmed means. 
- Use non-parametric tests (Mann–Whitney U/Kruskal–Wallis) or robust regression/quantile regression for group comparisons or modeling; complement with effect sizes such as Hodges–Lehmann shift or Cliff’s delta. 
- Consider transformations (log or Box–Cox) to stabilize variance; verify improvement via follow-up Q–Q plots and Shapiro–Wilk. 
- Conduct sensitivity analyses: Winsorize or trim 5%–10% of extremes and compare estimates; report influence diagnostics. 
- For publication, accompany the Q–Q plot with density/box/violin plots and a table of median, IQR, and bootstrap CIs; explicitly state p < 0.001 for Shapiro–Wilk. 
- Note limitations: single-framework sample, potential run-level heterogeneity, and right-tail outliers that may reflect specific tasks or logging artifacts.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 43.3s
- Token Usage: 3,848 tokens (1,749 prompt + 2,099 completion)
- Estimated Cost: $0.0000 USD

# Visualization Documentation: qq_plot_tokens_in_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_in  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:34:53.416255Z

---

## Rationale

This Qq Plot visualization was generated to compare Input Tokens (count) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 35750.290 | 35167.000 | [35167.000, 35167.000] | 953.219 | 35167.000 | 38937.000 | 35167.000 | 37052.000 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Input Tokens (count) patterns across frameworks. baes shows the lowest mean (35750.290), while baes exhibits the highest (35750.290), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for baes shows strong deviations from the normal reference line across the entire quantile range. Rather than a smooth alignment, the sample quantiles form two pronounced plateaus around approximately 35.2k and 37.0k tokens, with two extreme high-end points near 39.0k. This step-like pattern indicates discreteness and potential mixture behavior (e.g., two dominant regimes), not a single Gaussian process. The upper tail is markedly heavier than expected under normality, producing pronounced positive skew. Consistent with the visual evidence, the embedded Shapiro–Wilk test reports p < 0.001, confirming a statistically significant departure from normality at α = 0.05. Programmatic diagnostics further flagged high skewness (|skew| > 1), implying that the mean is a poor measure of central tendency; the median and IQR are more representative. With N = 100 runs, the substantial tail and clustering are unlikely to be sampling noise and instead reflect structural features of the data-generating process (e.g., truncation, batching, or heterogeneous prompts). Data quality concerns include potential capping near an operational limit (suggested by the ~39k outliers), discretization due to fixed template lengths, and possible unmodeled stratification. Collectively, the figure indicates that parametric tests assuming normality would be inappropriate without transformation or robust methods; non-parametric comparisons and median-based effect sizes are preferred.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_in_baes.svg summarized the distributional form of Input Tokens (count) for the baes framework using a Q–Q plot against the theoretical normal distribution. The sample quantiles did not align with the diagonal reference; instead, they formed two distinct horizontal clusters near ~35.2k and ~37.0k tokens, with two prominent high-end points close to 39.0k. The Shapiro–Wilk test indicated a significant violation of normality (p < 0.001), and auxiliary diagnostics suggested high positive skew (|skew| > 1) based on N = 100 runs. These results challenged the assumption of Gaussian errors that underpins parametric inference. The presence of discrete plateaus and a heavy right tail is consistent with mixture or truncation processes and implies that the mean is not a stable summary of central tendency. This suggests that subsequent cross-framework comparisons of token usage should rely on rank-based or robust estimators (e.g., medians with bootstrap confidence intervals) rather than t-tests. With respect to the study’s research question regarding distributional assumptions for performance metrics, the figure provided clear evidence that normality did not hold for baes, thereby motivating non-parametric hypothesis testing and robust effect size reporting.

### Actionable Recommendations

Interpret the baes token counts as non-normal, positively skewed, and potentially multimodal. Report medians, IQRs, and bootstrap 95% CIs; avoid means and standard deviations as primary summaries. For between-framework comparisons, use Mann–Whitney U or Kruskal–Wallis with Hodges–Lehmann or rank-biserial effect sizes. Consider transformations (log or Box–Cox) only if they meaningfully reduce skew without obscuring the plateau structure. Investigate data-generation sources of the two clusters by stratifying analyses by prompt/template type and checking for context-limit truncation near ~39k tokens. Evaluate bimodality formally (e.g., dip test or two-component Gaussian mixtures). Handle extreme values via sensitivity analyses (trimmed/winsorized summaries). For publication, present complementary visuals (histogram/density and violin plots) and report the Shapiro–Wilk statistic with p-value alongside robust estimates to transparently justify methodological choices.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 55.5s
- Token Usage: 4,178 tokens (1,663 prompt + 2,515 completion)
- Estimated Cost: $0.0000 USD

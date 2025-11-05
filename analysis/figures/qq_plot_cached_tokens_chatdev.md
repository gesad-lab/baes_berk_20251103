# Visualization Documentation: qq_plot_cached_tokens_chatdev.svg

**Visualization Type**: Qq Plot  
**Metric**: cached_tokens  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T11:26:35.689438Z

---

## Rationale

This Qq Plot visualization was generated to compare Cached Tokens (count) performance across chatdev. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| chatdev | 10056.960 | 7872.000 | [6912.000, 8896.000] | 7654.752 | 0.000 | 39424.000 | 5184.000 | 12288.000 | 9 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Cached Tokens (count) patterns across frameworks. chatdev shows the lowest mean (10056.960), while chatdev exhibits the highest (10056.960), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Cached Tokens (count) in chatdev shows clear deviations from normality. While mid-quantiles lie reasonably close to the 45° reference line, both tails depart substantially. The upper tail exhibits strong positive curvature with several extreme observations around 30–40k tokens, indicating a heavy right tail and high positive skew. The lower tail is compressed near zero, consistent with count data bounded below and possibly reflecting floor effects. The embedded Shapiro–Wilk result (p < 0.001) statistically confirms non-normality at α = 0.05. This pattern suggests that occasional runs cache far more tokens than typical, inflating variance and making the mean a fragile summary. Outliers are visually evident; they likely exceed the 1.5×IQR rule and should be examined for scenario-specific causes rather than dismissed as noise. Given N ≈ 100 runs, the Central Limit Theorem might stabilize sampling distributions of means, but the severe tail divergence and small p-value argue for robust or non-parametric analyses for group comparisons. Effect sizes should emphasize medians and ranks (e.g., Hodges–Lehmann estimator, Cliff’s delta) with bootstrap 95% CIs. Overall data quality appears adequate with no missingness apparent, but the distributional shape (skew/heavy tails) and outliers warrant cautious interpretation and potentially transformation (log or square-root) if parametric modeling is required.

### Camera-Ready Paragraph

Figure: qq_plot_cached_tokens_chatdev.svg presented a Q–Q plot comparing the empirical quantiles of cached token counts from chatdev (N = 100) to a theoretical normal distribution. The points tracked the reference line near central quantiles but diverged substantially in both tails, with a pronounced upward bend in the upper tail and several extreme observations (~30–40k tokens). A Shapiro–Wilk test confirmed strong deviation from normality (p < 0.001). These results indicated positive skew and heavy-tailed behavior, consistent with count data bounded at zero and punctuated by rare, high-caching events. The analysis revealed that the normality assumption required for parametric inference was violated, challenging the use of t-tests or ANOVA for framework comparisons. This suggests that subsequent inference should employ robust or non-parametric procedures and report effect sizes that are insensitive to outliers (e.g., median differences via the Hodges–Lehmann estimator or rank-based metrics such as Cliff’s delta) with bootstrap 95% confidence intervals. In the context of the research questions on efficiency variability, the visualization supported the hypothesis that cached token usage is heterogeneous, with a minority of runs dominating the upper tail, thereby affecting central tendency estimates and uncertainty quantification.

### Actionable Recommendations

Practically, summarize chatdev cached tokens with median and IQR, not the mean, and report bootstrap 95% CIs. For group comparisons, favor Mann–Whitney U or Kruskal–Wallis with robust effect sizes (Hodges–Lehmann, Cliff’s delta). Consider modeling counts via negative binomial or zero-inflated frameworks; if parametric tests are unavoidable, apply a log or square-root transform and verify residual Q–Q plots. Inspect extreme runs (~30–40k tokens) to determine whether they stem from specific tasks or pipeline states; perform sensitivity analyses with trimming/winsorization. Pre-register decision rules for outlier handling. For publication, retain the Q–Q plot, add annotations for the most extreme points, and report Shapiro–Wilk p-values alongside a brief justification for the chosen inference method. If comparing frameworks, complement Q–Q plots with violin/ECDF plots and quantile regression to characterize differences across the distribution.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 45.9s
- Token Usage: 3,681 tokens (1,749 prompt + 1,932 completion)
- Estimated Cost: $0.0000 USD

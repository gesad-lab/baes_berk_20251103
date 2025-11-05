# Visualization Documentation: qq_plot_tokens_out_chatdev.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_out  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T11:39:49.424920Z

---

## Rationale

This Qq Plot visualization was generated to compare Output Tokens (count) performance across chatdev. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| chatdev | 50550.520 | 48016.500 | [45467.000, 49658.000] | 10145.859 | 35241.000 | 83436.000 | 43469.250 | 54369.500 | 6 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Output Tokens (count) patterns across frameworks. chatdev shows the lowest mean (50550.520), while chatdev exhibits the highest (50550.520), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Output Tokens (count) in chatdev shows pronounced deviations from normality. Points align with the reference line only near the middle quantiles; both tails diverge, with the right tail bending markedly above the line. This S‑shaped pattern indicates strong positive skewness and heavy right tails, consistent with a few runs producing substantially more tokens than expected under a Gaussian model. Visual outliers are apparent at the upper end (≈75k–84k tokens), which inflate dispersion and bias the mean upward relative to the median. The embedded Shapiro–Wilk test reports p < 0.001, providing statistical evidence against normality at α = 0.05. Given N ≈ 100 runs, the departure is not a minor sampling artifact; the tail behavior is systematic. Effect sizes cannot be read directly from a Q–Q plot, but the magnitude of tail divergence suggests that parametric tests assuming normal residuals (t-tests, ANOVA on raw counts) would be unreliable or underpowered due to heteroscedasticity and outlier sensitivity. Data quality considerations include potential episodic processes that generate very large outputs (e.g., rare long conversations) and possible batch/run heterogeneity. Summary statistics should emphasize median, interquartile range, and bootstrap confidence intervals rather than the mean and standard deviation. Non-parametric or robust approaches are indicated for hypothesis testing and interval estimation.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_out_chatdev.svg presents a Q–Q plot of Output Tokens (count) for chatdev. The sample quantiles departed systematically from the theoretical normal line, with an S-shaped curve characterized by a pronounced elevation in the upper tail and a slight depression in the lower tail. The Shapiro–Wilk test indicated non-normality (p < 0.001), and diagnostics pointed to high positive skewness (|skew| > 1) with several high-end outliers (~75k–84k tokens). These results demonstrated that the distribution of token counts was not Gaussian. This suggests that parametric procedures that assume normality of raw counts (e.g., t-tests or ANOVA) are inappropriate without transformation or robustification. In the context of the research questions on output-token behavior across runs, the visualization challenged the hypothesis of approximately normal variability and instead supported a heavy-tailed process, likely reflecting episodic runs that generate substantially more content. Consequently, inference should prioritize medians with bootstrap 95% confidence intervals and employ non-parametric tests (e.g., Mann–Whitney U or Kruskal–Wallis) or analyses on transformed scales (e.g., log counts). The figure directly supports these methodological choices by making the tail behavior visually explicit.

### Actionable Recommendations

Interpret output-token variability as heavy-tailed and positively skewed; report medians, IQRs, and bootstrap 95% CIs, not just means/SDs. For between-group comparisons, use Mann–Whitney U or Kruskal–Wallis; for modeling, consider quantile regression or robust regression (Huber/M-estimators). Explore log or Box–Cox transforms and re-check normality/variance homogeneity post-transform. Perform sensitivity analyses with trimming or Winsorizing to assess outlier influence, and examine potential batch effects or run-level covariates that may explain extreme counts. If the research focus is on averages, analyze means via bootstrap or permutation tests rather than normal-theory t-tests. For publication, retain the Q–Q plot with the dashed reference line, annotate N and the Shapiro–Wilk p-value, and accompany it with a table of medians, IQRs, and outlier counts. Clearly state that non-normality was anticipated and handled via robust methods.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 37.2s
- Token Usage: 3,751 tokens (1,749 prompt + 2,002 completion)
- Estimated Cost: $0.0000 USD

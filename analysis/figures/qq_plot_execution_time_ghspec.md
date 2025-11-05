# Visualization Documentation: qq_plot_execution_time_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: execution_time  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:29:22.699273Z

---

## Rationale

This Qq Plot visualization was generated to compare Execution Time (seconds) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 973.927 | 971.109 | [947.341, 1013.552] | 171.452 | 572.157 | 1440.584 | 885.385 | 1065.036 | 5 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Execution Time (seconds) patterns across frameworks. ghspec shows the lowest mean (973.927), while ghspec exhibits the highest (973.927), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q-Q plot for ghspec execution times shows sample quantiles closely tracking the theoretical normal line across the central range, indicating approximate normality. Minor deviations appear at the distributional tails: a slight upward departure for the largest quantiles (roughly two to three points around 1.9–2.4 theoretical quantiles) suggests a mild right-tail heaviness, while the lower tail shows only modest curvature. The embedded Shapiro–Wilk test reports p = 0.275, well above α = 0.05, so normality cannot be rejected. This supports using parametric summaries (mean, SD) and tests (t-tests/ANOVA) for this framework. The tail behavior implies a few slower-than-expected runs that could reflect occasional system jitter (e.g., I/O or GC events). These appear as potential high-end outliers but are not numerous enough to distort the overall linear trend. No S-shaped pattern is visible, arguing against systematic skew. The observable range spans roughly 560–1,450 seconds, with a dense, near-linear midsection from about 800 to 1,200 seconds. Confidence intervals and effect sizes are not shown in a Q-Q plot; however, the non-significant Shapiro–Wilk p-value serves as the principal statistical indicator of distributional adequacy. Data quality appears strong, with adequate sample size and only mild tail deviations; nonetheless, analysts should flag the extreme right-tail points for verification and consider robustness checks to ensure conclusions are not driven by these few runs.

### Camera-Ready Paragraph

Figure: qq_plot_execution_time_ghspec.svg presented a Q–Q plot of ghspec execution times against the theoretical normal distribution. The points followed the reference line closely across the central quantiles, with only mild divergence in the upper tail. A Shapiro–Wilk test embedded in the figure yielded p = 0.275, so the null hypothesis of normality was not rejected at α = 0.05. These results indicated that the distribution of execution times for ghspec was approximately Gaussian, with a small number of slower runs contributing to slight right-tail heaviness. This supports the assumption of normality typically required for parametric inference and suggests that mean-based comparisons and confidence intervals are appropriate descriptors for this dataset. In the context of the research questions on performance stability and comparative efficiency, the visualization supported the hypothesis that ghspec execution time fluctuations were predominantly random and symmetric, rather than systematically skewed. The mild tail deviations indicate that robustness checks (e.g., sensitivity to trimming or winsorization) remain prudent, but they do not challenge the primary inference that parametric tests can be validly applied when evaluating ghspec’s runtime behavior.

### Actionable Recommendations

Proceed with parametric analyses (e.g., t-tests/ANOVA) for ghspec, reporting mean ± SD and 95% CIs, given Shapiro–Wilk p = 0.275 and the near-linear Q–Q pattern. Include robustness checks: (1) compare median/IQR and bootstrapped CIs; (2) re-estimate results after trimming or winsorizing the top 1–5% to assess sensitivity to the mild right tail; and (3) test homoscedasticity (Levene/Brown–Forsythe) before between-group comparisons. Investigate the handful of extreme high-duration runs for run-time confounders (background load, I/O, GC). If multiple frameworks are analyzed, repeat Q–Q and Shapiro–Wilk per framework and consider Kruskal–Wallis as a sensitivity analysis. For publication, pair the Q–Q plot with a histogram/density plot and a table of summary statistics and CIs, clearly annotating the normality p-value and any data-cleaning rules applied.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 56.9s
- Token Usage: 3,814 tokens (1,672 prompt + 2,142 completion)
- Estimated Cost: $0.0000 USD

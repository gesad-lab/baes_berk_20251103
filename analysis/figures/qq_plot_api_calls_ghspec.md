# Visualization Documentation: qq_plot_api_calls_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: api_calls  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:20:41.257808Z

---

## Rationale

This Qq Plot visualization was generated to compare API Calls (count) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 89.910 | 89.000 | [86.000, 91.000] | 10.093 | 70.000 | 116.000 | 82.000 | 97.250 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals API Calls (count) patterns across frameworks. ghspec shows the lowest mean (89.910), while ghspec exhibits the highest (89.910), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for ghspec shows that sample quantiles track the 45° reference line near the center but deviate systematically at the tails. The lower tail is slightly off the line and the upper tail bends above it, indicating a positively skewed distribution with a heavier right tail. Several high-end observations (≈112–116 API calls) lie above the theoretical quantiles, suggesting potential upper-tail outliers; a single low-end point near ≈70 also appears. The embedded Shapiro–Wilk test reports p = 0.016, which rejects normality at α = 0.05. Given the moderate sample size (N ≈ 100), these tail departures are unlikely to be sampling noise alone. This has implications for parametric inference: t-based methods that assume normal residuals may yield biased estimates or anticonservative Type I error. Central tendencies appear concentrated around the mid-to-high 90s, but the asymmetry implies mean and standard deviation are not fully representative. No obvious missingness is visible; point density is uniform across quantiles. Data quality concerns center on tail behavior and outliers rather than measurement gaps. For inference and benchmarking of API call counts, median, IQR, and bootstrap confidence intervals would better summarize performance than mean ± SD, and non-parametric tests are advisable for between-framework comparisons.

### Camera-Ready Paragraph

Figure: qq_plot_api_calls_ghspec.svg evaluated the normality of API call counts for ghspec using a Q–Q plot against the theoretical normal distribution. The points aligned closely with the reference line in the central quantiles but exhibited systematic curvature at the extremes, with an elevated upper tail and several high-end observations. A Shapiro–Wilk test confirmed non-normality (p = 0.016), indicating a statistically significant departure from a Gaussian distribution. Descriptively, the distribution centered around roughly 90–100 calls, yet the right-tail inflation suggested that mean-based summaries may overstate central tendency relative to the median. These results challenge the working hypothesis that API call counts for this framework are normally distributed and, by extension, the suitability of parametric procedures that rely on that assumption. This suggests that subsequent performance comparisons should prioritize robust or non-parametric methodologies and report uncertainty using bootstrap confidence intervals. The visualization directly supports these conclusions by highlighting tail deviations and potential outliers that would influence t-tests or ANOVA.

### Actionable Recommendations

For practical inference, favor robust summaries (median, IQR) and non-parametric tests (Mann–Whitney U for pairwise, Kruskal–Wallis for multiple frameworks). If parametric models are desired, consider transformations (log or Box–Cox) and verify residual normality post-fit. Evaluate tail influence via outlier diagnostics (1.5×IQR rule) and conduct sensitivity analyses with and without outliers. Report bootstrap 95% CIs for medians or location shifts and assess variance equality using Levene or Brown–Forsythe tests. Given N≈100, CLT may stabilize mean estimates, but tail-heavy deviations warrant robust alternatives. For publication, complement the Q–Q plot with histograms or violin plots, clearly state the Shapiro–Wilk p-value, and justify the chosen statistical tests with assumptions checks and pre-registered analysis plans.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 45.8s
- Token Usage: 3,556 tokens (1,585 prompt + 1,971 completion)
- Estimated Cost: $0.0000 USD

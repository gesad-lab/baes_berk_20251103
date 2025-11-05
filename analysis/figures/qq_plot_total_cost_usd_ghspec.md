# Visualization Documentation: qq_plot_total_cost_usd_ghspec.svg

**Visualization Type**: Qq Plot  
**Metric**: total_cost_usd  
**Frameworks**: ghspec  
**Generated**: 2025-11-03T11:46:06.352058Z

---

## Rationale

This Qq Plot visualization was generated to compare Total Cost (USD) performance across ghspec. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 0.065 | 0.064 | [0.062, 0.066] | 0.007 | 0.050 | 0.087 | 0.059 | 0.069 | 2 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Total Cost (USD) patterns across frameworks. ghspec shows the lowest mean (0.065), while ghspec exhibits the highest (0.065), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Total Cost (USD) under the ghspec framework shows sample quantiles aligning closely with the theoretical normal line through the mid-range, but with systematic departures in the tails. The upper tail bends above the line with two conspicuous high-end points (~0.086–0.087), indicating a heavier-than-normal right tail and potential outliers. The lower tail exhibits a milder deviation below the line, consistent with slight right-skew. The embedded Shapiro–Wilk test reports p = 0.041 (< 0.05), providing statistical evidence against normality at α = 0.05. With N ≈ 100 runs, the central limit theorem may mitigate minor deviations for mean-based inference, but the visible tail inflation and outliers can bias standard errors and elevate Type I/II error rates in t-tests/ANOVA. No missing data are evident from the graphic, but the presence of high-end outliers raises data-quality questions (e.g., episodic cost spikes, configuration anomalies, or logging errors). The pattern suggests that median and IQR are more representative than the mean for central tendency and spread. Effect sizes are not directly conveyed by a Q–Q plot; however, the concentration of departures in the upper 5–10% of quantiles implies practically meaningful risk of rare but costly runs. Overall, the visualization and p-value jointly indicate a non-normal, mildly right-skewed distribution with influential upper-tail observations.

### Camera-Ready Paragraph

Figure: qq_plot_total_cost_usd_ghspec.svg depicted the quantile–quantile relationship between Total Cost (USD) for ghspec and the theoretical normal distribution. The points closely followed the diagonal through the central quantiles but departed systematically in the tails, with pronounced positive deviations at the upper tail and two high-end observations. A Shapiro–Wilk test yielded p = 0.041, indicating non-normality at α = 0.05. These results suggested a mildly right-skewed distribution with heavy upper tail, consistent with occasional high-cost runs. In the context of the research question on comparing total costs across frameworks, this challenged the assumption of normal residuals required by parametric tests and indicated that mean-based inference may be sensitive to outliers. The visualization supported the use of robust or non-parametric procedures and the reporting of median-centered estimates with uncertainty. Practically, the tail behavior implies that while typical runs are stable, rare events can substantially increase costs; analyses that account for such tail risk (e.g., quantile-focused methods) are warranted.

### Actionable Recommendations

Interpret the ghspec cost distribution as mildly right-skewed with influential upper-tail observations; emphasize medians, IQR, and robust dispersion (MAD) over means. For hypothesis testing across frameworks, prefer Mann–Whitney U or Kruskal–Wallis, or use robust ANOVA/Welch tests with heteroskedasticity-consistent standard errors. Conduct sensitivity analyses: (a) log or Yeo–Johnson transform, (b) 5% trimming or winsorization, and (c) exclusion of the top two outliers with justification. Validate outliers by auditing run logs and configuration settings to rule out measurement artifacts. Complement group comparisons with quantile regression to assess tail risk. Report bootstrap 95% CIs for medians and effects, and disclose Shapiro–Wilk p-values. For publication, include both the Q–Q plot and a table summarizing median, IQR, and outlier counts; state prespecified alpha levels and corrections if multiple tests are performed.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 42.1s
- Token Usage: 3,584 tokens (1,678 prompt + 1,906 completion)
- Estimated Cost: $0.0000 USD

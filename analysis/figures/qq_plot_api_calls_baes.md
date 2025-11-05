# Visualization Documentation: qq_plot_api_calls_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: api_calls  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:21:27.124285Z

---

## Rationale

This Qq Plot visualization was generated to compare API Calls (count) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 18.310 | 18.000 | [18.000, 18.000] | 0.506 | 18.000 | 20.000 | 18.000 | 19.000 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals API Calls (count) patterns across frameworks. baes shows the lowest mean (18.310), while baes exhibits the highest (18.310), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for API Calls (count) under the baes framework shows a pronounced departure from normality. Points do not align with the 45° reference; instead, they form horizontal bands at integer values (notably 18 and 19), with a few upper-tail points near 20. This step-like pattern reflects the discrete nature of the outcome and suggests heaping at specific counts. Tails diverge from the line, most clearly in the right tail, indicating positive skew and heavier-than-normal extremes. The embedded Shapiro–Wilk result (p < 0.001) statistically confirms non-normality at α = 0.05. Programmatic summaries concur, flagging high skewness (|skew| > 1) and recommending robust methods. Central tendency appears tightly concentrated, with the mean around 18.31 and the median likely near 18–19, but the skew and discreteness make the mean less reliable. Outliers at ~20 calls may represent occasional bursts or a ceiling effect, warranting scrutiny for data generation or logging caps. With N = 100 runs, minor deviations could be tolerable under the CLT, yet the severe, systematic departures here argue against parametric assumptions. Data quality considerations include potential rounding/aggregation to integer counts, limited support (few unique values), and ties that can distort normal-based diagnostics. Overall, the visualization indicates that non-parametric or count-model approaches are more appropriate for inference than Gaussian methods.

### Camera-Ready Paragraph

Figure: qq_plot_api_calls_baes.svg presented a Q–Q plot of API call counts for the baes framework. The sample quantiles displayed step-like horizontal bands at 18 and 19 calls with a few high-end points near 20, rather than following the 45° reference line. The Shapiro–Wilk test indicated a significant deviation from normality (p < 0.001), consistent with the observed positive skew and tail divergence. The distribution exhibited low dispersion around a mean of 18.31, but the discreteness and skew rendered the mean a suboptimal summary relative to the median. These results contradicted the assumption of normality required for standard parametric tests and challenged any hypothesis positing approximately Gaussian behavior in call counts. The pattern is more consistent with a bounded or count-generating process and suggests that robust or non-parametric procedures are warranted. For subsequent hypothesis testing across frameworks, median-based comparisons with bootstrap confidence intervals and rank-based tests (e.g., Mann–Whitney or Kruskal–Wallis) are appropriate. Alternatively, generalized linear models for counts (Poisson/negative binomial) would align with the observed data structure. The figure therefore directly supported the methodological decision to avoid normal-theory analyses for baes.

### Actionable Recommendations

Interpret the counts as a discrete outcome with positive skew. Report medians, IQRs, and bootstrap 95% CIs rather than means alone, and use rank-based tests (Mann–Whitney/Kruskal–Wallis) for between-framework comparisons. If modeling covariates, fit count GLMs (Poisson or negative binomial) and test for overdispersion; consider robust (sandwich) SEs. Inspect the upper-tail points (~20 calls) for process limits or instrumentation caps; if confirmed, discuss potential ceiling effects. Conduct sensitivity analyses with outlier trimming and with robust estimators (Huber, trimmed means). For presentation, accompany the Q–Q plot with ECDFs or violin plots to show discreteness and concentration. Clearly state the Shapiro–Wilk result (p < 0.001) and justify the choice of non-parametric or count-model methods in the methods section.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 42.7s
- Token Usage: 3,780 tokens (1,661 prompt + 2,119 completion)
- Estimated Cost: $0.0000 USD

# Visualization Documentation: regression_tokens_total_vs_total_cost_usd.svg

**Visualization Type**: Regression  
**Metric**: tokens_total  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:49:35.177281Z

---

## Rationale

This Regression visualization was generated to compare Total Tokens (count) performance across ghspec, baes, chatdev. The regression plot shows the relationship between token usage and cost with fitted trend lines.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 347210.760 | 338787.000 | [332269.000, 356658.000] | 38116.260 | 274758.000 | 464365.000 | 319176.750 | 370940.500 | 1 | 100 |
| baes | 45122.300 | 44198.500 | [44190.000, 44213.500] | 1529.463 | 44120.000 | 50218.000 | 44177.500 | 47190.500 | 0 | 100 |
| chatdev | 205467.960 | 193778.500 | [186545.000, 201611.000] | 41986.351 | 139789.000 | 365531.000 | 181751.250 | 225626.500 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The regression reveals Total Tokens (count) patterns across frameworks. baes shows the lowest mean (45122.300), while ghspec exhibits the highest (347210.760), representing a 669.5% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 2 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 2 framework(s): ghspec, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The regression plot shows a clear, nearly linear association between total tokens and total cost within each framework. Despite the on-plot label saying “no relationship,” the fitted lines and high coefficients of determination indicate strong fits: R² ≈ 0.996 (baes), 0.971 (chatdev), and 0.946 (ghspec). Visual slopes imply different marginal costs per token: chatdev exhibits the steepest gradient (~4.5×10⁻⁴ USD/token), roughly 2.3× higher than ghspec (~1.9×10⁻⁴) and slightly above baes (~2.0×10⁻⁴). Framework usage volumes differ markedly: baes has the lowest token counts (mean ≈ 45,122), whereas ghspec is highest (mean ≈ 347,211), a 669.5% relative difference. Outliers are visible for ghspec and chatdev at high token counts, but they do not overturn the linear trend; still, they may inflate variance and influence slope estimates. Distribution diagnostics from the accompanying analysis reported Shapiro–Wilk p < 0.05 for all three frameworks (non-normality), with high skewness in two groups (|skew| > 1), making medians and robust methods preferable. The study used medians with bootstrap 95% CIs, which is appropriate given skew and outliers; confidence bands around the regressions would further aid interpretation. Collectively, the figure indicates statistically meaningful, framework-specific cost scaling with tokens and suggests material effect-size differences in per-token cost, even before formal non-parametric significance testing (e.g., Kruskal–Wallis with post hoc comparisons). A minor data-quality note: the “no relationship” annotations contradict the observed fits and should be corrected.

### Camera-Ready Paragraph

Figure: regression_tokens_total_vs_total_cost_usd.svg depicted the relationship between total tokens and total cost for baes, chatdev, and ghspec. The analysis revealed strong linear scaling within each framework (R² = 0.996 for baes, 0.971 for chatdev, and 0.946 for ghspec). Estimated marginal costs per token differed substantially: chatdev showed the steepest slope (~4.5×10⁻⁴ USD/token), exceeding ghspec (~1.9×10⁻⁴) by ≈2.3× and slightly exceeding baes (~2.0×10⁻⁴). Token volumes also diverged, with ghspec operating at the highest counts (mean 347,210.76) and baes at the lowest (mean 45,122.30), a 669.5% relative difference. Outliers were observed for ghspec and chatdev, but the overall trends remained stable. Shapiro–Wilk tests rejected normality in all groups (p < 0.05), and two distributions exhibited high skewness (|skew| > 1), motivating median-based summaries with bootstrap 95% confidence intervals and non-parametric inference. This suggests that, while cost predictably increases with tokens, frameworks differ in per-token cost efficiency and typical operating scale. The figure therefore supports the hypothesis that token usage is a primary driver of cost and indicates meaningful between-framework differences relevant to the research question on comparative efficiency.

### Actionable Recommendations

For practice, interpret slopes as marginal cost per token and compare medians rather than means given skewness. Report per-token cost distributions and test differences with Kruskal–Wallis plus Dunn’s post hoc (Holm-adjusted), alongside effect sizes (Cliff’s delta). Fit robust regressions (Theil–Sen or quantile) and provide bootstrap confidence intervals for slopes to quantify uncertainty. Check heteroscedasticity and influence diagnostics; consider winsorizing or sensitivity analyses excluding flagged outliers. Normalize costs by task or success criteria to ensure fair comparisons when token volumes differ substantially. For publication, correct the “no relationship” label, add regression confidence bands, and include a table with median costs, IQRs, and 95% CIs. Clearly state that Shapiro–Wilk p < 0.05 justified non-parametric inference and that findings generalize to skewed, outlier-prone workloads.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 60.6s
- Token Usage: 4,313 tokens (1,617 prompt + 2,696 completion)
- Estimated Cost: $0.0000 USD

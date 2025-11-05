# Visualization Documentation: overlap_tokens_out_ghspec_vs_chatdev.svg

**Visualization Type**: Overlap  
**Metric**: tokens_out  
**Frameworks**: ghspec, chatdev  
**Generated**: 2025-11-03T11:50:35.960352Z

---

## Rationale

This Overlap visualization was generated to compare Output Tokens (count) performance across ghspec, chatdev. The overlapping distributions enable direct visual comparison of two-way differences.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 52490.180 | 51643.000 | [50609.000, 53956.000] | 6351.669 | 38737.000 | 72642.000 | 47675.250 | 56534.250 | 2 | 100 |
| chatdev | 50550.520 | 48016.500 | [45467.000, 49658.000] | 10145.859 | 35241.000 | 83436.000 | 43469.250 | 54369.500 | 6 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The overlap reveals Output Tokens (count) patterns across frameworks. chatdev shows the lowest mean (50550.520), while ghspec exhibits the highest (52490.180), representing a 3.8% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 2/2 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 2 framework(s): ghspec, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The overlap plot shows moderately distinct but largely intersecting distributions of Output Tokens for ghspec (blue) and chatdev (orange). Central mass for ghspec was shifted right relative to chatdev, consistent with the reported means (52,490 vs. 50,551; +3.8%). Despite chatdev exhibiting a visibly heavier right tail extending to ~90–95k tokens, most of its density peaked left of ghspec, which explains its lower mean. The overlap coefficient of 0.694 indicates that roughly 69% of probability mass is shared, reinforcing that differences are modest in practice. The statistical annotation reported a borderline p-value (0.0500) and a small effect size (Cliff’s δ = 0.266), implying weak-to-moderate evidence that ghspec tends to produce more tokens. Normality assumptions were violated for both frameworks (Shapiro–Wilk p < 0.05), and both showed outliers; chatdev’s distribution appeared more positively skewed, making medians and IQRs preferable summaries. Under skew and outliers, the Mann–Whitney U test is appropriate; bootstrapped 95% CIs around medians (not shown) would provide more reliable uncertainty than parametric intervals. An unexpected feature is that chatdev’s right tail is longer yet its central tendency remains lower than ghspec, suggesting a mixture or heterogeneity within chatdev runs (a few very large outputs among many smaller ones). Data quality considerations include potential leverage from extreme high-token runs and heteroscedasticity between methods, both of which can dampen significance and inflate mean-based differences.

### Camera-Ready Paragraph

Figure: overlap_tokens_out_ghspec_vs_chatdev.svg compared the distributions of Output Tokens across ghspec and chatdev over N = 100 runs per framework. The analysis revealed that ghspec was right-shifted relative to chatdev, with means of 52,490 and 50,551 tokens, respectively (+3.8%). A Mann–Whitney U comparison yielded a borderline p-value of 0.0500, and the effect size was small (Cliff’s δ = 0.266). The overlap coefficient was 0.694, indicating substantial distributional overlap. Shapiro–Wilk tests rejected normality for both groups, and visual inspection suggested stronger positive skew and more pronounced right-tail events for chatdev, alongside outliers in both frameworks. These results imply that although ghspec tended to generate more tokens on average, the difference was modest and sensitive to distributional assumptions. From a substantive standpoint, the evidence only marginally supported the hypothesis that ghspec produces higher output volume; given the high overlap and skew, median-based contrasts may better capture typical behavior. This suggests that practical distinctions in token generation between the frameworks are limited for most runs, with occasional extreme outputs more characteristic of chatdev.

### Actionable Recommendations

Interpret the difference as small and operationally modest: most runs will produce comparable token counts, with ghspec slightly higher on average. Report medians, IQRs, and Hodges–Lehmann median differences with bootstrap 95% CIs to complement means. Confirm findings with Mann–Whitney U and quantify uncertainty for Cliff’s δ (CI). Examine robustness by trimming or winsorizing and by comparing upper quantiles (e.g., 75th/90th) to characterize chatdev’s heavy tail. Assess heteroscedasticity and perform sensitivity analyses excluding extreme outliers. Increase sample size or stratify by task/prompt to reduce mixture effects and improve power. For publication, annotate plots with median lines and IQR bands, and state the non-normality diagnostics, test choices, α-level, and effect sizes alongside the overlap coefficient to clarify both statistical and practical significance.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 54.3s
- Token Usage: 3,886 tokens (1,615 prompt + 2,271 completion)
- Estimated Cost: $0.0000 USD

# Visualization Documentation: violin_plot_tokens_out.svg

**Visualization Type**: Violin  
**Metric**: tokens_out  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:37:24.475459Z

---

## Rationale

This Violin visualization was generated to compare Output Tokens (count) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 52490.180 | 51643.000 | [50609.000, 53956.000] | 6351.669 | 38737.000 | 72642.000 | 47675.250 | 56534.250 | 2 | 100 |
| baes | 9372.010 | 9031.500 | [9023.000, 9046.500] | 576.600 | 8953.000 | 11281.000 | 9010.500 | 10138.500 | 0 | 100 |
| chatdev | 50550.520 | 48016.500 | [45467.000, 49658.000] | 10145.859 | 35241.000 | 83436.000 | 43469.250 | 54369.500 | 6 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The violin reveals Output Tokens (count) patterns across frameworks. baes shows the lowest mean (9372.010), while ghspec exhibits the highest (52490.180), representing a 460.1% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The violin plot contrasts Output Tokens (count) across ghspec, baes, and chatdev. Clear separation is visible: baes exhibits the smallest output with a tight, compact violin centered around roughly 9–10k tokens (mean 9,372), whereas ghspec shows the largest counts (mean 52,490), a 460.1% increase relative to baes. Chatdev occupies an intermediate-high region with a broad distribution, visually close to ghspec but with a heavier right tail. Width and tail behavior indicate substantial dispersion for ghspec and chatdev, with right-skewness and several extreme high-token cases; programmatic checks flagged outliers for both and high skewness for 2 frameworks (|skew|>1). Shapiro–Wilk tests rejected normality for all three groups (p<0.05), so means are less representative than medians and non-parametric inference is appropriate. The median-based bootstrap 95% CIs (methodology given) support robust uncertainty quantification; although the exact intervals are not printed, the minimal overlap between baes and the others suggests large practical differences. Some overlap between ghspec and chatdev indicates that their central tendencies may be closer, warranting formal non-parametric tests (e.g., Kruskal–Wallis followed by Mann–Whitney) to assess significance. Data-quality considerations include heteroscedasticity (variance rising with mean), right-tailed outliers, and potential sensitivity to task mix. A log transformation or coefficient-of-variation comparison would help stabilize variance and enable fairer cross-framework evaluation.

### Camera-Ready Paragraph

Figure: violin_plot_tokens_out.svg depicted the distribution of Output Tokens (count) for three frameworks. baes produced the fewest tokens (mean 9,372) with a narrow, concentrated distribution, whereas ghspec yielded the most (mean 52,490), representing a 460.1% increase over baes; chatdev occupied an intermediate-high range with greater dispersion and a pronounced upper tail. Shapiro–Wilk tests indicated non-normality for all groups (p<0.05), and outliers were detected for ghspec and chatdev. Consequently, distributions were characterized by medians with bootstrap 95% confidence intervals, and non-parametric testing is indicated (Kruskal–Wallis with Mann–Whitney pairwise follow-ups). The visualization supported the hypothesis that frameworks differ in output-token profiles: baes was clearly separated from the others, while ghspec and chatdev partially overlapped yet showed distinct centers and tail behavior. These results suggest that framework choice materially affects verbosity. Given evident skewness and heteroscedasticity, interpretations should emphasize median differences and robust effect sizes rather than means; variance-stabilizing transformations or coefficient-of-variation comparisons are advisable to align statistical assumptions with the observed data.

### Actionable Recommendations

For practical interpretation, treat differences as substantial: baes is consistently less verbose, while ghspec and chatdev generate markedly more tokens with heavier right tails. Use a Kruskal–Wallis test across the three groups (N=100 each), followed by Holm-adjusted Mann–Whitney tests, and report robust effect sizes (Hodges–Lehmann median differences, Cliff’s delta). Consider log10-transforming tokens or comparing coefficients of variation to address heteroscedasticity. Investigate flagged outliers in ghspec and chatdev to determine whether they reflect rare tasks or controllable settings. For reporting, emphasize medians with bootstrap 95% CIs, overlay raw jittered points on the violins, and note the non-normality (Shapiro–Wilk p<0.05). If task complexity varies, normalize tokens by task length or difficulty to ensure fair cross-framework comparisons.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 50.6s
- Token Usage: 4,631 tokens (1,721 prompt + 2,910 completion)
- Estimated Cost: $0.0000 USD

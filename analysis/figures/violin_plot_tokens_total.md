# Visualization Documentation: violin_plot_tokens_total.svg

**Visualization Type**: Violin  
**Metric**: tokens_total  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:41:15.618514Z

---

## Rationale

This Violin visualization was generated to compare Total Tokens (count) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

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

The violin reveals Total Tokens (count) patterns across frameworks. baes shows the lowest mean (45122.300), while ghspec exhibits the highest (347210.760), representing a 669.5% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The violin plot contrasts total token usage across three frameworks and shows pronounced separation of distributions. ghspec has the largest central mass, centered well above 300k tokens with a long right tail, while chatdev forms an intermediate distribution around ~180–200k with a similarly extended upper tail. baes is tightly concentrated near 45k tokens, with a markedly narrower spread than the other two. Programmatic results report means of 347,210.76 (ghspec) and 45,122.30 (baes), a 669.5% relative difference; visual non-overlap of the inner quartiles implies large practical differences in typical token consumption. Shapiro–Wilk tests indicated non-normality for all frameworks (p<0.05), consistent with the visible skewness (|skew|>1 for two frameworks) and heavy tails. Consequently, medians and IQRs, together with bootstrap 95% CIs, provide more reliable summaries than means. Outliers were detected for ghspec and chatdev; these appear aligned with the long right tails rather than isolated errors, but they inflate means and variance. The between-group spread is heterogeneous (wider violins for ghspec/chatdev vs baes), suggesting heteroscedasticity and reinforcing the need for robust, non-parametric inference (e.g., Kruskal–Wallis followed by rank-based pairwise tests). Overall, the visualization indicates substantial and likely statistically significant differences in token consumption across frameworks, with ghspec most token-intensive, baes most efficient, and chatdev in between.

### Camera-Ready Paragraph

Figure: violin_plot_tokens_total.svg compared the distributions of total token counts across ghspec, baes, and chatdev (N=100 runs per framework). The analysis revealed strong separation among groups: ghspec exhibited the largest token usage with a broad, right-skewed distribution centered above 300k; chatdev showed an intermediate distribution around 180–200k with a similar upper tail; baes displayed a compact distribution near 45k. Means differed widely (ghspec 347,210.76 vs. baes 45,122.30; +669.5%). Shapiro–Wilk tests indicated non-normality for all frameworks (p<0.05), and two frameworks showed high skewness (|skew|>1), justifying median- and rank-based inference. Outliers were present for ghspec and chatdev, consistent with heavy-tailed behavior; bootstrap 95% confidence intervals around medians exhibited minimal overlap, implying large effect sizes. These results supported the hypothesis that frameworks differ in token consumption and indicated that ghspec is the most token-intensive while baes is the most efficient, with chatdev intermediate. The visual evidence, coupled with non-parametric assumptions, suggests that observed differences are both statistically and practically meaningful, informing subsequent evaluation of cost and throughput trade-offs.

### Actionable Recommendations

Interpret group differences using medians, IQRs, and bootstrap CIs rather than means, given non-normality and skew. Formalize the visual separation with a Kruskal–Wallis test followed by Dunn–Bonferroni pairwise comparisons and report effect sizes (Cliff’s delta or rank-biserial r). Assess robustness by repeating analyses on log-transformed tokens and by trimming or Winsorizing outliers. Examine heteroscedasticity via group-wise coefficients of variation. If tasks vary in difficulty, stratify or include task as a covariate in a rank-based ANCOVA. For publication, report N=100 per framework, the outlier rule (1.5×IQR), and provide supplementary ECDFs or ridge plots to corroborate violin shapes. Discuss practical implications in terms of compute cost per run and potential biases introduced by long-tail episodes.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 32.7s
- Token Usage: 3,611 tokens (1,721 prompt + 1,890 completion)
- Estimated Cost: $0.0000 USD

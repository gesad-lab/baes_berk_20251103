# Visualization Documentation: qq_plot_api_calls_chatdev.svg

**Visualization Type**: Qq Plot  
**Metric**: api_calls  
**Frameworks**: chatdev  
**Generated**: 2025-11-03T11:22:09.875236Z

---

## Rationale

This Qq Plot visualization was generated to compare API Calls (count) performance across chatdev. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| chatdev | 116.010 | 111.000 | [109.000, 119.000] | 20.048 | 85.000 | 172.000 | 103.000 | 129.250 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals API Calls (count) patterns across frameworks. chatdev shows the lowest mean (116.010), while chatdev exhibits the highest (116.010), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Outliers**: Detected in 1 framework(s): chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for chatdev’s API call counts shows approximate linearity in the mid-quantiles but clear departures in both tails. The upper tail bends above the reference line, with several points beyond ~160–170 calls, indicating a heavy right tail and potential positive skew. The lower tail also diverges, though less markedly, around ~85–90 calls. Together, these features produce an S-shaped pattern characteristic of non-normal data. The embedded Shapiro–Wilk result (p = 0.005, α = 0.05) confirms a statistically significant deviation from normality with N ≈ 100 runs. This result suggests that parametric procedures relying on normal residuals (e.g., t-tests/ANOVA on raw counts) may be invalid or less efficient. The presence of a few high-end outliers is visually evident and likely inflates variance; robust estimators (median, trimmed means) would be less sensitive. While the central portion aligns reasonably well, the magnitude and consistency of tail deviations imply more than minor sampling noise and point to systematic heterogeneity in API demand across runs (e.g., bursty episodes). No missingness is visible in the figure; however, the tail behavior raises data-quality questions about rare but extreme sessions. Confidence intervals are not depicted here, but bootstrapped intervals around the median would better summarize uncertainty under non-normality. Overall, the Q–Q pattern and p-value provide convergent evidence against the normality assumption for these counts.

### Camera-Ready Paragraph

Figure: qq_plot_api_calls_chatdev.svg presented a Q–Q comparison of chatdev’s API call counts against a theoretical normal distribution. The points adhered to the reference line in the central quantiles but diverged at both tails, with the upper tail bending above the line and several extreme observations around 160–170 calls. A Shapiro–Wilk test indicated significant non-normality (p = 0.005, α = 0.05; N ≈ 100). These results contradicted the working hypothesis that API call counts were approximately normal across runs and supported the interpretation that the distribution was positively skewed with heavy tails. The observed pattern implies that occasional high-demand episodes occurred, producing outliers and inflated variance. Consequently, reliance on parametric tests that assume normality would be questionable; non-parametric or robust approaches (e.g., Mann–Whitney U, Kruskal–Wallis, bootstrapped confidence intervals, or trimmed-mean analyses) are more appropriate for inference. This evidence answers the research question about distributional form by showing that normality does not hold for chatdev’s API usage, which in turn affects the choice of valid statistical procedures and the interpretation of central tendency and variability in system performance.

### Actionable Recommendations

Interpret API call counts as skewed and heavy-tailed: report medians, IQRs, and bootstrap 95% CIs rather than means alone. Use Mann–Whitney U (two groups) or Kruskal–Wallis (multiple groups) for group comparisons; supplement with robust estimators (20% trimmed mean, Huber M-estimates) and sensitivity analyses with winsorized or trimmed data. Consider transformations (log or Box–Cox) for modeling, but present untransformed effect sizes for interpretability. Inspect heteroscedasticity and perform permutation or bootstrap tests if sample sizes differ. Document and justify any outlier handling; report results with and without outliers. For publication, include the Q–Q plot, Shapiro–Wilk statistics (p-value and N), and a table of robust summaries. Clearly state that normality was rejected and that non-parametric/robust methods were pre-specified or chosen post hoc with rationale.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 44.3s
- Token Usage: 3,985 tokens (1,665 prompt + 2,320 completion)
- Estimated Cost: $0.0000 USD

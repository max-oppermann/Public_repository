In high complexity jobs, my predicted job performance is ca. in the **99.5th percentile** (1 in 200). For the average job, it is the **98.9th percentile** (ca. 1 in 90). 

### Calculating that:
The strongest predictor of job performance (as rated by superiors) is general mental ability (GMA); another reliable predictor is trait conscientiousness. My [GMA](README-g.md) is in the 99.9th percentile, my [conscientiousness](Big-Five/README.md) around the 90th.  
These traits correlate with job performance at $0.65$ and $0.22$ respectively;<sup>1</sup> they are themselves uncorrelated. But the correlation between GMA and job performance for the *highest complexity jobs* is actually $0.74$.<sup>2</sup>  
Using the latter to predict my $z$-score for job performance by regressing my GMA and conscientiousness $z$-scores to the mean:  

&nbsp;&nbsp;&nbsp;&nbsp; $z_{\text{Job Performance}}=(0.74\times\Phi^{-1}(0.999))+(0.22\times\Phi^{-1}(0.90))\approx (0.74×3.09)+(0.22×1.28)=2.5682$  

where $\Phi$ is the standard Normal CDF. Converting this $z$-score back to a percentile (assuming job performance is normally distributed):  

&nbsp;&nbsp;&nbsp;&nbsp; $\Phi(2.568)\approx0.9949$.  

This corresponds to a rounded 99.5th percentile. Using the $0.65$ correlation for the average job instead yields the 98.9th percentile.<sup>3</sup> You can check the numbers via, e. g., [this](https://stattrek.com/online-calculator/normal) calculator. 

#### Confidence interval:  
The multiple correlation coefficient for predicting job performance from GMA and conscientiousness (when not differentiating by job complexity) is $0.70$.<sup>1</sup> Using this, a 95% confidence interval for my predicted job performance $z$-score is:    

&nbsp;&nbsp;&nbsp;&nbsp; $2.568 \pm (1.96\times \sqrt{1-0.70^2})$  

which yields a 95% confidence interval of $[1.168,3.968]$ for the $z$-score, corresponding to a range for the job performance percentile of $[87.86, 99.99]$.

#### *Caveat emptor*:  
The relationship between IQ and job performance is [not uncontroversial](https://menghu.substack.com/p/controversy-over-the-predictive-validity-of-iq)<sup>4</sup> and my choice of $0.74$ yields the highest predicted percentile. A naive alternative would be to simply wiggle that $0.74$ in the first equation. The results of that are presented in the table below. Realistically, the regression weight for conscientiousness would also change, yielding a higher predicted percentile, and the multiple correlation coefficient would change as well, yielding a wider CI.

| Correlation | Predicted percentile | 95% CI |
|-------|-------|----------------|
| $0.65$  | $98.9$  | $[81.22, 99.99]$ |
| $0.60$  | $98.3$  | $[76.91, 99.98]$ |
| $0.50$  | $96.6$  | $[66.53, 99.94]$ |
| $0.40$  | $93.5$  | $[54.70, 99.82]$ |
| $0.30$  | $88.7$  | $[42.46, 99.55]$ |

---
<small>
<br>
<sup>1</sup> Table 1 in: Schmidt, F. “The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 100 Years of Research Findings.” Working paper, 2016.  <br>
This is an update to the published article:<br>  
Schmidt, F., Hunter, J. “The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 85 Years of Research Findings.” <i>Psychological Bulletin</i>, 124(2), 1998. 262–274.
<br><br>
<sup>2</sup> <i>Ibid.</i> page 13: "[...] GMA validity
ranged from .74 for professional and managerial jobs down to .39 for unskilled jobs."
<br><br>
<sup>3</sup> The updated paper presents regression weights for GMA and conscientiousness of 0.67 and 0.27 rather than the 0.65 and 0.22 which I would expect because GMA and trait conscientiousness are usually uncorrelated. Using that in the equation yields a z-score for the average job of 2.416 rather than 2.290.
<br><br>
<sup>4</sup> The crux of the issue is range restriction. Range restriction refers to the reduction in variability (SD) of a predictor (e.g., IQ) in a studied sample compared to the broader population of interest (e.g., all job applicants). This reduction occurs because the sample is not randomly selected but filtered through some selection process (e.g., hiring). In other words, <i>successful applicants are already selected on IQ</i>. The stronger the correlation between the selection mechanism and IQ, the more the range will be restricted and the more the estimated impact of IQ on job performance will be nudged upwards when we correct for the restriction. Hunter and Schmidt assume a high correlation; the 0.3 correlation is approximately the result for <i>no range restriction</i>, so a very low correlation between job selection procedure and IQ. <br>
&nbsp;&nbsp;&nbsp;&nbsp; But the construct of "job performance" is also suspect. Usually, supervisor ratings are used, but when hands-on performance tests (which are what they say on the tin) are employed instead, the correlation between IQ and performance goes up.
</small>

In high complexity jobs, my predicted job performance is ca. in the **99.5th percentile** (ca. 1 in 200). For the average job, it is the **98.9th percentile** (ca. 1 in 90). 

### Calculating that:
The strongest predictor of job performance (as rated by superiors) is general mental ability (GMA); another reliable predictor is trait conscientiousness. My [GMA](README-g.md) is in the 99.9th percentile, my [conscientiousness](Big-Five/README.md) around the 90th.  
Using these traits in a regression model to predict job performance yields regression weights of $0.65$ and $0.22$ respectively.<sup>1</sup> Since GMA and conscientiousness are uncorrelated, these weights align with their individual correlations to job performance. But the correlation between GMA and job performance for the *highest complexity jobs* is actually $0.74$.<sup>2</sup>  
Using the latter to predict my $z$-score for job performance by regressing my GMA and conscientiousness $z$-scores to the mean:  
$z_{\text{Job Performance}}=(0.74\times\Phi^{-1}(0.999))+(0.22\times\Phi^{-1}(0.90))\approx (0.74×3.09)+(0.22×1.28)=2.5682$  
where $\Phi$ is the standard Normal CDF. Converting this $z$-score back to a percentile (assuming job performance is normally distributed):  
$\Phi(2.568)\approx0.9949$.  
This corresponds to a rounded 99.5th percentile. Using the $0.65$ correlation for the average job instead yields the 98.9th percentile. You can check the numbers via, e. g., [this](https://stattrek.com/online-calculator/normal) calculator. 

#### Confidence interval:  
The multiple correlation coefficient for predicting job performance from GMA and conscientiousness (when not differentiating by job complexity) is $0.70$.<sup>1</sup> Using this, a 95% confidence interval for my predicted job performance $z$-score is:    
$2.568 \pm (1.96\times \sqrt{1-0.70^2})$  
which yields a 95% confidence interval of $[1.168,3.968]$ for the $z$-score, corresponding to a job performance percentile range of $[87.86, 99.99]$.

---
<small>
<sup>1</sup>Table 1 in: Schmidt, F. “The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 100 Years of Research Findings.” Working paper, 2016.  <br>
This is an update to the published article:<br>  
Schmidt, F., Hunter, J. “The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 85 Years of Research Findings.” <i>Psychological Bulletin</i>, 124(2), 1998. 262–274.
<br><br>
<sup>2</sup><i>Ibid.</i> page 13: "[...] GMA validity
ranged from .74 for professional and managerial jobs down to .39 for unskilled jobs."
</small>

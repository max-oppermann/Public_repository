In high complexity jobs, my predicted job performance is in the **98.6th percentile** among individuals working in these roles (ca. 1 in 70). For the average job, it is the **97.6th percentile** (ca. 1 in 40). 

### Calculating that:
The strongest predictor of job performance (as rated by superiors) is general mental ability (GMA); another reliable predictor is trait conscientiousness. My [GMA](README-g.md) is in the 99.9th percentile, my [conscientiousness](Big-Five/README.md) around the 90th.  
Using these traits in a regression model to predict job performance yields regression weights of $0.51$ and $0.31$ respectively.<sup>1</sup> Since GMA and conscientiousness are uncorrelated, these weights align with their individual correlations to job performance. But the correlation between GMA and job performance for the *highest complexity jobs* is actually $0.58$.<sup>2</sup>  
Using the latter to predict my $z$-score for job performance by regressing my GMA and conscientiousness $z$-scores to the mean:  
$z_{\text{Job Performance}}=(0.58\times\Phi^{-1}(0.999))+(0.31\times\Phi^{-1}(0.90))\approx (0.58×3.09)+(0.31×1.28)=2.189$  
where $\Phi$ is the standard Normal CDF. Converting this $z$-score back to a percentile (assuming job performance is normally distributed):  
$\Phi(2.189)\approx0.9857$.  
This corresponds to a rounded 98.6th percentile. Using the $0.51$ correlation for the average job instead yields the 97.6th percentile. You can check the numbers via, e. g., [this](https://stattrek.com/online-calculator/normal) calculator. 

#### Confidence interval:  
The multiple correlation coefficient for predicting job performance from GMA and conscientiousness (when not differentiating by job complexity) is 0.60.<sup>1</sup> Using this (underestimate), a 95% confidence interval for my predicted job performance z-score is:    
$2.189 \pm (1.96\times \sqrt{1-0.60^2})$  
which yields a 95% confidence interval of $[0.621,3.757]$ for the z-score, corresponding to a job performance percentile range of $[73.27, 99.99]$.

---
<small>
<sup>1</sup>Table 1 in: Schmidt, F., Hunter, J. “The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 85 Years of Research Findings.” <i>Psychological Bulletin</i>, 124(2), 1998. 262–274.
<br><br>

<sup>2</sup>Table 2 in: Schmidt, F., Hunter, J. “General Mental Ability in the World of Work: Occupational Attainment and Job Performance.” <i>Journal of Personality and Social Psychology</i>, 86(1), 2004. 162–173.
</small>

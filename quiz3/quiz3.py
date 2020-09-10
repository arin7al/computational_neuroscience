from scipy.stats import norm

decisionThresholds = [5.667, 5.830, 5.978, 2.69]
mu1 = 5
mu2 = 7
sigma1 = 0.5
sigma2 = 1
lossRatio = 2  # loss ratio of mistakenly picking s2 to mistakenly picking s1
# best decision threshold is loss1*P(r|s1)*p(s1)/p(r) = loss2*P(r|s2)*p(s2)/p(r), or the one closest to it
metrics = []
for x in decisionThresholds:
    pRS_1 = norm.cdf(x, mu1, sigma1)
    pRS_2 = norm.cdf(x, mu2, sigma2)
    metrics.append(lossRatio*pRS_1 + (1-pRS_2))
bestThreshold = decisionThresholds[metrics.index(max(metrics))]
print bestThreshold

import cPickle as cp
import scipy.stats as st
import dadi
import horse_demography


spec = dadi.Spectrum.from_file("../easySFS/horse_DOM2_chr10.filtered.vcf.gz_output/dadi/pop1-20.sfs")

opts = []
for n in range(1,6):
	opts.append([])
	for i in range(50):
		print n, i
		start = st.uniform.rvs(scale=2,size=2*n)
		lower = [.01]*n + [0]*n
		upper = [100]*n + [5]*n
		opts[-1].append(dadi.Inference.optimize_log_fmin(start,spec,horse_demography.epoch_model,100,full_output = True, verbose=50, lower_bound = lower, upper_bound=upper))

outfile = open("optima.pickle","w")
cp.dump(opts,outfile)
outfile.close()

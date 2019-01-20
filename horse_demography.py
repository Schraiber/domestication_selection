import dadi

def epoch_model(params, ns=25, pts = 500):

	num_epoch = len(params)/2

	popsize = params[:num_epoch]
	
	time = params[num_epoch:]


	xx = dadi.Numerics.default_grid(pts)
	
	phi = dadi.PhiManip.phi_1D(xx)

	for i in range(len(time)):
		phi = dadi.Integration.one_pop(phi, xx, time[i], popsize[i])

	fs = dadi.Spectrum.from_phi(phi,ns,[xx]) 

	return fs	

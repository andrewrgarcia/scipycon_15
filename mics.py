#mics.py
#Andrew R Garcia, 2015
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pickle
from scipy.stats import tstd

def shear(N,Ri,R):
    '''shear rate (gamma) function
    Ri=stator radius, mm;  R=rotor radius, mm;    N=frequency, rpm; 
    omega=angular velocity, rad/s'''
  
    omega =2*np.pi*N/60
    gamma=omega/((Ri/R)-1)

    return gamma

def data():
    '''EXPERIMENTAL DATA''' 
    #Microspheres size measurements [microsphere diameters] matrix
    micsM=pickle.load( open( "micsmat.p", "rb" ) )
	
    '''STATISTICAL VALUES'''		
    'mean  vector'
    meanV=np.zeros(8)
    for i in range(0,8):
        meanV[i]=np.mean(micsM[i])
    
    'sample std. deviation (sigma) vector'
    sigmaV=np.zeros(8)
    for j in range(0,8):
        sigmaV[j]=tstd(micsM[j])
		
    return micsM, meanV, sigmaV

def stacks():
 
    [micsM,meanV,sigmaV]=data()
	
    '''SHEAR RATES (gamma) vector'''
    global shear
    #2 different mixers used: mixers 'A' and 'B'
    #rotor and stator radii of mixer A (see def shear): 
    R_A=1.77
    Ri_A=2
    #rotor and stator radii of mixer B (see def shear): 
    R_B=3.82913349489977
    Ri_B=4
    
    gamma2=shear(N=16800,Ri=Ri_A,R=R_A)
    gamma4=shear(N=8000,Ri=Ri_A,R=R_A)
    gamma6=shear(N=1000,Ri=Ri_B,R=R_B)
    gamma8=shear(N=300,Ri=Ri_B,R=R_B)
    gamma7=shear(N=500,Ri=Ri_B,R=R_B)
    gamma5=shear(N=2000,Ri=Ri_B,R=R_B)
    gamma3=shear(N=4000,Ri=Ri_B,R=R_B)
    gamma1=shear(N=6000,Ri=Ri_B,R=R_B)
    gammaV = np.array([gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8])
   
    '''HISTOGRAMS'''
    bins =20
    # A= SUM(a_ij)
    histM = [[0 for j in range(8)] for i in range(np.shape(micsM[2])[0])]
    binsM = [[0 for j in range(8)] for i in range(np.shape(micsM[2])[0])]
    # Create histograms and normalize total count to 1 (data):
    for i in range(0,8):
        histM[i],binsM[i]= np.histogram(micsM[i], bins = bins)
        histM[i] = [ float(n)/sum(histM[i]) for n in histM[i]]
    # Set histograms' parameters (data)
    center = [[0 for j in range(8)] for i in range(20)]
    width=np.zeros(8)
    for i in range(0,8):
        center[i] = (binsM[i][:-1]+binsM[i][1:])/2
        width[i]= 1*(binsM[i][1]-binsM[i][0]) 
            
    f, ax = plt.subplots(4, 4)            
    # Generate histograms + hist. annotations/description + hist. color style         
    cmap = mpl.cm.cool
    for k in range(0,4):
        ax[k, 0].bar(center[k], histM[k], align = 'center', width = width[k],color=cmap((k+2) / float(11)))
        ax[k, 0].text(5.2,0.25,"$\dot{\gamma}$="+str(round(gammaV[k],1))+r" rad/s")
        ax[k, 0].text(5.2, 0.22,r"D="+str(round(meanV[k], 1))+r"$\pm$"+str(round(sigmaV[k], 1))+r"$\; \mu m$")
        ax[k, 0].set_ylabel('P'), ax[k, 0].set_xscale('log'), ax[k, 0].set_xlim([0.1, 100]),ax[k, 0].set_ylim([0, 0.3])
    
    for k in range(4,8):
        ax[k-4, 2].bar(center[k], histM[k], align = 'center', width = width[k],color=cmap((k+2)/ float(11)))
        ax[k-4, 2].text(5.2,0.25,"$\dot{\gamma}$="+str(round(gammaV[k],1))+r" rad/s")
        ax[k-4, 2].text(5.2, 0.22,r"D="+str(round(meanV[k], 1))+r"$\pm$"+str(round(sigmaV[k], 1))+r"$\; \mu m$")
        ax[k-4, 2].set_ylabel('P'), ax[k-4, 2].set_xscale('log'), ax[k-4, 2].set_xlim([0.1, 100]),ax[k-4, 2].set_ylim([0, 0.3])
    
    ax[3, 0].set_xlabel('Microsphere diameter, $\; \mu m$')
    ax[3, 2].set_xlabel('Microsphere diameter, $\; \mu m$')

    '''IMAGES'''
    img,img2,img3,img4,img5,img6,img7,img8 = pickle.load( open( "imgdata.p", "rb" ) )
    
    ax[0, 1].imshow(img), ax[1, 1].imshow(img2), ax[2, 1].imshow(img3), ax[3, 1].imshow(img4)
    ax[0, 3].imshow(img5), ax[1, 3].imshow(img6), ax[2, 3].imshow(img7), ax[3, 3].imshow(img8)
    
    # Fine-tune figure
    f.subplots_adjust(hspace=0,wspace=0,left=0.08,right=0.95)
    plt.setp([a.get_xticklabels() for a in f.axes[:]], visible=False)
    plt.setp([a.get_yticklabels() for a in f.axes[:]], visible=False)
    plt.setp(ax[3, 0].get_xticklabels(), visible=True)
    plt.setp(ax[3, 2].get_xticklabels(), visible=True)
    plt.suptitle('Microspheres size distribution',size=15)
    plt.show()

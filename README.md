#Entry to the 2015 Scipy John Hunter Excellence in Plotting Contest
##Authors (plot):

Andrew R. Garcia

[This figure is based on scientific work done by Andrew Garcia, Catherine Snyder, Christopher Lacko, and Dr. Carlos Rinaldi in 2014 and 2015.]

##Abstract: 
An emulsion is a stabilized mixture of two commonly immiscible liquids, such as water and oil, where one liquid is dispersed in the other. The dispersed liquid naturally takes the shape of a ‘droplet’ in the larger liquid or continuous phase.

In 1934, Sir G.I. Taylor published an article where emulsion formation was quantified with theoretical estimates.1 The emulsion droplets that Taylor analyzed were in the order of a centimeter and characterized by photographs. For this plot, a series of microsphere experiments made by an emulsification process were made in order to show how Taylor’s theory can extend to microscopic systems. 

The emulsification process employed was comminution, where an emulsion is made by disrupting a larger volume into smaller subunits with a mechanical force. After comminution the microspheres are created by crosslinking microscopic emulsion droplets with a calcium chloride solution. Two different rotor-stator mixers were used to produce the emulsion. The shear rate produced by the mixers γ ̇ is used in order to remove the dependency of the different rotor-stator dimensions between the two mixers.  

<img src="http://latex.codecogs.com/gif.latex?\dot\gamma&space;=&space;\frac{R\omega}{R_{i}-R}" title="\dot\gamma = \frac{R\omega}{R_{i}-R}" />

Where ω, Ri and R are the angular velocity of the mixer’s rotor, the stator radius and the rotor radius, respectively.2 The results for the series of experiments shown in this plot vary in the shear rate employed to make the microspheres. 

From Taylor’s analysis it can be deduced that the size of the emulsion droplet is inversely proportional to shear rate employed to make it. An agreement with this relation was met at significantly high shear rates that produce microspheres with relatively uniform size distributions. At lower shear rates a limitation in this agreement is found as the microspheres become more poly-disperse due to low power mixing.  

Each histogram is the result of measuring the size of about 100 microspheres from taken Scanning Electron Microscopy (SEM) images through ImageJ. In this plot each histogram is complemented by an SEM image of its corresponding experiment, where the scale bar in the last SEM image is global to all images. For the Python script, all SEM image data was imported into **numpy** arrays using **matplotlib.image** package module. The microsphere size measurements of all experiments were arranged in an array to facilitate generating the information and representation of the plot with *for loops*. The mean and standard deviations in all experiments were calculated using numpy and the **scipy.stats** package module, respectively. Object serialization was done with the **pickle** module.

[1] Taylor, G. I. "The formation of emulsions in definable fields of flow."Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character (1934): 501-523. 

[2] Mabille, C., V. Schmitt, Ph Gorria, F. Leal Calderon, V. Faye, B. Deminiere, and J. Bibette. "Rheological and shearing conditions for the preparation of monodisperse emulsions." Langmuir 16, no. 2 (2000): 422-429.

# Limits on the stability of TRAPPIST-1

This repository contains the source code to reproduce the simulations and figures from Tamayo et al. (2017). The data generation and processing is segmented. We start from the most processed (figures) to the least (generating the data files).

The various scripts require REBOUND (https://github.com/hannorein/rebound), REBOUNDx (https://github.com/dtamayo/reboundx), and fairly standard python libraries (jupyter, matplotlib, numpy, pandas).

# Figures

fig1, fig2, fig3 and fig4.ipynb reproduce the figures in the paper, and use CSV files in the csvs directory.

# CSVs

The ipynbs starting with `process_` generate the CSV files for visualization from the simulation archive files. To run them, you first have to get the datafiles at https://zenodo.org/record/496153, and place all the files in the data/ directory.

`process_instability_times.ipynb` extracts the instability times from all the simulations.
`process_nonres_instablity_times.ipynb` does the same for the initial conditions drawn from Gillon et al. (2017). See paper for details.
`process_orbital_elements.ipynb` generates a large number of orbital elements, not all of which were incorporated into the paper figures. This file can be used as a template to extract other data of interest from the simulations, and the figure notebooks for how to plot them.

# Simulation Archives

The simulations can be reproduced following a sequence of steps, separated as folders. Each one has a script particular to the job submission format on the CITA cluster that would have to be modified.

To generate the disk-migration simulations:

1. makeic--This will attempt to generate a resonant chain using the simID as the seed for the random number generator
2. selectic--Not all systems generated in the above step will have the observed commensurabilities. This step adiabatically removes the disk forces, applies the $\eta$ kick described in the paper ('mag' in the code), and then checks whether the commensurabilities are satisfied. If they are, it will set up and run a short simulation archive.
3. runs--This script can be run over and over with increasing tmax. It will restart the simulationarchive from the previous step (or one already run to a particular tmax).

To generate the Gillon 2017 simulations:

Run the script in the nonres folder.

The above scripts all rely on some convenience functions in ic.py at the top level of the repository.

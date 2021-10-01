# ewatercycle examples
![image](https://github.com/eWaterCycle/ewatercycle/raw/main/docs/examples/logo.png)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5543899.svg)](https://doi.org/10.5281/zenodo.5543899)

A collection of Jupyter notebooks accompanying the publication `The eWaterCycle platform for Open and FAIR Hydrological collaboration` (link follows). eWaterCycle is a platform for conducting computational hydrological research. See this video (link follows) for a short overview of the platform and its capabilities. See the publication for more details on the design choices made when building the platform. Finaly, see the [eWaterCycle package repository](https://doi.org/10.5281/zenodo.5119389) for the code behind the platform

This repo contains five notebooks with use cases of computational hydrological research that illustrate the capabillities of the eWaterCycle platform. Those use cases are:

1. a 'Hello world' use case demonstrating how a model is setup-up, how forcingdata is created using ESMValTool and how a model is run. The calculated river discharge is compared against GRDC observations.
2. a model comparison notebook where two (distributed) models are run for the same catchment and the generated discharge is compared against GRDC observations.
3. a model coupling notebook where the output from one model is used as input for another model. Note that the models are written in different programming languages, but the hydrologist conducting the experiment can work from the (python) eWaterCycle environment.
4. an experiment where the state of the model is changed during runtime. Each timestep the model state is altered to correct the calculated evaporation based on (Fluxnet) observed evaporation.
5. A model calibration study where a model is run in parallel many times to calibrate its parameters based on observations.

The eWaterCycle platform, including the models used in the notebooks of this repository, can be installed on any sufficiently advanced computer. See the installation instructions for the [eWaterCycle package repository](https://doi.org/10.5281/zenodo.5119389). Currently no publicly accessable machine is available where any scientist can work on the eWaterCycle platform without having to install it themselves. This might change with future funding oppertunities (in which case this page will also be updated).

More examples, for more different models, can be found in the
[eWaterCycle documentation](https://ewatercycle.readthedocs.io).

## License

Copyright (c) 2021, Netherlands eScience Center & Delft University of
Technology

Apache Software License 2.0
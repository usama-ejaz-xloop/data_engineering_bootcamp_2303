# Introduction to MLFlow

This module will bring you up to speed with basics of MLFlow.

## Needed tools

You will need to install anaconda. It is used by MLFlow by default, and it really helps portability.
In `conda.yaml` there are specified project dependencies. Each time you will train a model its directory will contain these dependencies.
In this way you can export model to a different server and when you use MLFlow it will know what library versions it should use.

It is also possible to configure these dependencies for each step separately, but we will not do this in this course.

It is helpful to remember it though because sometimes you might require some steps to run Spark and have different dependencies.

Look into [installing options](https://docs.anaconda.com/anaconda/install/linux/)

After completing the installation, provide path to your conda binary in mlflow_env_vars.sh.  
**Take the content from output of `echo $CONDA_EXE` command**  
Example:
`echo $CONDA_EXE`   
**/home/patryk/anaconda3** /bin/conda

The file should look like 
``` python
#!/bin/sh

export MLFLOW_CONDA_HOME=/home/patryk/anaconda3/
export MLFLOW_TRACKING_URI="http://localhost:5000"
export MLFLOW_AR=./mlruns
```



## The environment preparation

1. Conda is used for running MLFlow steps using conda environments. We are going to work still with use of `virtualenv`. Python `3.10.6` is assumed.

2. Run the following commands to prepare the environment:
`virtualenv --python=/usr/bin/python3 mlops-student`

3. Enter the virtual environment with:
`source mlops-student/bin/activate`

4. Install mlflow (2.0.1)
`pip install mlflow`

4. (**to be used only if the notebook has some issues running the examples**) In your conda environment install modules if needed:
    `/home/<user>/anaconda3/bin/python3.9 -m pip install mlflow category-encoders==2.5.1.post0 cloudpickle==2.2.0 psutil==5.9.2 scikit-learn==1.1.3`

5. Once you are in virtual environment run the `jupyter lab &`. linux command.
6. Navigate to MLFlow_lab.ipynb, the other needed files will be referenced in the notebook.

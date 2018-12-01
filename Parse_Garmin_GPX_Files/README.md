# Parse GPX Files

## References

- <https://en.wikipedia.org/wiki/GPS_Exchange_Format>

- <https://ocefpaf.github.io/python4oceanographers/blog/2014/08/18/gpx/>
- <http://support.datascientistworkbench.com/knowledgebase/articles/600735-how-do-i-install-additional-libraries-in-my-notebo>
- <http://wiki.openstreetmap.org/wiki/GPX>

- <https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html>

- <http://benalexkeen.com/resampling-time-series-data-with-pandas/>

## Install Anaconda

<https://www.anaconda.com/download/>

## Download GPX file from Garmin 51LMT-D SatNav

Connect Garmin via USB to a Mac and enter file tranfer mode. Ignore Disk errors. On the mounted SD Card the GPX files should be found at: -

- ```GPX\Current.gpx```
- ```.System\GPX\DriveLog.gpx```

Create data folder and copy ```GPX``` folder into it.

~~~
mkdir -p ./notebooks/_Data/
~~~

### Normalize Time Formats

~~~
./convert_gpx_timestamps.py "./_Data/GPX/**/*.gpx"
~~~

## Install pip requirements

### zshrc, Update

~~~
vim ~/.zshrc
~~~

Add lines

~~~
# Anaconda
export PATH="$PATH:${HOME}/anaconda/bin"
~~~

Re-source

~~~
source ~/.zshrc
~~~

## zshrc, Install xelatex, for Jupyter save as PDF

<https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex>

~~~
vim ~/.zshrc
~~~

~~~
# TeX
export PATH="/usr/local/texlive/2017/bin/x86_64-darwin/:$PATH"
~~~

### Install gpx via pip

<https://stackoverflow.com/questions/43437884/jupyter-notebook-import-error-no-module-named-matplotlib>

#### Create environment

~~~
conda create --name germin_gpx python=3.6 -y
~~~

#### Get conda environments

~~~
conda info --envs
~~~

~~~
# conda environments:
#
germin_gpx               /Users/jpnewman/anaconda/envs/germin_gpx
root                  *  /Users/jpnewman/anaconda
~~~

## Install jupyter

~~~
conda install jupyter -y
~~~

#### Load Environment

~~~
source activate germin_gpx
~~~

#### Install Requirements

~~~
pip3 install -r requirements.txt
~~~

-- or --

~~~
pip3 install gpxpy
pip3 install seawater

# pip3 install oceans
# pip3 install git+git://github.com/pyoceans/python-oceans.git
# pip3 install /Users/johnpaulnewman/Documents/dev/github/python-oceans
pip3 install git+git://github.com/jpnewman/python-oceans.git

pip3 install netCDF4

pip3 install mplleaflet
~~~

## Run Jupyter

~~~
cd notebooks
~~~

~~~
jupyter notebook Garmin_GPX.ipynb
~~~

### Create Slideshow

~~~
cd notebooks
jupyter nbconvert Garmin_GPX.ipynb --to slides --post serve --ServePostProcessor.port=8910 --ServerPostProcessor.ip='*'
~~~

#### Deactivate environment

~~~
source deactivate
~~~

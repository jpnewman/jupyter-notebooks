
Jupyter Notebook Examples

## References

- <https://www.anaconda.com/download>
- <http://jupyter.org/>

### Pandas

- <https://pandas.pydata.org/>
- <https://pandas.pydata.org/pandas-docs/stable/10min.html>
- <https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html>

- <http://robertmitchellv.com/blog-bar-chart-annotations-pandas-mpl.html>

- <https://www.dataquest.io/blog/settingwithcopywarning/>

### Plotly

- <http://blog.kaggle.com/2016/11/30/seventeen-ways-to-map-data-in-kaggle-kernels/>
- <https://raw.githubusercontent.com/grantbrown/Influenza/master/Data/Census/NST-EST2014-01.csv>

### Data Set

- <https://catalog.data.gov/dataset?res_format=CSV>
- <https://www.cdc.gov/nchs/data-visualization/mortality-leading-causes/index.htm>


## Data Set

- <https://catalog.data.gov/dataset/age-adjusted-death-rates-for-the-top-10-leading-causes-of-death-united-states-2013>

## Add Anaconda to path, if needed

~~~
export PATH="$PATH:${HOME}/anaconda/bin"
~~~

#### Create environment

~~~
conda create --name jupyter python=3.6 -y
~~~

#### Load environment

~~~
source activate jupyter
~~~

## Run Jupyter

~~~
cd notebooks
~~~

~~~
jupyter notebook
~~~

## Load Notebook

~~~
jupyter notebook NCHS_Leading_Causes_of_Death_USA.ipynb
~~~

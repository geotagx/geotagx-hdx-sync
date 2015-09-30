## Creating a Dataset in HDX
In order to create a dataset on HDX programmatically, run the functions `CreateDataset()` and `CreateResource()` available in `create/create.py` script. That function takes two parameters as input:

* **apikey**: (String) Your HDX API key.
* **path**: (Dictionary) An object with all the fields necessary to create a dataset and add resources in HDX.

HDX has created a series of custom validators. Please refer to the file `dataset.json` for an example that includes all the required fields for a dataset and the `resource.json` file for the required fields for a resource.

You will notice that, in HDX, there are a number of fields that are required. For instance, you will need to add a `group` field which refers to a country in HDX by adding the country's ISO 3-letter-code. For more information about the HDX metadata, please refer to HDX's [dataset metadata guide](http://docs.hdx.rwlabs.org/providing-metadata-for-your-datasets-on-hdx/).

## Usage
To experiment with the script, do the following:

* Add your HDX API Key to the `create/create.py` script.
* Edit the `dataset.json` file.


## Setup
Create a virtual environment using `virtualenv` and install the dependencies from `requirements.txt`. The `Makefile` setup instruction contains those commands and can be run with the shortcut (run it inside the repository folder):

```shell
$ make setup
```

##TO-DO
* Add script to create GeoJSON resource for *all* projects on GeoTagX
* Refactor and add separate configuration file for params like author, email, etc

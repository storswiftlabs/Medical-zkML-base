# Medical-zkML-base

## Description

As the base library of Medical-zkML. Using leo_translate tool generate machine learning model prediction process, likes
decision tree，K-Means and XGBoost. Additional libraries will be added in the future.

## Directory structure

- data: The UCI nine medical datasets, "new_data.tsv" file is generated after data preprocessing.
- leo_translate: Leo transpiler, include Leo language different module
  - context: Process the transformation context to build the complete Noir file
  - core_module: Include some core components such as statements, struct and function
  - submodule: Include some base components such as base type sign and keywords
  - utils: tools such as code format
- model_generate: Include three ML algorithm train and generate model obj
- src: Include three ML algorithm and preprocess code, Used python generated Leo code and data preprocess
- tests: Testcase for leo transpiler and translation model from python to Leo

## Build guide

- Python 3.7+
- Anaconda
- Leo for Visual Studio Code 0.16.0

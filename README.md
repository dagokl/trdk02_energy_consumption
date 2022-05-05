# Energy Consumption Anomaly Detection
This repository contains the work done by group 17 in the subject IT2901 in 2022. The project aims to use machine learning to detect anomalies in energy consumption. The project is done for Trondheim municipality and the data used are from their buildings.

## Anomaly Detection Pipeline
![Image of pipeline](/images/orchest_pipeline.jpg)
Here we deploy our Energy Temperature Time (ETT) model. The pipeline runs in Orchest and integrates with Clarify. The anomalies found can be viewed in Clarify. The pipeline is located in this repo: https://github.com/dagokl/trdk02_energy_consumption_anomalies_pipeline  
![Image of Clarify](/images/clarify.jpg)

## Notebooks
In addition to the pipeline, we have created some notebook while experimenting with different models. These notebooks are located in the models folder.
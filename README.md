# MIU Machine Learning
This repository is for Machine Learning class at MIU.
Unless the students choose a different project, the default project is
"the Mongolian Sidewalk Project" described below.


# Mongolian Sidewalk Project
The goal of the Mongolian Sidewalk Project is build an AI
that detects various objects seen in the streets of Mongolia.
By doing the project, the students will have a chance to see the whole aspects of 
developing an AI and thereby learn Machine Learning.

# What needs to be done?
Here is what is expected for all participants.
1. Collecting data: Take pictures of the streets in Mongolia and add to
 "data/sidewalk_mn/to_label" folder.
2. Label: Use [makesense.ai](https://www.makesense.ai/) to label target objects
 (See Dataset section for details). We are using bounding box label type.
 After you are done with labeling, export the annotation in YOLO format.
3. Train: As a starter, we will use YOLO V5.
4. Predict: After the model is trained, we will use a testset to evaluate the model performance
5. Deploy: For a demo purpose, we will create a simple web service to predict real data.

# Dataset
To train a model, we need a lot of data. Our target goal is 
to have at least 300 labeled images.

Each participant is expected to contribute at least 50 labeled images.
After 300 labeled images are gathered, we will split the data into:
- train: 200 images
- validation: 50 images
- test: 50 images

## Classes

The initial dataset classes are borrowed from the Korean sidewalk dataset.
There might be different objects we are interested in identifying so we will
leave the option to add more classes later on.
The initial classes are:

| id | class label |
| --- | --- |
| 0 | wheelchair |
1 | truck |
2 | tree_trunk |
3 | traffic_sign |
4 | traffic_light |
5 | traffic_light_controller |
6 | table |
7 | stroller |
8 | stop |
9 | scooter |
10 | potted_plant |
11 | power_controller |
12 | pole |
13 | person |
14 | parking_meter |
15 | movable_signage |
16 | motorcycle |
17 | kiosk |
18 | fire_hydrant |
19 | dog |
20 | chair |
21 | cat |
22 | carrier |
23 | car |
24 | bus |
25 | bollard |
26 | bicycle |
27 | bench |
28 | barricade |
29 | van |

# Related Work

There have been several Machine Learning projects that deal with
sidewalk image data. For instance, [Deep Learning for Automatically Detecting Sidewalk
Accessibility Problems Using Streetscape Imagery](https://kurti.sh/pubs/sidewalk_cv_assets_final_fixed_accessible.pdf) (2019),
and [Korean sidewalk project](https://aihub.or.kr/aidata/136) for
people with disabilities.

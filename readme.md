# Human Activity Recognition in Snowboarding

## Introduction

Data from wearable sensors were collected on a subject
while snowboarding for a total duration of 353 minutes.
Every minute, a class label was assigned to classify the activity of the subject.

There are 6 different activities: lift, lying, sitting, snowboarding, standing and towlift.

The objective is to predict one of the 6 possible activities,
given a 60 sec window of 25 metrics from wearable sensors.

Methodology is open. You can extract new features, make a feature selection,
propose your favorite machine learning algorithm.

## Dataset description

The dataset is split in three parts: train, validation and test.

The training split covers the first 270 min, the validation split the next 30 min,
and the test split the last 53 min. This is then a rather small dataset.

Features are in the `split_feat.csv` files.
Activity labels are in the `split_label.csv` files.

## Features description

There are a total of 25 metrics.
* `HR`: heart rate (beats per minute)
* `HRConfidence`: heart rate confidence.
* `HRV`: heart rate variability.

* `BR`: breathing rate (breths per minute)
* `BRAmplitude`: breathing amplitude (bits).
* `BRNoise`: breathing noise.
* `BRConfidence`: breathing confidence.

* `SkinTemp`: skin temperature (degree Celcius)
* `GSR`: Galvanic skin response.

* `Posture`: vertical posture (degrees from vertical, range from +/- 180)
* `Activity`: vector magnitude units (VMU). See manual for details.
* `PeakAccel`: peak acceleration.

* `VerticalMin`: minimum vertical acceleration (x axis).
* `VerticalPeak`: peak vertical acceleration (x axis).
* `LateralMin`: minimum lateral acceleration (y axis).
* `LateralPeak`: peak lateral acceleration (y axis).
* `SagittalMin`: minimum sagittal acceleration (z axis).
* `SagittalPeak`: peak sagittal acceleration (z axis).

* `ECGAmplitude`: electrical activity of the heart (volts).
* `ECGNoise`: noise in the ECG signal.

* `ROGState`: red (exceeded threshold values), orange (crossed threshold values), green (ok)
* `ROGTime`: time duration of status

* `AuxADC1`: additional or just hardware noise
* `AuxADC2`: additional or just hardware noise
* `AuxADC3`: additional or just hardware noise

For detailed information, please check the
[user manual](https://www.zephyranywhere.com/media/download/bioharness-log-data-descriptions-07-apr-2016.pdf)

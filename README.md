# MobileNetv2 Object Detection Notes
## Training Parameter
```bash
# training_2205160210
learning_rate_base: 0.3
total_steps: 12000
warmup_learning_rate: 0.03
warmup_steps: 1000

# 2nd failed, lr too high, gradient exploding
# parameters
num_classes = 1
batch_size = 8 #16
num_steps = 52000 #50000
num_eval_steps = 1000

learning_rate_base = 0.2 #0.8
total_steps = num_steps #50000
warmup_learning_rate = 0.03 #0.13333
warmup_steps = 1000 #2000

# 3rd (not finish, until Step 42100)
# parameters
num_classes = 1
batch_size = 8 #16
num_steps = 52000 #50000
num_eval_steps = 1000

learning_rate_base = 0.03 #0.8
total_steps = num_steps #50000
warmup_learning_rate = 0.013333 #0.13333
warmup_steps = 1000 #2000

# 4th
# parameters
num_classes = 1
batch_size = 8 #16
num_steps = 52000 #50000
num_eval_steps = 1000

learning_rate_base = 0.02 #0.8
total_steps = num_steps #50000
warmup_learning_rate = 0.013333 #0.13333
warmup_steps = 1000 #2000

```

## Ref
- [ReadTheDocs | Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#evaluating-the-model-optional)
  - Good intro in using OD API
- [GitHub | TF/TPU compatible detection pipelines](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tpu_compatibility.md)
  - Official guide in using TPU
  - learning_rate_base: .04
    total_steps: 25000
    warmup_learning_rate: .013333
    warmup_steps: 2000
- [SO | Changing the optimizer in the tensorflow object detection](https://stackoverflow.com/questions/56167463/changing-the-optimizer-in-the-tensorflow-object-detection)
  - learning_rate_base: 0.2
    total_steps: 2000
    warmup_steps: 0
- [NeptuneBlog | TensorFlow Object Detection API: Best Practices to Training, Evaluation & Deployment](https://neptune.ai/blog/tensorflow-object-detection-api-best-practices-to-training-evaluation-deployment)
  - Good explanation in using cosine decay lr
- [SO | Tensorflow object detection API loss increases dramatically](https://stackoverflow.com/questions/68834108/tensorflow-object-detection-api-loss-increases-dramatically)
  - divided the batch size by 64, so I divided the learning rate by the same amount
- [GitHub | ssd_mobilenet_v2_320x320_coco17_tpu-8.config](https://github.com/tensorflow/models/blob/master/research/object_detection/configs/tf2/ssd_mobilenet_v2_320x320_coco17_tpu-8.config)
  - Original config file
  - learning_rate_base: .8
    total_steps: 50000
    warmup_learning_rate: 0.13333
    warmup_steps: 2000
- [Gist GitHub | pets_detector.config](https://gist.githubusercontent.com/sayakpaul/70c414fbe581def12f4b500659372c4f/raw/4f6c52548749c2991af4357e0fe07466382274a1/pets_detector.config)
  - learning_rate_base: .2
    total_steps: 2000
    warmup_learning_rate: 0.13333
    warmup_steps: 0
- [Google Colab | DepthAI Tutorial: Training an Object Detection Model with Your Own Data](https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/Easy_Object_Detection_With_Custom_Data_Demo_Training.ipynb#scrollTo=CjDHjhKQofT5)
  - other similar script
- [Medium | How to retrain an object detection model with a custom training set](https://medium.com/analytics-vidhya/how-to-retrain-an-object-detection-model-with-a-custom-training-set-c827aa3eb796)
  - From my experience, loss function result with a value lower than 0.2 is enough for a demo application.
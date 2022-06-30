# Convert_to_TFLITE
#introduction
Similar to the page page this follows, object detection, this is a loose look at the code I used and how to use it. The following sources should be your primary source.  
[Convert TF Object Detector Google Collab](https://colab.research.google.com/github/tensorflow/models/blob/master/research/object_detection/colab_tutorials/convert_odt_model_to_TFLite.ipynb)  
[Gilbert Tanner's "Convert your Tensorflow Object Detection model to Tensorflow Lite."](https://gilberttanner.com/blog/convert-your-tensorflow-object-detection-model-to-tensorflow-lite/)  
Gilbert's article was pretty helpful for understand the workflow however the google collab is the software base for this repo.  
Before you start you should train a model and test it using a script to confirm it works correctly.  

## Step 1: Export Inference Graph
I used the script **export_tflite_graph_tf2.py** to turn a saved model into a copy that is able to be interpretted by the tflite tools.  
This script requires the latest version of tensorflow and keras among other things but if it is throwing errors I was able to attain success by rolling back both libraries to version 2.6.  
Start by creating a tflite folder in your "root folder" that the scripts will work out of.  
The script is excecuted like so:  
```
cd [path to "root folder"]  
py export_tflite_graph_tf2.py --pipeline_config_path ./models/[Model Name]/pipeline.config --trained_checkpoint_dir ./exported-models/my_model/checkpoint --output_directory ./tflite  
```
This will populate the folder with the saved_model folder as exhibited above. The variables folder should have contents but that was making github angry so I omitted it.  

##Step 2: Convert to TFLITE and add Metadata
This is a consolifation of steps 2 and 3 of the google collab.  
This is completed by running **Convert_to_TFLITE.py** in visual studio. In its current state it's pretty messy and I intend to clean it up in the future. For now I will say the file directories are self explanitory but I will make it easier to use soon.  
You should now have a tflite folder like the one above.  

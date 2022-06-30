#this is step 2 of google collab

model_name = "lite1"
model_name = "lite_model"


import tensorflow as tf
#_TFlite1_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/test/model.tflite"
_TFlite_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/tflite/model.tflite"

#converter = tf.compat.v1.lite.TFLiteConverter.from_saved_model('C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/exported-models/my_model/saved_model')
print(_TFlite_PATH)

#converter = tf.lite.TFLiteConverter.from_saved_model('C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/exported-models/my_model/saved_model')
converter = tf.lite.TFLiteConverter.from_saved_model("C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/tflite/saved_model")
converter.experimental_new_converter = True
converter.experimental_new_converter = True
converter.allow_custom_ops = True
converter.target_spec.supported_ops =[tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite = converter.convert()

with open(_TFlite_PATH, 'wb') as f:
  f.write(tflite)


from object_detection.utils import label_map_util

#this is the google collab step 3 
#https://colab.research.google.com/github/tensorflow/models/blob/master/research/object_detection/colab_tutorials/convert_odt_model_to_TFLite.ipynb#scrollTo=FT3-38PJsSOt

#Write the labelmap txt file
#_TF"+model_name+"_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/test/model.tflite"
_ODT_LABEL_MAP_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/annotations/label_map.pbtxt"
_TFLITE_LABEL_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/tflite/tflite_label_map.txt"

category_index = label_map_util.create_category_index_from_labelmap(
    _ODT_LABEL_MAP_PATH)
f = open(_TFLITE_LABEL_PATH, 'w')

len = len(category_index) #grab label qty

for class_id in range(1, len+1): #sweep thru each label and do the following:
  if class_id not in category_index:
    f.write('???/n')
    continue
  name = category_index[class_id]['name']
  f.write(name)
  f.write('/n')
f.close()

#Write the metadata to tflite model

from tflite_support import metadata
from tflite_support.metadata_writers import object_detector
from tflite_support.metadata_writers import writer_utils

_TFLITE_MODEL_WITH_METADATA_PATH = "C:/Users/cameron.circo/Documents/TensorFlow/models-master/workspace/"+model_name+"/tflite/model_with_metadata.tflite"

writer = object_detector.MetadataWriter.create_for_inference(
    #writer_utils.load_file(_TFLITE_MODEL_PATH), input_norm_mean=[127.5], 
    writer_utils.load_file(_TFlite_PATH), input_norm_mean=[127.5], 
    input_norm_std=[127.5], label_file_paths=[_TFLITE_LABEL_PATH])
writer_utils.save_file(writer.populate(), _TFLITE_MODEL_WITH_METADATA_PATH)

#Print metadata

displayer = metadata.MetadataDisplayer.with_model_file(_TFLITE_MODEL_WITH_METADATA_PATH)
print("Metadata populated:")
print(displayer.get_metadata_json())
print("=============================")
print("Associated file(s) populated:")  
print(displayer.get_packed_associated_file_list())


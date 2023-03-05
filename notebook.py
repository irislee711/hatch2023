#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator


# In[2]:


tf.__version__


# In[18]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
training_set = train_datagen.flow_from_directory('training_set',target_size=(64, 64),batch_size=32,class_mode='categorical')


# In[19]:


test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory('test_set',target_size=(64, 64),batch_size=32,class_mode='categorical')


# In[20]:


cnn = tf.keras.models.Sequential()


# In[21]:


cnn.add(tf.keras.layers.Conv2D(filters=64 , kernel_size=3 , activation='relu' , input_shape=[64,64,3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))


# In[22]:


cnn.add(tf.keras.layers.Conv2D(filters=64 , kernel_size=3 , activation='relu' ))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2 , strides=2))


# In[23]:


cnn.add(tf.keras.layers.Dropout(0.5))


# In[24]:


cnn.add(tf.keras.layers.Flatten())


# In[25]:


cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))


# In[26]:


cnn.add(tf.keras.layers.Dense(units=5 , activation='softmax'))


# In[27]:


cnn.compile(optimizer = 'rmsprop' , loss = 'categorical_crossentropy' , metrics = ['accuracy'])


# In[28]:


cnn.fit(x = training_set , validation_data = test_set , epochs = 30)


# In[40]:


from tensorflow.keras.preprocessing import image
test_image = image.load_img('Prediction/s.jpg',target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image,axis=0)
result = cnn.predict(test_image)
training_set.class_indices


# In[42]:


if result[0][0]==1:
    print('Daisy')
elif result[0][1]==1:
    print('Dandelion')
elif result[0][2]==1:
    print('Rose')
elif result[0][3]==1:
    print('Sunflower')
elif result[0][4]==1:
    print("Tulip")


# In[38]:


print(result)


# In[1]:


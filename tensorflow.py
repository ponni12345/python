import tensorflow as tf
import numpy as np

#sample training data
x=np.array([1,2,3,4],dtype=flow)
y=np.array([3,5,7,9],dtype=flow)
#define the model
model = tf.Keras.Sequential([
    tf.Keras.layers.Dense(units=1, input_shape=[1])
])                          
#compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

#Train the model
model.fit(x,y,epochs=500,verbose=0)

#predict using NumPy array
print("prediction for x = 5:", model.predict(np.array([5.0]))[0][0])


import tensorflow as tf

W = tf.Variable(tf.ones(shape=(2,2)), name="W")
b = tf.Variable(tf.zeros(shape=(2)), name="b")

@tf.function
def forward(x):
  return W * x + b

out_a = forward([1,0])
print(out_a)

out_b = forward([0,1])
regularizer = tf.keras.regularizers.l2(0.04)
reg_loss = regularizer(W)
print(out_b)
print(reg_logss)






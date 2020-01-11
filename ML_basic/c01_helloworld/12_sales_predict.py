import tensorflow as tf

xData = [1,2,3,4,5,6,7]
yData=[25000, 55000, 75000, 110000, 128000, 155000, 180000]

W = tf.Variable(tf.random.uniform([1], -100, 100))
b = tf.Variable(tf.random.uniform([1], -100, 100))
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
H = W * X + b
cost = tf.reduce_mean(tf.square(H - Y))
a = tf.Variable(0.01)                             # jump range
optimizer = tf.train.GradientDescentOptimizer(a)  # 경사하각lib
train = optimizer.minimize(cost)
init = tf.gloabl_variables_initializer()

with tf.compat.v1.Session() as sess:
  sess.run(init)
  for i in range(5001):
    sess.run(train, feed_dict={X: xdata, Y: yData})
    if i % 500 == 0:
      print (i, sess.run(cost, feed_dict={X: xdata, Y: yData}), sess.run(W), sess.run(b)  )
  print(sess.run(H, feed_dict={X: [8]}))
sess.close()


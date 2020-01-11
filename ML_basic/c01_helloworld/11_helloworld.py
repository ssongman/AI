#import tensorflow as tf
#with tf.compat.v1.Session() as sess:
#  hello = tf.constant('Hello World!')
#  print(sess.run(hello))
#sess.close()
import tensorflow as tf
hello = tf.constant ('Hello world')
sess = tf.Session()
print(sess.run(hello))


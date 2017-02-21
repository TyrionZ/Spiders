import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,100)
plt.subplot(221)  # 2行2列第1个图
plt.plot(x,x)
plt.subplot(222)
plt.plot(x,-x)
plt.subplot(223)
plt.plot(x,x*x)
plt.subplot(224)
plt.plot(x,np.log(x))
plt.show()
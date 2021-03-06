from keras.models import load_model
import numpy as np 




def mean_squared_loss(x1,x2):
	diff=x1-x2
	a,b,c,d,e=diff.shape
	n_samples=a*b*c*d*e
	sq_diff=diff**2
	Sum=sq_diff.sum()
	dist=np.sqrt(Sum)
	mean_dist=dist/n_samples
	return mean_dist

threshold=0.00041
model=load_model('AD.h5')
X_test=np.load('N3.npy')
frames=X_test.shape[2]
#Need to make number of frames divisible by 10


flag=0 #Overall video flagq

frames=frames-frames%10
X_test=X_test[:,:,:frames]
X_test=X_test.reshape(-1,227,227,10)
X_test=np.expand_dims(X_test,axis=4)


for number,bunch in enumerate(X_test):
               
                n_bunch=np.expand_dims(bunch,axis=0)
                #print("Frame num:"+str(len(n_bunch)))
                
                reconstructed_bunch=model.predict(n_bunch)
                

                loss=mean_squared_loss(n_bunch,reconstructed_bunch)
                print(loss)
                if loss>=threshold:
                        print("Anomalous bunch of frames at bunch number {}".format(number))
                        flag=1
                        n= number*10
                        t1 = n/30
                        print("Start Duration of anomaly: " +str(t1)+" second" )
                        


                else:
                        print('Bunch Normal')

               
if flag==1:
	print("Anomalous Events detected")
	



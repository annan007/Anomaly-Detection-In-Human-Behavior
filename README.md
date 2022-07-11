Step-wise instructions to execute the code.
a) The code was built and run on Anaconda environment with the help of popular APIs such as Keras, numpy, scipy and tensorflow. Also download ffmpeg. Run the Code preferably on GPU than CPU. 
b) Divide the video dataset into training set and testing set and store them under the same directory as that of the python file.
c)Run processor.py with the following command
>>python processor.py video_dir_path time_in_seconds_to_extract_one_frame
	Eg: 
	>>python processor.py ./train 5
This converts the given training video into frame and store in .npy extension file after all the data pre-processing.
d)Next we need to train a model on the training set. We make use of the Keras Sequential model with required layers defined in the file model.py. This file is then imported into train.py file where we train the model and save the model as AD.h5.To run the file we use the following command:
	>>python3 train.py n_epochs(enter integer)  
to begin training. 
e)Before testing the model, we need to convert the testing video sample to sequence of frames and store it in .npy file using the same python file (processor.py) as in Step b.
Eg: 
		>>python processor.py ./test 5
f) Finally, test the saved model AD.h5 on the test sample.
		>>python test.py

	

	



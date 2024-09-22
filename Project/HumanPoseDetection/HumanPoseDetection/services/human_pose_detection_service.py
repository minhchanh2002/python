import cv2
import numpy as np
import tensorflow as tf
from models.view_model import ViewModel

# Height and Width of Video Frame
ImageHeight, ImageWidth = 64,64

# List of classes used for Training
ClassTrainList = ['Biking','Mixing','YoYo','Billiards','Basketball','Diving','HighJump','HorseRiding','JugglingBalls','JumpRope','PizzaTossing','PlayingGuitar','PlayingPiano','TaiChi','PullUps','Punch','SkateBoarding','SoccerJuggling','Swing','WalkingWithDog']

class HumanPoseDetectionService():
    _model = None

    def __init__(self):
        if HumanPoseDetectionService._model is None:
            HumanPoseDetectionService._model = self.load_model()

    @staticmethod
    def load_model():
        if HumanPoseDetectionService._model is None:
            # Load the trained model
            HumanPoseDetectionService._model = tf.keras.models.load_model('E:/mse/imageprocessing/prsnt/HumanPoseDetection/static/model/lrcnModel.h5')
        return HumanPoseDetectionService._model

    def return_view(self, filename, detectionResult):
        view = ViewModel()
        view.link_preview_vid = 'static/upload/%s' % (filename)
        view.human_pose_detection_result = detectionResult
        return view

    def predict_single_action(self, video_file_name, video_path, seq_length):
        # Initializing the VideoCapture
        VideoReader = cv2.VideoCapture(video_path)
        OriginalVideoWidth = int(VideoReader.get(cv2.CAP_PROP_FRAME_WIDTH))
        OriginalVideoHeight = int(VideoReader.get(cv2.CAP_PROP_FRAME_HEIGHT))

        FramesList = []

        # Variable to store number of frames
        PredictedClassName = ''

        # Number of Frames in the Video
        VideoFrameCount = int(VideoReader.get(cv2.CAP_PROP_FRAME_COUNT))

        # Skip the interval once added to the list of frames
        SkipFrameWindow = max(int(VideoFrameCount / seq_length), 1)

        # Iterating the number of times equal to fixed length of seq
        for FrameCounter in range(seq_length):
            VideoReader.set(cv2.CAP_PROP_POS_FRAMES, FrameCounter * SkipFrameWindow)

            # Reading frame
            success, Frame = VideoReader.read()

            if not success:
                break

            ResizedFrame = cv2.resize(Frame, (ImageHeight, ImageWidth))

            # Normalizing the resized frame
            NormalizedFrame = ResizedFrame / 255.0

            # Appending the preprocessed frame in the list
            FramesList.append(NormalizedFrame)

        # Passing the preprocessed frame to the model to get predicted
        PredictedLabelProb = HumanPoseDetectionService._model.predict(np.expand_dims(FramesList, axis=0))[0]

        # Getting the index of the class with high probability
        PredictedLabel = np.argmax(PredictedLabelProb)

        # Class name using retrieved index
        PredictedClassName = ClassTrainList[PredictedLabel]

        prdt = f'Action Predicted: {PredictedClassName} \nConfidence: {PredictedLabelProb[PredictedLabel]}'
        print(prdt)

        # Release the VideoCapture object
        VideoReader.release()

        view = self.return_view(video_file_name, prdt)
        print(view)
        return view
# -*- coding: utf-8 -*-

from zmq import Context
from .params import Params
from .subscriber import SkeletonSubscriber, SpeechSubscriber
from .publisher import TTSPublisher

class Kinect2Client(object):
    def __init__(self, ip, params_port=33410, skel_speech_port=33405, tts_port=33406):
        self.context = Context()
        self.params = Params(ip, params_port, self.context)
        self.skeleton = SkeletonSubscriber('skeleton', ip, skel_speech_port, self.params, self.context)
        self.speech = SpeechSubscriber('recognized_speech', ip, skel_speech_port, self.params, self.context)
        self.tts = TTSPublisher(ip, tts_port, self.params, self.context)
        
    def start_all(self):
        self.skeleton.start()
        self.speech.start()
        self.tts.start()

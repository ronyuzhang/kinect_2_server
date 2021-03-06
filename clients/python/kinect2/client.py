# -*- coding: utf-8 -*-

from zmq import Context
from .subscriber import SkeletonSubscriber, SpeechSubscriber, RGBDSubscriber, MicrophoneSubscriber
from .publisher import TTSRequester

class Kinect2Client(object):
    def __init__(self, ip, speech_port=33405, skel_port=33406, tts_port=33407, color_port=33408, mapping_port=33409, mask_port=33410, audio_port=33411, param_port=33412):
        self._context = Context()
        self.skeleton = SkeletonSubscriber(self._context, ip, skel_port, param_port)
        self.speech = SpeechSubscriber(self._context, ip, speech_port, param_port)
        self.tts = TTSRequester(self._context, ip, tts_port, param_port)
        self.rgbd = RGBDSubscriber(self._context, ip, color_port, mapping_port, mask_port, param_port)
        self.mic = MicrophoneSubscriber(self._context, ip, audio_port, param_port)
        
    def start_all(self):
        self.skeleton.start()
        self.speech.start()
        self.tts.start()
        self.rgbd.start()
        self.mic.start()

    def pause_speech_recognition(self):
        self.speech.params.off()
        self.speech.params.send_params()
        
    def unpause_speech_recognition(self):
        self.speech.params.on()
        self.speech.params.send_params()

    def display_speech(self):
        self.speech.params.display()

    def display_skeleton(self):
        self.skeleton.params.display()

    def display_tts(self):
        self.tts.params.display()

    def display_rgbd_mic(self):
        self.rgbd.params.display()

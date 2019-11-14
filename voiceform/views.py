from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
import base64
from rest_framework.views import APIView 
import speech_recognition as sr
# Create your views here.
class voiceRequest(APIView):
    def get(self,request):
        dataa = request.data
        print(dataa)
        return JsonResponse({'name':'hi'},safe=False)
    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        body = request.data
        acfile = request.data['file']
        r = sr.Recognizer()
        with sr.AudioFile(acfile) as source:
            audio = r.record(source)
                                    #   ,language='en-in'
        print(r.recognize_sphinx(audio                  ))
                                                            # ,language='en-in'
        return JsonResponse({'text':r.recognize_sphinx(audio                    )},safe=False)
        # ds = Model('deepspeech-0.5.1-models/output_graph.pbmm', 26, 9, 'deepspeech-0.5.1-models/alphabet.txt', 500)
        # fs, audio = wav.read(acfile)
        # processed_data = ds.stt(audio, fs)
        # print(processed_data)
        # return JsonResponse({'text':processed_data},safe=False)
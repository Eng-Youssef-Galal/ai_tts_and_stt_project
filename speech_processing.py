from google.cloud import speech_v1 as speech
from google.cloud import texttospeech_v1 as tts

def convert_voice_to_text(voice_data):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=voice_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

def convert_text_to_voice(text):
    client = tts.TextToSpeechClient()
    synthesis_input = tts.SynthesisInput(text=text)
    voice = tts.VoiceSelectionParams(
        language_code="en-US", ssml_gender=tts.SsmlVoiceGender.NEUTRAL
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content

import openai
openai.api_key = "PUT KEY HERE"
audio_file= open("/Users/nada/Desktop/APPLE.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

import requests
from configure import *

headers = {
    "authorization": auth_token,
    "content-type": "application/json"
}

def upload_to_AssemblyAI(audio_file):

    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    print('uploading')
    upload_response = requests.post(
        upload_endpoint,
        headers=headers, data=audio_file
    )

    audio_url = upload_response.json()['upload_url']
    print('done')

    json = {
        "audio_url" : audio_url,
        "punctuate": True,
        "format_text": True,
        "iab_categories": True,
        "auto_chapters": True,
        "speaker_labels": True,
        "entity_detection": True,
        #"summarization": True,
        #"summary_model": "informative",
        #"summary_type": "bullets",
        "language_detection": True
    }

    response = requests.post(transcript_endpoint , json=json, headers=headers)
    print(response.json())

    polling_endpoint = transcript_endpoint + "/" + response.json()['id']
    return polling_endpoint


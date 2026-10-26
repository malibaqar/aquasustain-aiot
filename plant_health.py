import os, argparse
from pathlib import Path
from google import genai
from google.genai import types
if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('image');p.add_argument('--mime',default='image/jpeg');a=p.parse_args()
    client=genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    response=client.models.generate_content(model=os.environ['GEMINI_MODEL'], contents=[
        'Describe visible plant symptoms, possible causes, uncertainty and observations needed. Do not claim a confirmed diagnosis or prescribe treatment.',
        types.Part.from_bytes(data=Path(a.image).read_bytes(), mime_type=a.mime)])
    print(response.text)

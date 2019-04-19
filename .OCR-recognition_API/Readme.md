<h1>OCR-Recognition API </h1>
<h2>This repo is used to extract texts in an image using Optical Character Recognition feature provided by Google Cloud Vision API.
</h2>
1)get the necessary API key from the Google Cloud Vision API.
2)run the command

```
python cloudvisreq.py API_Key download.jpeg
```




3)The result will be the recognised text from the given image into stored into a json file.
The file json_parser.py contains the code to parse the json file .The recognised text can be used by this program.

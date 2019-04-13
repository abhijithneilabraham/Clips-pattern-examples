<h1>OCR-Recognition API </h1>
<h2>This repo is used to extract texts in an image using Optical Character Recognition feature provided by Google Cloud Vision API.
</h2>
run the command
```
python cloudvisreq.py API_Key download.jpeg
```
Before that ,get the necessary API key from the Google Cloud Vision API.


The result will be the recognised text from the given image into a json file.
The file json_parser.py contains the code to parse the json file .The recognised text can be used by this program.

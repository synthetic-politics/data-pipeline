# data-pipeline
HOW TO USE:
good quesiton

Some hints on reading and navigating the repository:
Note that in the repository on GitHub online, some of the data files (raw-data, source-data, deduplicated) are empty - this is because they are very large unprocessed zip files and thus have been included in the .gitignore. 

It was 80 GB of zipped data dawg

under the /data directory there are two folders, one-nation and comparative-contries - depending on the scraping tool used, all folders may not necessarily be used- their structure is thus:

## Elle's infinite to-do list
### One Nation
  - **Preliminary**
    - [x] Identify scraping tools + check functionality
  - **Data Collection:**
    - [x] Instagram
    - [x] Twitter
    - [ ] FaceBook
    - [ ] TikTok
    - [ ] YouTube
    - [ ] Party Website (Wayback)
    - [ ] Physical Advertisements (Trove)
  - **Data Processing:**
    - [ ] Filter posts outside of date range
    - [ ] Deduplicate data
    - [ ] Format file structure
  
### Comparative Countries
  - **Preliminary**
    - [x] Identify scraping tool for Instagram + check functionality
    - [x] Create spreadsheet with relevant parties
  - **Data Collection:**
    - [x] Run IG Grab for:
      - [x] Leaders
      - [x] Parties
  - **Data Processing**
    - [x] Ingest and unzip bulk downloads
    - [x] Write & run script to filter posts outside of date range: scripts/reorganise-comparative-countries.py
    - [ ] Run PaddleOCR on non-English images
    - [ ] Run WhisperAI on non-English videos
    
## Data Schema

```text
**00_raw**      : Raw data from the source
KeyNameLoooooong    : Value
AnotherKey          : Value
```
**00_raw**:                Raw data from the source <br />
**01_ingested**:           Unzipped and ready for processing  <br />
**02_filtered**: remove extraneous json & txt files (these may actually be useful for img context, reconsider) (For bulk downloads, also filter those not within date range)  <br />
**03_deduplicated**: Multiple copies of the same videos/images removed - DO NOT DEDUPLICATE! MULTIPLE COPIES OF AI IMAGES OUGHT TO BE NOTED IN RESULTS!  <br />
**04_formatted**: Rename and restructure files according to {YYYY-MM-DD}_{author}_{post_number}  <br />
**05_extraction**:  <br />
  **05.1_ocr_and_translate**: OCR extract text in foreign languages, save to ?json, translate json to english (PaddleOCR via API)  <br />
  **05.2_translate_and_transcribe**: whisper-AI in-memory translation, save to srt + txt... (txt may be hard to read?)

```
data-pipeline/
├── data/
│   ├── one-nation/
│   │   ├── 00_raw/
│   │   ├── 02_filter/
│   │   ├── 03_deduplicate/
│   │   └── 04_format/
│   ├── comparative-countries/
│   │   ├── 00_raw/
│   │   ├── 01_ingest/
│   │   ├── 02_filter/
│   │   ├── 04_format/
│   │   ├── 05_extract/
│   │   │   ├── 05.1_ocr_and_translate
│   │   │   └── 05.2_translate_and_transcribe
├── public/
│   ├── images/
│   │   └── logo.png
│   └── fonts/
│       └── main.woff
├── tests/
│   └── unit/
│       └── example.test.js
└── config/
    ├── dev/
    │   └── settings.json
    └── prod/
        └── settings.json
```

### Other Thoughts
- for analysis step, coding i am still ehhhh - i think as many tags as possible would be good - i.e. deepfakes, pure-ai, repeated occurence of particular AI image/repost, etc.

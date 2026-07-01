# data-pipeline
Note that many data files flagged as collected (e.g. raw, ingest) are not present - they have been deliberately excluded due to file size. Additionally, videos are not present within this repository for the same reason. I may make these accessible via a OneDrive at a later date.

## Elle's infinite to-do list
### One Nation
  - **Preliminary**
    - [x] Identify scraping tools + check functionality
  - **Raw Data Collection:**
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
  - **Raw Data Collection:**
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
00_raw           :      Raw data from the source
01_ingest        :      Unzipped and ready for processing 
02_filter        :      Filter by time range, remove extraneous files
03_deduplicate   :      Multiple copies of the same videos/images removed (PHON FOLDER ONLY!!)
04_format        :      Rename and restructure files according to {YYYY-MM-DD}_{author}_{post_number}
05_extract       :
  05.1_image     :      PaddleOCR extract text in foreign languages, translate to eng via API
  05.2_video     :      Whisper-AI in-memory translation, save to srt + txt/json
```
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

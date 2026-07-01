# data-pipeline
Welcome to ~~DaPipeline~~ data-pipeline

Some hints on reading and navigating the repository:
Note that in the repository on GitHub online, some of the data files (raw-data, source-data, deduplicated) are empty - this is because they are very large unprocessed zip files and thus have been included in the .gitignore.

under the /data directory there are two folders, one-nation and comparative-contries - depending on the scraping tool used, all folders may not necessarily be used- their structure is thus:
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
│   │   ├── 05_imageocr/
│   │   │   ├── 05.1_extract
│   │   │   └── 05.2_translate
│   │   └── 06_whisper/
│   │       ├── 06.1_translate
│   │       └── 06.1_transcribe
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
- **Elle's infinite to-do list:**
  - **One Nation**
    - **Preliminary**
      - [x] Identify platforms
      - [x] Identify scraping tools
      - [x] Check scraping tools are all functional
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
  
  - **Comparative Countries**
    - **Preliminary**
      - [x] Identify scraping tool for Instagram
      - [x] Create spreadsheet with relevant parties
      - [x] Identify timeframe of analysis
    - **Data Collection:**
      - [x] Run IG Grab for leaders + parties
      - [ x] write + run 
    - **Data Processing**
      - [x] Ingest and unzip bulk downloads
      - [x] Write & run script to filter posts outside of date range: scripts/reorganise-comparative-countries.py
    
### Data Structure Explanation

**00_raw**: Raw data from the source

**01_ingested**: Unzipped and ingested

**02_filtered**: remove extraneous json & txt files (these may actually be useful for img context, reconsider) (For bulk downloads, also filter those not within date range)

**03_deduplicated**: Multiple copies of the same videos/images removed - DO NOT DEDUPLICATE! MULTIPLE COPIES OF AI IMAGES OUGHT TO BE NOTED IN RESULTS!

**04_formatted**: Rename and restructure files according to {YYYY-MM-DD}_{author}_{post_number}

**05_imageocr**:
  **05.1_extract**: OCR extract text in foreign languages, save to ?json
  **05.2_translate**: translate json to english (PaddleOCR via API)
  (note this step may be done in single script, i.e. extract foreign text, but only save eng to disk)

**06_whisper**:
  **06.1_translate**: whisper in-memory
  **06.2_transcribe**: save to srt + txt... (txt may be hard to read?)

HOW TO USE:
good quesiton

coding i am still ehhhh - i think as many tags as possible would be good - i.e. deepfakes, pure-ai, etc.

Note: Videos are too large to be stored within the repo, hence this is images only

## FAQ
Help

![Architecture](docs/data-pipeline.svg)

Source: [architecture.drawio](docs/data-pipeline.drawio)

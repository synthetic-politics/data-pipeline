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
│   │   ├── 01_ingest/
│   │   ├── 02_filter/
│   │   ├── 03_deduplicate/
│   │   └── 04_format/
│   ├── comparative-countries/
│   │   ├── 00_raw/
│   │   ├── 01_ingest/
│   │   ├── 02_filter/
│   │   ├── 03_deduplicate/
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
    - **Data Collection:**
      - [x] Instagram
      - [x] Twitter
      - [ ] FaceBook
      - [ ] TikTok
      - [ ] YouTube
      - [ ] Party Website (Wayback)
      - [ ] Physical Advertisements (Trove)
  - **Comparative Countries**
  - 
  - **Data Collection:**
    - [x] data-pipeline/party_table.xlsx
    - [ ] Run insta-grab for leaders + parties
    - [ ] write + run data-pipeline/scripts/reorganise-comparative-countries.py
  - **Data analysis**

Data analysis 

Data Processing

#### One Nation
**00_raw**: Raw data from the source

**01_ingest**: Unzipped and ingested

**02_filter**: remove extraneous json & txt files (these may actually be useful for img context, reconsider) (For bulk downloads, also filter those not within date range)

**03_deduplicate**: Multiple copies of the same videos/images removed

**04_format**: Rename and restructure files according to {YYYY-MM-DD}_{author}_{post_number}

#### Comparative Countries
**00_raw**: Raw data from the source

**01_ingest**: Unzipped and ingested

**02_filter**: remove extraneous json & txt files (these may actually be useful for img context, reconsider) (For bulk downloads, also filter those not within date range)

**03_deduplicate**: Multiple copies of the same videos/images removed - DO NOT DEDUPLICATE! MULTIPLE COPIES OF AI IMAGES OUGHT TO BE NOTED IN RESULTS!

**04_format**: Rename and restructure files according to {YYYY-MM-DD}_{author}_{post_number}

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

![Architecture](docs/data-pipeline.svg)

Source: [architecture.drawio](docs/data-pipeline.drawio)

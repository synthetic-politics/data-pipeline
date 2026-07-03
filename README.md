# Elle's infinite to-do list aka the data-pipeline
Note that many data files flagged as collected (e.g. raw, ingest) are not present - they have been deliberately excluded due to file size. Additionally, videos are not present within this repository for the same reason. I may make these accessible via a OneDrive link or similar at a later date.

# 
## One Nation
### Preliminary 
- [ ] Identify scrapers & verify functionality
  - [x] Instagram - [IG Grab](https://addons.mozilla.org/en-US/firefox/addon/ig-grab/)
  - [x] Twitter/X - [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
  - [ ] Facebook - [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
  - [ ] TikTok - ?
  - [x] YouTube - [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [x] Verify Wayback Machine functionality
- [ ] Verify Trove functionality
### Raw Data Collection

| Account | Instagram | Twitter/X | Facebook | TikTok | YouTube |
|---------|:---------:|:---------:|:--------:|:-------:|:-------:|
| One Nation | <ul><li>[x]</li><li> | ✓ | - [ ] | - [ ] | - [ ] |
| Pauline Hanson | - [ ] | - [ ] | - [ ] | - [ ] | - [ ] |

- [ ] Party Website (via [Wayback Machine](https://web.archive.org/))
- [ ] Physical Advertisements (via [Trove](https://trove.nla.gov.au/))
### Data Processing
  - [ ] Filter posts outside of date range
  - [ ] Deduplicate images/videos with [idealo/imagededup](https://github.com/idealo/imagededup)
  - [ ] Format file structure
### Data Analysis
- [ ] TruthScan computer analysis for AI
- [ ] Human analysis for AI
### Completed
 - [ ] Verified total non-use of AI imagery
  
## Comparative Countries
### Preliminary
- [x] Identify scraping tool for Instagram + check functionality
- [x] Create spreadsheet with relevant parties
### Raw Data Collection
- [x] Parties 
  - [x] One Nation
  - [x] People's Party of Canada
  - [x] Reform UK
  - [x] National Rally
  - [x] Party for Freedom
  - [x] Progress Party
  - [x] Vlaams Belang
  - [x] Alternative for Germany
  - [x] Patriots for Europe
- [x] Leaders
  - [x] Pauline Hanson
  - [x] Maxime Bernier
  - [x] Nigel Farage
  - [x] Jordan Bardella (France)
  - [x] Geert Wilders
  - [x] Sylvi Listhaug
  - [x] Tom Van Grieken
  - [x] Alice Weidel
  - [x] Jordan Bardella (EU)
### Data Processing
- [x] Ingest and unzip bulk downloads
- [x] Write & run script to filter posts outside of date range: scripts/reorganise-comparative-countries.py
- [ ] Run PaddleOCR on non-English images (Optical Character Recognition)
  - [ ] Transcribe foreign characters -> Foreign text
  - [ ] Translate foreign text -> English
- [ ] Run WhisperAI on non-English videos (Automatic Speech Recognition)
  - [ ] Transcribe foreign audio -> Foreign text
  - [ ] Translate foreign text -> English text
### Data Analysis
- [ ] Preliminary Quantiative Analysis.
- [ ] 
- [ ] Code for recurring themes
- [ ] Better define structure of analysis, presently:
  - [ ] Bivariate analysis via chi-square
  - [ ] Logistic regression analysis / multivariate analysis


### Completed
 - [ ] All data synthesised for final analysis


Further Literature review

Final Qualitative
    
# Data Schema
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
- when coding (analysis), as many relevant tags as possible would be good - i.e. deepfakes, pure-ai, repeated occurence of particular AI image/repost, etc.

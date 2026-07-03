# Task Checklist
aka Elle's infinite to-do list - For a table of relevant parties, leaders, election dates, etc., see [here](/party-table)
## One Nation
### Preparation 
- [ ] Identify scrapers & verify functionality
  - [x] Instagram - [IG Grab](https://addons.mozilla.org/en-US/firefox/addon/ig-grab/)
  - [x] Twitter/X - [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
  - [ ] Facebook - [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
  - [ ] TikTok - ?
  - [x] YouTube - [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [x] Verify Wayback Machine functionality
- [ ] Verify Trove functionality
### Raw Data Collection

Here's the table restructured vertically:

| Platform | One Nation | Pauline Hanson |
|---------|:---------:|:---------:|
| Instagram | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Twitter/X | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Facebook | <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |
| TikTok | <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |
| YouTube | <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |

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
### Preparation
- [x] Identify scraping tool for Instagram + check functionality
- [x] Create spreadsheet with relevant parties
### Raw Data Collection
| Country / Region | Party | Leader |
|:---|:---:|:---:|
| Australia | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Canada | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| United Kingdom | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| France | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Netherlands | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Norway | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Belgium | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| Germany | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |
| European Union | <ul><li>- [x] </li></ul> | <ul><li>- [x] </li></ul> |

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
- [ ] Preliminary Quantiative
  - [ ] TruthScan computer analysis for AI
  - [ ] Human analysis for AI
  - [ ] Aggregate total/percentage AI usage across parties/countries
- [ ] Coding
  - [ ] Code for recurring themes
  - [ ] Finalise sample size
- [ ] Primary Quantitative
  - [ ] Better define structure/function of analysis
  - [ ] Bivariate analysis via chi-square
  - [ ] Logistic regression analysis / multivariate analysis
  - [ ] Identify themes that correlate most strongly with AI usage
### Completed
 - [ ] All data synthesised for final analysis

## Further Literature to Review
### Culture & Strategy:
- [ ] Anglo-Celtic Australian Culture +
- [ ]  **Perception** of Anglo-Celtic Australian culture shaping strategic choice
  - [ ] Tall Poppy Syndrome
  - [ ] Anti-intellectualism
  - [ ] Aversion to / slow adoption of new technologies
### Organisation & Capacity: * Expand this
 - [ ] One Nation organisational
 - [ ] One Nation capacity-based

## Final Qualitative Analysis
- [ ] Evaluate if passive or active
- [ ] Evaluate pillars:
  - [ ] Ideological (Discuss methodological findings, PHON vs rest)
  - [ ] Organisation
  - [ ] Capacity
  - [ ] Culture
  - [ ] Strategy
    
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

### Notes
- when coding (analysis), as many relevant tags as possible would be good - i.e. deepfakes, pure-ai, repeated occurence of particular AI image/repost, etc.
- Many data files flagged as collected (e.g. raw, ingest) are not present - they have been deliberately excluded due to file size. Additionally, videos are not present within this repository for the same reason. I may make these accessible via a OneDrive link or similar at a later date.

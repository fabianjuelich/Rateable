# Rateable
![Icon](assets/Icons/icons8-f%C3%BCnf-von-f%C3%BCnf-sternen-64.png)

### Rateable is a multiplatform desktop application that allows users to scrape and collect rating data from Audible for any audiobook files (Provided that the folder names used as keywords are chosen wisely). The collected data can be stored in an Excel file and as ID3-tag.
### In this way, Rateable provides a convenient way to organize and analyze audiobook ratings and other information to help you decide which book to listen to next.

## Features

- Ratings: Scrapes rating data for each audiobook based on the folder name from Audible (The remaining time is calculated and displayed).
- Metadata: Fetches audiobook metadata for enhanced information (Choose from ID3 or Audible information).
- ID3-tag Updates (ToDo): Writes rating stars (and other metadata if not already available) to the audiobook file ID3-tag.
- Rating Updates: Refresh ratings for previous audiobooks to keep them up to date.
- Permanent Storage: Stores collected rating data permanently in a database and also saves it to an Excel sheet.
- Batch Selection: Batch processing for folders containing multiple audiobooks (Recursive search).

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Follow the instructions to download the [Chromium browser](https://www.chromium.org/getting-involved/download-chromium) and its [driver](https://chromedriver.chromium.org/downloads) for your os and place them in the [assets folder](assets/) (possibly you have to edit associated paths in the [constructor](src/scraper.py)).
4. Optional: Customize the TLD used for scraping the Audible website.
5. Run the app using `python main.py` (optionally package to make it executable).

## Usage

1. Launch the Rateable application.
2. Click "Open Explorer" to select the folder containing the audiobook files.
3. Decide which source to use for metadata retrieval
3. Confirm the selection, and the application will start scraping the rating data for each audiobook.
4. If using the application for the first time, specify the save path for the Excel file.
5. Open the Excel file by clicking "Open result".
6. To update ratings for previous audiobooks, click "Update".

## Screenshots

![start-screen](assets/Screenshots/start-screen.png)
![result](assets/Screenshots/result.png)

## Credits

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [SQLite3](https://www.sqlite.org/index.html)
- [Audible](https://www.audible.de/)
- [icons8](https://icons8.de/)

## Contributing

Contributions are welcome! Please create a new issue or submit a pull request for any issues or suggestions for improvements.
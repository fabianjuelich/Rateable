# Rateable

Rateable is a multiplatform desktop application that allows users to scrape and collect rating data from Audible for chosen audiobooks. The collected data can be stored in an Excel file and as ID3-tags. Rateable provides a convenient way to organize and analyze audiobook ratings.

## Features

1. **Scraping and Rating**: Utilizes a scraper to fetch the rating data for each audiobook based on the folder name.
2. **Batch Selection**: Folders containing multiple audiobooks can be selected, enabling batch processing.
3. **Rating Updates**: Users can update the ratings for previously selected audiobooks.
4. **Permanent Storage**: The collected rating data is stored permanently and can be saved to an Excel sheet for easy reference.
5. **Metadata Handling** (ToDo): The application reads and adds metadata from the audiobooks to enhance the information available.
6. **ID3-tag Integration** (ToDo): The rating stars can be written to the ID3-tag of the audiobook file, allowing easy access to ratings in various media players.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Follow the provided [steps to install the Chromium browser and its driver](https://www.chromium.org/getting-involved/download-chromium/#downloading-old-builds-of-chrome-chromium), which needs to be moved into the [assets folder](assets/).
4. Run the app with a working internet connection using `python main.py` (optionally package with pyinstaller.sh to make it executable).

## Usage

1. Launch the Rateable application.
2. Click the "Open Explorer" button to select the folder containing the audiobook files.
3. Once the folder is selected, click the "Confirm" button to proceed.
4. If it's the first time using the application, you will be prompted to specify the save path for the Excel file. Choose the desired location and provide a name for the file.
5. The application will start scraping the rating data for each audiobook.
6. Once the scraping process is complete, the rating data will be stored in the Excel file.
7. To update the ratings for previously selected audiobooks, click the "Update" button.
8. The application will fetch the updated rating data and update the Excel file accordingly.
9. You can open the Excel file by clicking the "Open result" button.

## Screenshots

Insert screenshots of the application here.

## Credits

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [SQLite3](https://www.sqlite.org/index.html)
- [Audible](https://www.audible.de/)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.
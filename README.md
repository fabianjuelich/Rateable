# Rateable
![Icon](assets/Icons/icons8-f%C3%BCnf-von-f%C3%BCnf-sternen-64.png)

Rateable is a multiplatform desktop application that allows users to scrape and collect rating data from Audible for any audiobook files. The collected data can be stored in an Excel file and as ID3-tag. Rateable provides a convenient way to organize and analyze audiobook ratings.

## Features

1. **Scraping and Rating**: Utilizes a scraper to fetch the rating data for each audiobook based on the folder name.
2. **Batch Selection**: Folders containing multiple audiobooks can be selected, enabling batch processing.
3. **Rating Updates**: Users can update the ratings for previous audiobooks so they stay up to date.
4. **Permanent Storage**: The collected rating data is stored permanently and can be saved to an Excel sheet for easy reference.
5. **Metadata** (ToDo): If present, the application handles the audiobook files metadata to enhance the information available. Otherwise the metadata from Audible is used.
6. **ID3-tag** (ToDo): The rating stars (and other metadata if not already available) can be written to the ID3-tag of the audiobooks files, allowing easy access to ratings in various media players.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Follow the provided instructions to install the [Chromium browser](https://www.chromium.org/getting-involved/download-chromium) and its [driver](https://chromedriver.chromium.org/downloads), which needs to be moved into the [assets folder](assets/).
4. Optional: For possibly better matches, you can change the TLD used to scrape the Audible website to your own.
5. Run the app with a working internet connection using `python main.py` (optionally package with pyinstaller.sh to make it executable).

## Usage

1. Launch the Rateable application.
2. Click the "Open Explorer" button to select the folder containing the audiobook files.
3. Once the folder is selected, click the "Confirm" button to proceed. The application will start scraping the rating data for each audiobook.
4. If it's the first time using the application, you will be prompted to specify the save path for the Excel file. Choose the desired location and provide a name for the file. Once this is complete, the rating data will be stored in the Excel file.
5. To update the ratings for previous audiobooks, click the "Update" button. The application will fetch the latest rating data and update the Excel file accordingly.
6. You can open the Excel file by clicking the "Open result" button.

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

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.
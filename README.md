# Instagram Followers & Following Checker

This Python script helps you analyze your Instagram connections by comparing your followers and following lists. It identifies who follows you back and who doesn't.

## Features
- Lists all your Instagram connections and marks who follows you back.
- Identifies users you follow who do not follow you back.

## Requirements
- Python 3.1 or higher

## Downloading Your Instagram Data
To obtain the necessary JSON files from Instagram:
1. Open Instagram on your web browser.
2. Go to **Settings** > **Privacy and Security**.
3. Scroll down to **Data Download** and click **Request Download**.
4. Choose **JSON** as the format and submit the request.
5. Once you receive an email from Instagram, download the ZIP file and extract it.
6. Locate `followers_1.json` (followers list) and `following.json` (following list) inside the extracted folder.

## Installation
1. Clone this repository or download the script.
2. Ensure you have the required JSON files:
   - `followers_1.json` (Contains your followers list)
   - `following.json` (Contains your following list)
3. Place these files inside the `files` directory inside the project.

## Usage
1. Run the script using:
   ```sh
   python main.py
   ```
2. Choose an option:
   - `1` to see all connections (who follows you back and who doesn't).
   - `2` to see a list of people who do not follow you back.

## Example Output
```
1. Show all connections
2. Show Non Followers
Enter Your Choice: 2

People not following you: 
❌  : user1
❌  : user2
❌  : user3
```

## Notes
- Ensure that your JSON files are correctly formatted.
- The script does not interact with Instagram; you must download your data manually.

## License
This project is licensed under the MIT License.


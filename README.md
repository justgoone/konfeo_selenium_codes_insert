# konfeo_selenium_codes_insert
Software used to add bigger amounts of discount codes to konfeo.com

First, make sure you have both Selenium and selenoium Chrome WebDriver installed on your PC. Make sure that the Web Driver is in correct spot (Program Files (x86) by default)
To make sure the app works correctly change the code to have correct links where 'konfeo.com event discounts screen' text is. The links may be aquired by navigating to the event page and clicking 'Rabaty'. It schould look something like 'https://admin.konfeo.com/events/(your event number)/discounts'.
After that make sure to have a correctly prepared file with codes in the same folder as the app. Example may be found in this repository under 'example_codes.csv'
When done correctly, you can now activate the .py app. CMD window will appear prompting you to input your konfeo.com login credentials. After imputing them, the app will do the rest.

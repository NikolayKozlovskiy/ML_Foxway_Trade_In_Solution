# Manually labeling data

Go through images in any folder that is named `Front ON` or `Front OFF`.
* If it isn't a phone, ignore it.
* Otherwise, rename the file in the following format: `label1_label2_label3_x`
  * `label1`, `label2` etc. are labels for machine learning purposes.
  * `x` is the original file name, including the extension. Leave it intact, we need unique file names.

This is a list of possible labels:
* If the phone has a cracked screen, add label `crack`.
* If the screen is turned on and the LCD is damaged, add label `lcd`.
* If it's an iPhone, add label `iphone`.
* If it's a Samsung, add label `samsung`.

The absence of a label indicates the opposite, e.g when the `crack` label is absent, we can tell that the screen is not cracked.

For example, if it's a samsung with a cracked screen and no lcd damage, the file name would be `samsung_crack_x`.

But if it's neither iPhone nor Samsung, the screen has visible damage on lcd screen, but there are no cracks in the glass, the file name would be `lcd_x`.

After renaming the file, download it and commit the image to `data` folder in this repository.
    
Ration excel file - https://docs.google.com/spreadsheets/d/1iF9JLFY9ve21WCrhPkEhbsDxwj9lB-c7bGtVF0zD3BU/edit#gid=0 
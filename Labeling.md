# Manually labeling data

Go through images in any folder that is named `Front ON` or `Front OFF`.
* If it isn't a phone, ignore it.
* Otherwise, rename the file in the following format: `label1_label2_label3_x`
  * `label1`, `label2` etc. are labels for machine learning purposes.
  * `x` is the original file name, including the extension. Leave it intact, we need unique file names.

This is a list of possible labels:
* If the phone has a cracked screen, add label `crack`.
* If the screen has LCD damage, add label `lcd`.
* If the screen is turned on, add label `on`.
* If it's an iPhone, add label `iphone`.
* If it's a Samsung, add label `samsung`.

The absence of a label indicates the opposite, e.g when the `crack` label is absent, we can tell that the screen is not cracked.

For example, if it's a samsung with a cracked screen and the screen is turned off, the file name would be `samsung_crack_x`.

But if it's neither iPhone nor Samsung, the screen is turned on and it's in perfect condition, the file name would be `on_x`.

After renaming the file, download it and commit the image to `data` folder in this repository.
    

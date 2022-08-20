DESCRIPTION
------------------
This software analyzes Google reviews in a graph vs time.
This repository contains the source code as well as a frozen version for Win10 64-bit (by cx_freeze),
which can be found zipped in the "freeze" subfolder.
In case you only want to use the software (and not modify it), you only have to download the "freeze" folder.


SETUP
------------------

The software depends on the Chormedriver webdriver, which is available here:
https:**chromedriver.chromium.org/

The Chromedriver version needs to match your installed version of the Chrome browser.

This software comes with a chromedriver.exe suitable for Chrome version 104.
If you use a different version of Google Chrome, you have to download the corresponding
Chromedriver version from the <a href=https://chromedriver.chromium.org/>Chromedriver homepage</a>, and replace 
chromedriver.exe in the "resources" subfolder (Note: when using the frozen version, the resources folder can be 
found in the "gorealyzer_Win10" folder after unpacking the zipfiles in the "freeze" folder).

The "make.bat" file generates the freeze using cx_freeze, which needs to be installed when you want to use it (Windows only).


DEPENDENCIES
-------------------
When using the source code, you need the following software/libraries installed:

* Python 3.7.6 or graeter
* Numpy
* Matplotlib
* Pandas
* Selenium
* Beautiful Soup
* cx_freeze (in case you want to use make.bat, Windows only)


USAGE
-------------------
* First, paste the url of the Google maps site of the site you want to analyze into the topmost text field.
* The required url can easily be acquired in the following way:
1. Go to https:**www.google.com/maps/
2. Enter the name of your reqired site in the Google Maps search field
3. When the location is shown, hit the link below the name of the site "xxx Reviews"
4. Paste the url into the Gorealyzer text field
* Hit "Load Reviews from web".
* The Reviews are scraped from Google. Depending on the number of reviews, this may take several minutes.
* After successfully loading the reviews, there are 3 analysis functions availiable:
1. "Plot unmodified data": plots the data in the time bins as they come from Google. May result in high fluctuations.
2. "Plot binned data": plots the data in a fixed amount of logarithmically spaced bins. The number of bins has to be given in the text field on the
right hand side.
3. "Plot downsampled data": combines the data into bins containing the same number of (original) data points. The number of data points that are 
combined into one bin needs to be given in the text field on the right hand side.

LEGAL
--------------------
Chormedriver (which is used by this software) is licensed under the <a href=http:**https://opensource.org/licenses/BSD-3-Clause>BSD-3-Clause</a>.

See full Chromedriver licensing information <a href=https://chromium.googlesource.com/chromium/src/+/HEAD/LICENSE>here</a>.

Following you find a copy of the Chromedriver licensing information:

**Copyright 2015 The Chromium Authors. All rights reserved.**

**Redistribution and use in source and binary forms, with or without**
**modification, are permitted provided that the following conditions are**
**met:**

* **Redistributions of source code must retain the above copyright**
**notice, this list of conditions and the following disclaimer.**
* **Redistributions in binary form must reproduce the above**
**copyright notice, this list of conditions and the following disclaimer**
**in the documentation and/or other materials provided with the**
**distribution.**
* **Neither the name of Google Inc. nor the names of its**
**contributors may be used to endorse or promote products derived from**
**this software without specific prior written permission.**

**THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS**
**"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT**
**LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR**
**A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT**
**OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,**
**SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT**
**LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,**
**DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY**
**THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT**
**(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE**
**OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.**






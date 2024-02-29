# Webpages Ping Test with Robot Framework

This Robot Framework project involves downloading a text file, reading its content, and performing tests on the webpages listed in the file.

## Getting Started

1. **Download the text file:**
   Download the text file "webpages.txt" from the following link and save it to your computer: [webpages.txt](https://drive.google.com/file/d/1oh29H14-WkGuRuHchN5M6fg3gQ7Tbae3/view)

2. **Install Robot Framework:**
   Make sure you have Robot Framework installed on your system. You can install it using the following command:

   ```bash
   pip install robotframework

## Program tasks 

1. Read the webpages.txt information using Robot Framework into a variable.

2. Ping each address found in the text file. (for mac: ping [host] -c 4) <- restricts ping packages to 4

3. Use RF to capture the IP and ping time of each pinged site. Test that the time taken for Ping is less than 50ms.

4. Create a new txt-file in which you enter the IP address of the pinged site and the average ping- time for the site.

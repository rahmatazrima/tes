import urllib.request
import os
# Open the file and read the URLs
with open('link.txt', 'r') as file:
   urls = file.readlines()

# Create the 'html' directory if it doesn't exist
if not os.path.exists('html'):
   os.makedirs('html')

# Download the HTML of each URL
for i, url in enumerate(urls):
   url = url.strip() # Remove any leading/trailing white space
   try:
       # Open the URL
       with urllib.request.urlopen(url) as response:
           # Read the HTML content
           html = response.read().decode('utf-8')

           # Save the HTML content to a file
           with open(f'html/page_{i}.html', 'w', encoding='utf-8') as file:
               file.write(html)
   except Exception as e:
       print(f'Failed to download HTML from {url}: {e}')

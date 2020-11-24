# Usage: screenshot should be called "image.png" and be in the same directory.

from PIL import Image
import pytesseract
import re
from datetime import datetime
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'


image = Image.open("image.png")
text = pytesseract.image_to_string(image)
# print(text)

item = input("What is the name of item (camel cased)?\n") 
date = input("Breach date in yyyy-mm-dd format?\n")
month = str(date[5:7])
# print(month)
if month == "01":
	month_name = "Jan"
elif month == "02":
	month_name = "Feb"
elif month == "03":
	month_name = "Mar"
elif month == "04":
	month_name = "Apr"
elif month == "05":
	month_name = "May"
elif month == "06":
	month_name = "Jun"
elif month == "07":
	month_name = "Jul"
elif month == "08":
	month_name = "Aug"
elif month == "09":
	month_name = "Sep"
elif month == "10": 
	month_name = "Oct"
elif month == "11":
	month_name = "Nov"
elif month == "12":
	month_name = "Dec"
else:
	print("Sorry, I wasn't able to figure out the month from the date you put in")
	sys.exit()

date_reformatted = month_name + str(date[8:10]) + str(date[0:4])
today_date = datetime.today().strftime('%Y-%m-%d')
today_date_for_path_1 = str(today_date.translate({ord('-'): '/'}))
today_date_for_path_2 = str(today_date.translate({ord('-'): None}))

class Correct_Answers:
	def __init__(self):
		self.title = "<REDACTED> from {site} {date}".format(site=website, date=date_reformatted)
		self.source = "<REDACTED>"
		self.source_type = "<REDACTED>"
		self.format_field = 'Username'
		self.delimiter = ":"
		self.auto_name_extracted_files = "No"
		self.best_effort_extraction = "No"
		self.tlp = "<REDACTED>"
		self.discovered_at = str(today_date)
		self.loaded_at = date 
		self.final = item.lower()
		self.path_to_file = "<REDACTED>" + today_date_for_path_1 + "/" + today_date_for_path_2 + "_" + website.lower() + "_" + date_reformatted + "_reformatted.txt"

good_to_go = True
answers = Correct_Answers()
print("If I find any problems, I'll mention them now, please wait...\n")
time.sleep(1)
if not re.search(answers.dump_title, text):
	print("Title should be:")
	print(answers.title + "\n")
	good_to_go = False
re.sub(answers.title, "foobar", text, 1)

if not re.search(answers.source, text):
	print("Source should be:")
	print(answers.source + "\n")
	good_to_go = False
re.sub(answers.dump_source, "foobar", text, 1)

if not re.search(answers.source_type, text):
	print("Source Type should be:")
	print(answers.source_type + "\n")
	good_to_go = False
re.sub(answers.source_type, "foobar", text, 1)

if not re.search(answers.format_field, text):
	print("\"Format\" should be:")
	print(answers.format_field + "[delimiter]<REDACTED>"+ "\n")
	good_to_go = False
re.sub(answers.format_field, "foobar", text, 1)

if not re.search(answers.delimiter, text):
	print("delimiter should be:")
	print(answers.delimiter + "\n")
	good_to_go = False
re.sub(answers.delimiter, "foobar", text, 1)

if not re.search(answers.auto_name_extracted_files, text):
	print("auto name extracted files is set to \"Yes\"... are you sure that's what you want? I was expecting to see:")
	print(answers.auto_name_extracted_files + "\n")
	good_to_go = False
re.sub(answers.auto_name_extracted_files, "foobar", text, 1)

if not re.search(answers.best_effort_extraction, text):
	print("Best Effort Extraction set to \"Yes\"... are you sure that's what you want? I was expecting to see:")
	print(answers.best_effort_extraction + "\n")
	good_to_go = False
re.sub(answers.best_effort_extraction, "foobar", text, 1)

if not re.search(answers.tlp, text):
	print("<REDACTED I was expecting to see:")
	print(answers.tlp + "\n")
	good_to_go = False
re.sub(answers.tlp, "foobar", text, 1)

if not re.search(answers.discovered_at, text):
	print("\"discovered at\" should should have this base date:")
	print(answers.discovered_at + "\n")
	good_to_go = False
re.sub(answers.discovered_at, "foobar", text, 1)

if not re.search(answers.loaded_at, text):
	print("\"<REDACTED\" should have this base date:")
	print(answers.loaded_at + "\n")
	good_to_go = False
re.sub(answers.loaded_at, "foobar", text, 1)

if not re.search(answers.final, text):
	print("<REDACTED should be:")
	print(answers.final + "\n")
	good_to_go = False
re.sub(answers.final, "foobar", text, 1)

if not re.search(answers.path_to_file, text):
	print("The date in <REDACTED to file does not match today's date, or the name is not the same, but that should be okay if it was reformatted earlier. This is what I was expecting:")
	print(answers.path_to_file + "\n")
	good_to_go = False

if good_to_go == False:
	print("I may have made a mistake and you may be okay! But those are the sections I would check.")
	sys.exit()
else:
	print("Good to go!")

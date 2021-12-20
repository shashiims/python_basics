import date_extractor
text = "I arrived in that city on 2020,feb 10"
date = date_extractor.extract_dates(text)
print(date)

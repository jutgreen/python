# creating a dictionary
# converting 3 digit month name to full month
# defining key value pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Meh"))
print(monthConversions.get("Meh", "Not a valid key"))
print(monthConversions.get("7"))
print(monthConversions.get("07", "Not a valid key"))
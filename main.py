from requests import get

websites = [
  "Google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tikto.com"
]

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"

  print(website)
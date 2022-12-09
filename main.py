from requests import get

websites = [
  "Google.com", "airbnb.com", "https://twitter.com", "facebook.com",
  "https://tiktok.com"
]

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"

  response = get(website)
  print(response.status_code)  #결과 값이 코드로만 나옴

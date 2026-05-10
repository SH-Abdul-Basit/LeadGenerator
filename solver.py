import capsolver

capsolver.api_key = "CAP-27EDD522E101C9BA91C25953DFE321E54640E1EDA571F7B697FEF1B10D607590"

def solve_recaptcha_v2(url, key):
    # 2. Configure the task
    solution = capsolver.solve({
        "type": "ReCaptchaV2TaskProxyless",
        "websiteURL": url,
        "websiteKey": key,
    })
    return solution

PAGE_URL = "https://www.google.com/recaptcha/api2/demo"
PAGE_KEY = "6Le-wvkSAAAAAPBMRTvw0QKyMSQ_R6GYYs7j4m-M" # Demo Key

print("Solving reCaptcha v2...")
result = solve_recaptcha_v2(PAGE_URL, PAGE_KEY)
print("Solution Token:", result.get("gRecaptchaResponse"))
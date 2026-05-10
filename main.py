from google import genai
from seleniumbase import SB
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEN_API_KEY")
client = genai.Client(api_key=API_KEY)



with SB(uc=True, incognito=True, xvfb=True) as sb:
    url = "https://www.google.com"
    # url = 'https://www.google.com/search?q=site:instagram.com+"Restaurants"+"USA"+"@gmail.com"&num=100'
    sb.uc_open_with_reconnect(url)
    # time.sleep(10)
    # sb.uc_gui_click_captcha()
    sb.send_keys('[name="q"]', 'site:instagram.com "Restaurants" "USA" "@gmail.com"\n')
    #
    # MAX_PAGE_SEARCH = 10
    #
    total_page_content = ""

    for i in range(25):
        content_section = sb.find_element("body")
    # while content_section:
    #     print("d")
        total_page_content += content_section.text
        buttons = sb.find_elements(".oeN89d")
        for btn in buttons:
            if btn.text == "Next":
                sb.driver.execute_script("arguments[0].setAttribute('id', 'auto-next-btn');", btn)

                # sb.assert_element("#auto-next-btn")

                sb.driver.uc_click("#auto-next-btn")
                # sb.driver.uc_switch_to_frame("iframe")
                # sb.uc_gui_click_captcha("span.recaptcha-checkbox")
                # btn.click()
                # sb.reconnect(4)
        # break

        # content_section = sb.find_element("body")

    content = """CREATE A TABLE IN CSV FORMAT AND FORMAT THE ABOVE DATA, AND CREATE A COLUMN FOR COUNT, FIRST NAME, LAST NAME, COMPANY NAME, COMPANY WEBSITE, INSTAGRAM LINK, EMAIL.

    HERE ARE SOME RULES:

    DON'T ADD ENTRIES THAT DON'T HAVE FIRST NAME OR EMAIL.
    DON'T REPEAT ENTRIES, USE THE FIRST OCCURRENCE.\n""" + total_page_content

    # print(content)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=content
    )

    print(response.text)
    with open("output.csv", "w") as file:
        file.write(response.text)



#
# # client = genai.Client(api_key=API_KEY)
# #
# driver = Driver(uc=True, incognito=True)
#
# driver.get("https://www.google.com")
#
# search_box = driver.find_element(By.NAME, "q")
#
# search_box.send_keys('site:instagram.com "Restaurants" "USA" "@gmail.com"')
# # search_box.send_keys('gmtk')
# # search_box.send_keys('H')
# search_box.send_keys(Keys.RETURN)
#
#
# # for i in range(MAX_PAGE_SEARCH):
# content_section = driver.find_element(By.TAG_NAME, "body")
# while content_section:
# #     print("d")
#     total_page_content += content_section.text
#     buttons = driver.find_elements(By.CLASS_NAME, "oeN89d")
#     for btn in buttons:
#         if btn.text == "Next":
#             btn.click()
#
#     content_section = driver.find_element(By.TAG_NAME, "body")
#
#
# # print(total_page_content)
# content = """CREATE A TABLE IN CSV FORMAT AND FORMAT THE ABOVE DATA, AND CREATE A COLUMN FOR COUNT, FIRST NAME, LAST NAME, COMPANY NAME, COMPANY WEBSITE, INSTAGRAM LINK, EMAIL.
#
# HERE ARE SOME RULES:
#
# DON'T ADD ENTRIES THAT DON'T HAVE FIRST NAME OR EMAIL.
# DON'T REPEAT ENTRIES, USE THE FIRST OCCURRENCE.\n""" + total_page_content
#
# # response = client.models.generate_content(
# #     model="gemini-2.5-flash",
# #     contents=content
# # )
#
#
# # print(response.text)
#
# # driver.close()
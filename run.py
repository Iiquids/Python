import asyncio
import aiohttp

async def postData():
    async with aiohttp.ClientSession() as session:
        # First POST request
        post_url = 'https://middletowncityschools.infinitecampus.org/campus/verify.jsp'
        post_payload = {
            'username': '1504573',
            'password': 'B#102506',
            'portalUrl': 'portal/students/mcsd.jsp?&rID=0.4447194889849019',
            'appName': 'mcsd',
            'url': 'nav-wrapper',
            'lang': 'en',
            'portalLoginPage': 'students'
        }
        post_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        await session.post(post_url, data=post_payload, headers=post_headers, ssl=False)

        # Second GET request
        term_url = 'https://middletowncityschools.infinitecampus.org/campus/resources/portal/roster?_expand=%7BsectionPlacements-%7Bterm%7D%7D&_date=2024-04-15'
        term_headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'expires': '0',
            'referrer': 'https://middletowncityschools.infinitecampus.org/campus/apps/portal/student/home',
            'referrerPolicy': 'strict-origin-when-cross-origin',
        }
        async with session.get(term_url, headers=term_headers, ssl=False) as term_response:
            term_data = await term_response.json()

        # Third GET request
        day_url = 'https://middletowncityschools.infinitecampus.org/campus/resources/calendar/instructionalDay?calendarID=204'
        day_headers = {
            'accept': 'application/json, text/plain, */*',
        }
        async with session.get(day_url, headers=day_headers, ssl=False) as day_response:
            day_data = await day_response.json()

    return day_data, term_data

async def main():
    data = await postData()
    print(data)

asyncio.run(main())

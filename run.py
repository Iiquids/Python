from datetime import datetime
import asyncio
import aiohttp

def getLocalDate():
    # Get current local date
    local_date = datetime.now().strftime('%Y-%m-%d')
    return local_date

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

        # Third GET request
        day_url = 'https://middletowncityschools.infinitecampus.org/campus/resources/calendar/instructionalDay?calendarID=204'
        day_headers = {
            'accept': 'application/json, text/plain, */*',
        }
        async with session.get(day_url, headers=day_headers, ssl=False) as day_response:
            day_data = await day_response.json()
    letterDay = "nil"
    for i in range(0, len(day_data)):
        if day_data[i]["date"] == getLocalDate():
            if day_data[i]["periodScheduleID"] == "562":
                letterDay = "X"
            elif day_data[i]["periodScheduleID"] == "563":
                letterDay = "Y"
            else:
                letterDay = "nil"
    
    return letterDay

async def main():
    data = await postData()
    print(data)

asyncio.run(main())

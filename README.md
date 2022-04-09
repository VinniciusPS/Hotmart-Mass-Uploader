# Hotmart Mass Uploader

![](img/video.jpg)

---

# 1.0 The context

A company that sells college entrance preparatory courses was about to launch a new package of courses on the market. The deadline for release was 5 months.
The videos links (Vimeo) and titles, which were allocated in a spreadsheet, were manually incorporated one by one to the Hotmart platform through the embedding field provided by the platform.

<br>

# 2.0 The problem

In the weekly meeting, it was verified by the managers that, as the product launch had a tight deadline and the budget was short, the company ran the risk of not being able to deliver 100% of the videos in the estimated time and would still exceed the budget ceiling due to the labor cost.

<br>

# 3.0 The solution

The delivered solution was a bulk upload with Python. 
The upload that was done manually and would take an average of 4
months to complete, it could be completed in a few weeks. This reduced the customer's labor spend by approximately 96%.

The program was substantially built using:

Pandas: Used to extract data from existing data sheet that contained Vimeo links, title and description of WebDriver videos for Browser automation. This would take advantage of the fact that the company already had a database, improving the query and writing process.

WebDriver: Used to automate user interaction with the browser.

1. The program would iteratively query the database to load the links and names of the videos.
2. Open the Browser (Chrome) and automate all interactions of login, password and clicks on folders made normally by the user.
3. Locate the target field where the links would be embedded
4. Embed the links iteratively until the end of the content referring to a specific topic.

<br>

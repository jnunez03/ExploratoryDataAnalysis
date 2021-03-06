# Exploratory Data Analysis (EDA for short)!

## Objectives:
1) Characteristics associated with people making "Phone Orders" (mobile).
2) Characteristics associated with people making "Cart Orders" (desktop).
3) Characteristics associated with non-conversions *AND* are they similiar to those who converted?

# Let's get started! This time with some useful graphs!
### Quick Notes
- Desktop: 14,238 people using desktop computers.
- Mobile:  4794 people
- Tablet:  1157 people
- Not all Session ID's were unique! This may cause double-counting. We have to drop duplicate values!! There were only 67 duplicate session ID's. When I looked further into the duplicated rows, the rest of the data was the same, so data quality remains the same, despite dropping these values. 
## Right away: Site Visits and Distinct Page Views
![ftegraphvisitsdistinctpageviews](https://user-images.githubusercontent.com/23710841/41834884-b3167838-7823-11e8-83ae-a9abf6c2a038.png)
## First up: People who ended up making a Phone Order!
- They could have came from either mobile, desktop, or tablet, but the important thing is they *ended up* purchasing through mobile!
![ftegraphphone](https://user-images.githubusercontent.com/23710841/41834883-b30a4c3e-7823-11e8-82c9-ac9f91127a43.png)
![correlation](https://user-images.githubusercontent.com/23710841/41834882-b2dc85e2-7823-11e8-9ff5-92a2b0d3c37c.png)
- We see that there is a distinct correlation between phone orders and distinct page views.
### Breakdown
![where1](https://user-images.githubusercontent.com/23710841/41747573-6a7ea9c8-757c-11e8-9942-17bdbbc5c612.png)
- This graph shows us a breakdown of people who made a Phone Order. What hardware they were using as well as how they got to the site.
- This also shows us that people who were already on their phones, stayed on their phones to make an order. People did divert to desktop, but mobile dominates.
- Paid search seems to do better on mobile & Direct Entry also dominates on mobile.
- Totals: 172 Mobile, 131 Desktop (significant when compared with difference when people make cart order. We will see later.)
- Tablets? Yeah... at least 22 people made a phone order (we will take anything!).
![distinct1](https://user-images.githubusercontent.com/23710841/41747571-6a6588ee-757c-11e8-838a-f8908225cc2b.png)
- Totals on how many different pages were visited.. lets break this down even more. 2 page visits leads the bounty!
![distinct2](https://user-images.githubusercontent.com/23710841/41747572-6a70aae4-757c-11e8-90f0-a2cec06c5157.png)
- Mobile has the highest 1-2 page visits, with desktop increasing in that order.
- Desktop leads when 3 or more pages are visited. This leads to conversion on Phone Order (Don't Forget!).
- In other words, people on desktop wanted to visit more sites before making a phone order, whereas people who made a phone order already being on their phone saw less web pages! It took less pages for people on the phone to make an order!
### When did they visit the site (AM or PM) and on what days?
![dayornight1](https://user-images.githubusercontent.com/23710841/41830893-a6896e34-7811-11e8-9d57-d9c2b323241e.png)
![dayornight2 2](https://user-images.githubusercontent.com/23710841/41831068-ed6d4d74-7812-11e8-8fca-03b54cc942f3.png)
#### Other:
- ISPs. Most had: Time Warner, Verizon, Comcast, and At&t (in that order). 
- Came from Cali, Texas, Florida.
- Most connection speeds were: Cable, mobile.
##### Totals
- Direct Entry:   147
- Natural Search: 117
- Paid Search:    60
- Other:          1
## TOTAL: 325 Phone Orders. 172 came through mobile, 131 started at desktop, 22 started from tablet.
## 1.61% total conversion given time frame of roughly 2-3 weeks in this data set (based on subset of data)
##### Conversion calculated by dividing 325 (our subset) by the whole data set.
__________________________________________________________________________________________________________________________
## Let's quickly look at people who made a Cart Order
![where1](https://user-images.githubusercontent.com/23710841/41747752-1f3a7aae-757d-11e8-8d9e-f394c0b10070.png)
- Here is where we less less of a disparity between mobile/desktop despite this being a Cart Order Conversion!
- Many people were on the phone and decided to diverge to desktop to make a purchase.
- Paid Search did fairly better this time around. 
![distinct1](https://user-images.githubusercontent.com/23710841/41747750-1f0db37a-757d-11e8-8276-2eedefacd1b9.png)
- 2 page views leads again, but 3 distinct site views is higher on cart orders than phone orders.
![distinct2](https://user-images.githubusercontent.com/23710841/41747751-1f2dd628-757d-11e8-9794-6eb8cada2c1e.png)
- Despite being mobile/desktop, when people make a desktop cart order, they generally see more than 1 page!
### When did they visit the site (AM or PM) and on what days?
![cartdaynight1](https://user-images.githubusercontent.com/23710841/41831151-67a8fc28-7813-11e8-97a3-62b36d1c2670.png)
![cartdaynight2](https://user-images.githubusercontent.com/23710841/41831152-67b3c5ea-7813-11e8-8856-5ed8f9ed9234.png)
- On March 2nd: Phone orders in AM exceeded PM. However, that is not that case for Cart Orders. PM dominated everyday.
#### Other:
- ISPs. Most had: Time Warner, Tmobile, and At&t.
- Came from Cali, Texas, Florida.
- Most connection speeds were: Cable, mobile.
##### Totals
- Direct Entry      101
- Natural Search    92
- Paid Search       76
- Other             2
## TOTAL: 271 Cart Orders. 124 Desktop, 123 started at mobile, 24 were on tablets.
## 1.34% Conversion rate give time frame (based on subset of data).
##### That conversion is calculated by dividing 271 (our subset) by the whole data set.
___________________________________________________________________________________________________________________________
# Let's look at people who did not convert 
### Quick Notes on non conversion
- Desktop: 13983 people who did not convert
- Mobile:  4499  people    ''
- Tablet:  1111  people    ''
#### If we subtract from our original values we see in our Grand Total Conversion (based on overall data):
- Desktop: Total of 1.8% desktop conversions.
- Mobile: Total of 6.2% phone conversions.
- Tablet: Total of 4% tablet conversions.
#### Breakdown
![where1](https://user-images.githubusercontent.com/23710841/41747990-f0b8d242-757d-11e8-9bcc-37510911213e.png)
- Alot of non-conversion obviously came from people on desktop (there were more in the dataset), but we see that the trend between Direct entry, paid search, natural search all decrease the same way for mobile users. This could be significant.
- Less people convert when there is direct entry.
- As seen earlier, direct entry did well for phone and cart orders as well as phone orders who were using their phones.
![distinct1](https://user-images.githubusercontent.com/23710841/41747988-f0a0303e-757d-11e8-9614-8f74da28c079.png)
![distinct2](https://user-images.githubusercontent.com/23710841/41747989-f0ad4d1e-757d-11e8-8689-49bcbb855dde.png)
- Same thing occurs despite hardware. Many people stopped at the first page! 
- No more than 1 page is visited, generally. 
#### Most Significant States Not Converting:
- CA:    3704
- FL:    2320
- TX:    2268
- CT:    1037
- IN:    908
- IL:    879
- NY:    848
- PA:    843
- WA:    819
- OH:    737
- AZ:    706
#### Most significant ISPs (non-conversion):
- Frontier Communications of America Inc:                   8064
- Time Warner Cable Internet llc:                           1392
- Comcast Cable Communications Inc:                         1278
- Verizon Wireless:                                         831
- Mci Communications Services Inc. dba verizon business:    730
- Att Internet Services:                                    650
- Qwest Communications Company llc:                         647
##### Totals
- Direct Entry:    11972
- Paid Search:     5112
- Natural Search:  2383
- Other:           126
# We're seeing a lot of Time Warner conversion. (Based on people who made Phone/Cart Orders)
- 1,521 people in this data set displayed Timer Warner as their ISP.
- 129 of them converted! 129 of them ended up making a purchase.
- Almost 10% of them converted in a small time frame, which is good!
##### Let's break it down even further and compare conversion and non-conversion of Time Warner customers
## Time Warner Customers who made a phone order
![where1](https://user-images.githubusercontent.com/23710841/41748259-1445d90c-757f-11e8-802c-badba19a8946.png)
- Most of them started on Desktop! Those who converted from desktop made more natural searches.
- More of those who started on mobile came from direct entry.
![distinct1](https://user-images.githubusercontent.com/23710841/41748257-142cff7c-757f-11e8-8c4f-aa2bc2d4c0bc.png)
- Again, we see the same trend of more distinct web pages being visited before a purchase is made.
![distinct2](https://user-images.githubusercontent.com/23710841/41748258-14386cea-757f-11e8-8193-ce7514991e8d.png)
- We have more people who converted to mobile phone orders who started from desktop. They tend to visit more pages.
- California/Florida/Texas lead the way.
- Most frequent landing page: "phonecompanyx.com"
##### Totals
- Desktop:    37
- Mobile:     24
- Tablet:     6
- Direct Entry:    32
- Natural Search:  19
- Paid Search:     15
- Other:           1
## Time Warner Customers who made a cart order
![where1](https://user-images.githubusercontent.com/23710841/41748378-a2085198-757f-11e8-9c74-1c557b410519.png)
- Paid Search does really well for time warner customers in general.
![distinct1](https://user-images.githubusercontent.com/23710841/41748376-a1ec4bb0-757f-11e8-85b9-0eed0499c454.png)
- Time warner customers are generally more curious. They visit more pages.
![distinct2](https://user-images.githubusercontent.com/23710841/41748377-a1fb5fe2-757f-11e8-9de7-e8fff01d0ce9.png)
- They usually stay on their computer to make an order.
### Other:
- States they come from: California, Texas, Florida.
- Most frequent landing page: "phonecompanyx.com"
##### Totals
- Desktop:    44
- Mobile:     10
- Tablet:     8
- Paid Search:     25
- Direct Entry:    22
- Natural Search:  15
## Time Warner Customers who did not convert
![where1](https://user-images.githubusercontent.com/23710841/41748848-93f42274-7581-11e8-972f-67a400a6eca4.png)
- Surprisingly, many came from paid search. So, they were probably looking to purchase a deal or browsing in this topic.
- Although, direct entry leads the way.
![distinct1](https://user-images.githubusercontent.com/23710841/41748846-93d52568-7581-11e8-9a6c-1b3845e89c7c.png)
- Not surprising either, they only visit 1 page.
![distinct2](https://user-images.githubusercontent.com/23710841/41748847-93e7efae-7581-11e8-9161-3d3862d26411.png)
- This shows that a good amount click a second page, however, they do not convert. 
#### Other:
- States that dominate: California, Florida, Texas, (Ohio & New York: Very low turn-outs for these states).
- Most frequent landing page: "phonecompanyx.com"
### 9 people each landed on these pages: 
###### (Don't know how to anonymize the actual tabs, but left for clarity sake)
- "phonecompanyx.com/fios"
- "phonecompanyx.com/shop/bundles/fios-ctf/fios-ctf"
- ".../fiosbyphonecompanyx?utm_source=mailer..."
##### Totals
- Desktop:    949
- Mobile:     346
- Tablet:     97
- Direct Entry:     680
- Paid Search:      522
- Natural Search:   184
- Other:            6
## Thoughts
- Scraping the data, many people who did not convert were using Chrome, were from California/Florida/Texas, and visited only 1 page of the website.
- A large amount has their Internet Service Provider as "Frontier Communications of America Inc" and "Time Warner". This could be why many people did not convert. Given that this could have been geared towards ISP provider, since many already had a different provider, they opted to not purchase which is why they stopped at the first page. 
- As shown earlier, a lot of people who had Time Warner atually converted, and a large portion who didn't. Maybe there is something about Time Warner that made people convert. Since there were many of them, we can market towards Time Warner and work on those kinds of people to increase conversion. Take advantage of the #'s.
- 11,972 came from direct entry. 5,122 came from paid search.
## Next?
- Definitely working to improve mobile, because we get a better turnout.
- Also, figure out why desktop is not performing better. Is it the ads? The experience? Maybe someone just does not want to purchase the product? Are the incentives good enough for them to make a purchase? Is the marketing being tailored for different people.
- A lot of people who were from Time Warner made a purchase. Dig deeper into figuring out why seems advantageous for conversion.
## Caveat
- Sometimes data doesn't answer all of our questions. Sometimes low turnout is just the way things are. Analyzing data does not automatically mean we will increase turnout, it means we can now leverage the information to improve with the goal to increase conversion. 
- Sometimes it's the small things that make a difference. How much can we personalize? 

##### Also Tableau could have been used to plot States/Cities visuals. 
# Next up? Predictive Analysis
## Can we predict if someone will convert? What variables are strongest when we think about conversion?
I focused on predicting Phone Orders since we did see better conversion.

### Random Forest 

- What is [Random Forest](https://towardsdatascience.com/the-random-forest-algorithm-d457d499ffcd)
- Another [Good Explanation](http://dataaspirant.com/2017/05/22/random-forest-algorithm-machine-learing/)

We've heard of linear regression to make predictions. Well, our data does not have numbers. Other than distinct page views, everything else is what we call categorical. "Device Type", "Broswer Type", "Traffic Source", aren't numbers. We can't use linear regression.
### Random Forest can make predictions and works well for categorical variables.
- After running my model, I was able to predict Phone Orders with a 98% accuracy level.
- We can also check which variables are the most "predictive" when asking who will make a Phone Order.
- In other words, what variable is most important when asking who will make a phone order.
![variableimportance](https://user-images.githubusercontent.com/23710841/41757833-a1738c56-75b2-11e8-906b-f6a9d8469633.png)
#### Caveat: I used a subset of the data. So, I used top 10 ISPs in our data. I only included top 11 states, and the top 6 browser types.
#### I did not use:
- Landing Page
- Order ID
- Zip Code
- OS Name
- Metro Name
- Manufacturer
- Country 
- Connection Speed
- Session Start Time
- Session Id
- City

## Notes
- The graph shows that Distinct Page Views was the most important when figuring out if someone would make a Phone Order.
- The 2nd, 3rd, & 4th most important variables were traffic source: direct entry, traffic source: natural search, and if someone resided in california. However, these were all tied in importance. Along with, residing in florida, texas, and if someone entered through paid search.

# End Notes
- Every model is different. We can get different results. However, random forest creates this classifier randomly. It generalizes well to our data and was 98% accurate in predicting a phone order given the variables that I decided to include based on context.  

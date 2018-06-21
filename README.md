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
- Not all Session ID's were unique! This may cause double-counting. We have to drop duplicate values!! There were only 67 duplicate session ID's. When I looked further into the duplicated rows, the rest of the data was the same, so data quality remains the same, desipite dropping these values. 
## First up: People who ended up making a Phone Order!
- They could have came from either mobile, desktop, or tablet, but the important thing is they *ended up* purchasing through mobile!
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
## Let's quickly look at people who made a Cart Order! (Results: Not So Surprising)
![where1](https://user-images.githubusercontent.com/23710841/41640781-ef8a32f6-7430-11e8-8ece-6854d2d9b042.png)
- Here is where we less less of a disparity between mobile/desktop despite this being a Cart Order Conversion!
- Many people were on the phone and decided to diverge to desktop to make a purchase.
- Paid Search did fairly better this time around. 
![distinct2](https://user-images.githubusercontent.com/23710841/41640778-ef71471e-7430-11e8-9627-7cee6581f6b3.png)
- 2 page views leads again, but 3 distinct site views increased from when someone made a phone order.
![distinct3](https://user-images.githubusercontent.com/23710841/41640780-ef7d631e-7430-11e8-91b5-38e7278dad57.png)
- Despite being mobile/desktop, when people make a desktop cart order, they generally see more than 1 page!
#### Other:
- ISPs. Most had: Time Warner, Tmobile, and At&t.
- Came from Cali, Texas, Florida.
- Most connection speeds were: Cable, mobile.
- Direct Entry      101
- Natural Search    92
- Paid Search       76
- Other             2
## TOTAL: 271 Cart Orders. 124 Desktop, 123 started at mobile, 24 were on tablets.
## 1.34% Conversion rate give time frame (based on subset of data).
##### That conversion is calculated by dividing 271 (our subset) by the whole data set.
___________________________________________________________________________________________________________________________
# Let's look at people who did not convert .... 
### Quick Notes on non conversion
- Desktop: 13983 people who did not convert
- Mobile:  4499  people  ''
- Tablet:  1111  people  ''
#### If we subtract from our original values we see in our Grand Total Conversion (based on overall data):
- Desktop: Total of 1.8% desktop conversions.
- Mobile: Total of 6.2% phone conversions.
- Tablet: Total of 4% tablet conversions.
#### Breakdown
![where1](https://user-images.githubusercontent.com/23710841/41641808-7c24b026-7434-11e8-9172-1571c74a7b00.png)
- Alot of non-conversion obviously came from people on desktop (there were more in the dataset), but we see that the trend between Direct entry, paid search, natural search all decrease the same way for mobile users. This could be significant.
- Less people convert when there is direct entry.
- As seen earlier, direct entry did well for phone and cart orders as well as phone orders who were using their phones.
![distinct1](https://user-images.githubusercontent.com/23710841/41641806-7bfe1f38-7434-11e8-8d21-bf77747a5c15.png)
![distinct2](https://user-images.githubusercontent.com/23710841/41641807-7c16051c-7434-11e8-9988-bdd3ffd3b4a8.png)
- Same thing occurs despite hardware. Many people stopped at the first page! 
- No more than 1 page is visited, generally. 

## We're seeing a lot of Time Warner conversion. Let's figure out more.
- 1536 people in this data set displayed Timer Warner as their ISP.
- 144 of them converted! 144 of them ended up making a purchase!
- Almost 10% of them converted in a small time frame, which is good!
##### Let's break it down even further and compare conversion and non-conversion of Time Warner customers
## Time Warner Customers who made a phone order
![where1](https://user-images.githubusercontent.com/23710841/41744911-3fca6162-7573-11e8-987e-df7606d119e9.png)
- Most of them started on Desktop! Those who converted from desktop made more natural searches.
- More of those who started on mobile came from direct entry.
![distinct1](https://user-images.githubusercontent.com/23710841/41744908-3f9e1396-7573-11e8-8768-d793f4459e38.png)
- Again, we see the same trend of more distinct web pages being visited before a purchase is made.
![distinct2](https://user-images.githubusercontent.com/23710841/41744910-3fb8b232-7573-11e8-8415-38be6ab93d17.png)
- We have more people who converted to mobile phone orders who started from desktop. They tend to visit more pages.
### Other:
- Desktop:    41
- Mobile:     28
- Tablet:     7
- California/Florida/Texas lead the way.
- Most frequent landing page: "phonecompanyx.com"
- Direct Entry      36
- Natural Search    22
- Paid Search       17
- Other              1

## Time Warner Customers who made a cart order
![where1](https://user-images.githubusercontent.com/23710841/41745453-fcbbe696-7574-11e8-8498-a43f04a2a99f.png)
- Paid Search does really well for time warner customers who are on their desktop. It does better for people who started out on their phones.
![distinct1](https://user-images.githubusercontent.com/23710841/41745451-fca2f898-7574-11e8-94ca-58538b8bf972.png)
![distinct2](https://user-images.githubusercontent.com/23710841/41745452-fcaf4ea4-7574-11e8-83f0-8ce045a62853.png)

### Why?
- Well that's not easy to answer.
- Scraping the data, many people who did not convert were using Chrome, were from California/Florida/Texas, and visited only 1 page of the website.
- A large amount has their Internet Service Provider as "Frontier Communications of America Inc" and "Time Warner". This could be why many people did not convert. Given that this could have been geared towards ISP provider, since many already had a different provider, they opted to not purchase which is why they stopped at the first page. 
- As shown earlier, a lot of people who had Time Warner atually converted, and a large portion who didn't. Maybe there is something about Time Warner that made people convert. Since there were many of them, we can market towards Time Warner and work on those kinds of people to increase conversion. Take advantage of the #'s.
- 11,972 came from direct entry. 


## Next?
- Definitely working to improve mobile, because we get a better turnout.
- Also, figure out why desktop is not performing better. Is it the ads? The experience? Maybe someone just does not want to purchase the product? Are the incentives good enough for them to make a purchase? Is the marketing being tailored for different people.
- People who were from Time Warner definitely made a purchase. Dig deeper into figuring out why seems advantageous for conversion.

# Caveat
- Sometimes data doesn't answer all of our questions. Sometimes low turnout is just the way things are. Analyzing data does not automatically mean we will increase turnout, it means we can now leverage the information to improve what needs to be improved with the goal to increase conversion. 
- Sometimes it's the small things that make a difference. How much can we personalize? 

##### Also Tableau could have been used to plot States/Cities visuals. 

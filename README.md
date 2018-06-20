# Exploratory Data Analysis (EDA for short)!

## Objectives:
1) Characteristics associated with people making "Phone Orders" (mobile).
2) Characteristics associated with people making "Cart Orders" (desktop).
3) Characteristics associated with non-conversions *AND* are they similiar to those who converted?

# Let's get started! This time with some useful graphs!
### Quick Notes
- Desktop: 14271 rows in our data. 14,271 people using desktop computers.
- Mobile:  4827 people
- Tablet:  1158 people
## First up: People who ended up making a Phone Order!
- They could have came from either mobile, desktop, or tablet, but the important thing is they *ended up* purchasing through mobile!
### Breakdown
![phoneconversion_where1](https://user-images.githubusercontent.com/23710841/41639331-520000a6-742b-11e8-95e4-f7fbe0d3c843.png)
- This graph shows us a breakdown of people who made a Phone Order. What hardware they were using as well as how they got to the site.
- This also shows us that people who were already on their phones, stayed on their phones to make an order. People did divert to desktop, but mobile dominates.
- Paid search seems to do better on mobile!
- Totals: 191 Mobile, 144 Desktop (significant when compared with difference when people make cart order. We will see later.)
- Tablets? Yeah... at least 23 people made a phone order (we will take anything!).
![phoneconvdistinct2](https://user-images.githubusercontent.com/23710841/41639330-51f0023c-742b-11e8-9eaf-08b720b7696f.png)
- Totals on how many different pages were visited.. lets break this down even more. 2 page visits leads the bounty! (No, it's not because Derek Jeter wore that number, but everyone has their conspiracies). 
![distinctfromwhere3](https://user-images.githubusercontent.com/23710841/41639329-51dd7a40-742b-11e8-80a2-49562b1554e5.png)
- Mobile has the highest 1-2 page visits, with desktop increasing in that order.
- Desktop leads when 3 or more pages are visited. This leads to conversion on Phone Order (Don't Forget!).
- In other words, people on desktop wanted to visit more sites before making a phone order, whereas people who made a phone order already being on their phone saw less web pages! It took less pages for people on the phone to make an order!
## TOTAL: 358 Phone Orders. 191 came through mobile, 144 started at desktop!
## 1.77% total conversion given time frame of roughly 2-3 weeks in this data set (based on subset of data)
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
## TOTAL: 305 Cart Orders. 144 Desktop, 137 started at mobile!
## 1.51% Conversion rate give time frame.. (based on subset of data)
___________________________________________________________________________________________________________________________
# Let's look at people who did not convert .... 
### Quick Notes on non conversion
- Desktop: 13983 people who did not convert
- Mobile:  4499  people  ''
- Tablet:  1111  people  ''
#### If we subtract from our original values we see in our Grand Total Conversion (based on overall data):
- Desktop: Total of 2% total conversion
- Mobile: Total of 6.8% total conversion
- Tablet: Total of 4.1% total convertsion
#### Breakdown
![where1](https://user-images.githubusercontent.com/23710841/41641808-7c24b026-7434-11e8-9172-1571c74a7b00.png)
- Alot of non-conversion obviously came from people on desktop (there were more in the dataset), but we see that the trend between Direct entry, paid search, natural search all decrease the same way for mobile users. This could be significant.
- Less people convert when there is direct entry.
- In contrast, direct entry did well for phone and cart orders as well as phone orders who were using their phones.
![distinct1](https://user-images.githubusercontent.com/23710841/41641806-7bfe1f38-7434-11e8-8d21-bf77747a5c15.png)
- No more than 1 page is visited, generally. 
![distinct2](https://user-images.githubusercontent.com/23710841/41641807-7c16051c-7434-11e8-9988-bdd3ffd3b4a8.png)
- Same thing occurs despite hardware. Many people stopped at the first page! 

### Why?
- Well that's not easy to answer.
- Scraping the data, many people who did not convert were using Chrome, were from California-Florida-Texas, visited only 1 page of the website.
- A large amount has their Internet Service Provider as "frontier communications of america inc" and "time warner". 
- 11,972 came from direct entry. 



csv_data = """foodname,country,taste,type,price,avoid,images
Pad Thai,thai,salty & spicy & umami,one-dish & seafood ,30-100,seafood,https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Phat_Thai_kung_Chang_Khien_street_stall.jpg/1200px-Phat_Thai_kung_Chang_Khien_street_stall.jpg
krapao pla,thai,salty umami ,one-dish,50-100,seafood,https://media-cdn.tripadvisor.com/media/photo-s/06/b1/32/32/ad-lib-restaurant.jpg
krapao kung,thai,salty umami,one-dish,50-100,seafood,https://www.thekitchenabroad.com/wp-content/uploads/2021/03/THAI-BASIL-SHRIMP-STIR-FRY-08-scaled.jpg
crab fried rice,thai,salty umami,one-dish,50-100,seafood,https://hot-thai-kitchen.com/wp-content/uploads/2020/12/Crab-fried-rice-sq.jpg
squid with curry,thai,salty umami,one-dish,50-100,seafood,https://tasteasianfood.com/wp-content/uploads/2022/09/squid-curry-recipe-5.jpeg
Tom Yum Spicy Soup,Thai,spicy salty,soup,50-100,seafood,https://hot-thai-kitchen.com/wp-content/uploads/2013/03/tom-yum-goong-blog.jpg
Mango Sticky Rice,Thai,sweet umami,dessert,50-100,dessert,https://elavegan.com/wp-content/uploads/2020/07/drizzling-coconut-sauce-over-mango-sticky-rice.jpg
Som Tum,Thai,spicy sour,salad,50-100,vegetable,https://www.seriouseats.com/thmb/yKNZ9ICJC5ZNhzcYHdHENxogpFw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20210928-Som-Tam-Thai-green-papaya-salad-vicky-wasik-24-f0d666fc609f49a0b9f34897bd2c6303.jpg
Khao Pad,Thai,umami salty,one-dish,50-100,,https://rachelcooksthai.com/wp-content/uploads/2011/01/4-1.jpg
Pad Kra Pao Moo,Thai,salty spicy umami,one-dish,40-80,pork,https://cdn.alldayieat.com/wp-content/uploads/2017/10/Pad-Kra-Pao-Moo-Stir-Fried-Pork-with-Thai-Holy-Basil-4.jpg
Mama Phad,Thai,salty spicy umami,one-dish,40-80,,https://cmtk.co-enterprise.com.sg/wp-content/uploads/Phad-Mama-28Thai-Fried-Instant-Noodle29.jpg
Coconut Milk Ice Cream,Thai,sweet umami,dessert,50-100,dessert,https://theflavoursofkitchen.com/wp-content/uploads/2019/06/Coconut-Ice-Cream-4.jpg
Pad See Ew Moo,Thai,Salty umami,Fry,30-50,pork,https://thewoksoflife.com/wp-content/uploads/2017/02/pad-see-ew-11-2.jpg
Green Curry,Thai,Spicy,Soup,50-100,Chicken,https://www.thecookingcollective.com.au/wp-content/uploads/2023/05/Thai-green-chicken-curry-3.jpg
Massaman Curry,Thai,Spicy and Umami,Soup,100-150,,https://www.wellplated.com/wp-content/uploads/2022/08/best-massaman-curry-recipe.jpg
Tom Kha Gai,Thai,Umami and Spicy,Soup,30-50,Chicken,https://hot-thai-kitchen.com/wp-content/uploads/2014/06/Tom-kha-gai-new-sq.jpg
Khao Soi,Thai,Creamy and Spicy,One-dish,50-100,Chicken,https://hot-thai-kitchen.com/wp-content/uploads/2014/01/kao-soi-blog.jpg
Pla Rad Prik,Thai,Spicy and Salty,Seafood,100-150,seafood,https://importfood.com/images/com_yoorecipe/22/plaradprik_8l.jpg
Kai Med Ma Muang,Thai,salty and spicy,Meat,30-50,Chicken,https://asianinspirations.com.au/wp-content/uploads/2019/01/R00890_Stir_Fried_Chicken_with_Cashew_Nuts.jpg
Yam Talay,Thai,Spicy and Sour,Seafood,50-100,seafood,https://importfood.com/images/cropped-yumtalay3l.jpg
Khao Niew  Moo Ping,Thai,Sweet and Sticky,snack,30-50,pork,https://www.marionskitchen.com/wp-content/uploads/2023/05/Thai-Moo-Ping-14.jpg
Pla Pao,Thai,Salty and Grilled,Seafood,100-150,seafood,https://asianinspirations.com.au/wp-content/uploads/2018/07/R00695_Pla-Pao.jpg
Larb Gai,Thai,Spicy and Tangy,One-dish,30-50,Chicken,https://img.taste.com.au/MDi8O9zz/taste/2016/11/larb-gai-with-mint-and-basil-83035-1.jpeg
Tod Mun Pla,Thai,Spicy and Crispy,Snack,100-150,seafood,https://thaicaliente.com/wp-content/uploads/2021/10/Fish-Cake-Feature.jpg
Green Mango Salad,Thai,Sour and Spicy,Snack,100-150,vegetable,https://littlespicejar.com/wp-content/uploads/2023/04/Thai-Mango-Salad-8-735x1103.jpg
Khao Man Gai,Thai,Savory and Ginger,One-dish,30-50,chicken,https://www.thespruceeats.com/thmb/bGeARnS56XAFr1DgyFxe_gpSusA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/thai-khao-man-gai-4767706-hero-01-08fec21125fe4d3bbd00d53ab95de058.jpg
Yum Woon Sen,Thai,Spicy and Tangy,Seafood,30-50,,https://thaicaliente.com/wp-content/uploads/2021/08/Yum-Woon-Sen-Feature.jpg
Kao Pad Tom Yum,Thai,Spicy and Savory,One-dish,30-50,seafood,https://asianinspirations.com.au/wp-content/uploads/2019/01/R00879_Tom_Yum_Fried_Rice.jpg
Larb Moo,Thai,Spicy and Tangy,Meat,30-50,pork,https://www.eatingthaifood.com/wp-content/uploads/2014/02/thai-larb-recipe.jpg
Kai Jeow,Thai,Savory and Crispy,One-dish,30-50,,https://rachelcooksthai.com/wp-content/uploads/2022/08/Kai-Jeow-2.jpg
Lodchong,Thai,Sweet,dessert,10-30,dessert,https://miro.medium.com/v2/resize:fit:1200/1*N1l-JwbacwuYzO87LmFFpQ.jpeg
Bualoy,Thai,Sweet ,Dessert,10-30,dessert,https://www.messyvegancook.com/wp-content/uploads/2010/11/2018-08-817-Edit_HDR.jpeg
Pla Kapong Neung Manao,Thai,Sour and Spicy,Seafood,100-150,seafood,https://www.eatingthaifood.com/wp-content/uploads/2016/01/thai-steamed-fish-recipe-18.jpg
Pad Kana Moo Krob,Thai,Salty and Crispy,Meat,50-100,pork,https://hungryinthailand.com/wp-content/uploads/2023/05/pad-kana-moo-krob.webp
Khao Pad Sapparod,Thai,sour umami,One-dish,30-50,seafood,https://whattocooktoday.com/wp-content/uploads/2013/09/pineapple-fried-rice-26.jpg
Sashimi,Japanese,Umami,Seafood,100-150,seafood,https://food.fnr.sndimg.com/content/dam/images/food/fullset/2023/3/22/japanese-tuna-and-salmon-sashimi-in-bowl-on-gray-background.jpg.rend.hgtvcom.1280.1280.suffix/1679511773776.jpeg
Tempura,Japanese,Salty and Crispy,Fry,50-100,seafood,https://thesuburbansoapbox.com/wp-content/uploads/2022/08/STempura-18.jpg
Ramen,Japanese,Umami salty,Soup noodle,30-100,pork,"https://res.cloudinary.com/jnto/image/upload/w_750,h_450,c_fill,f_auto,fl_lossy,q_60/v1/media/filer_public/e0/3c/e03c7f75-06a7-45ed-920b-dc5d7ad6eb60/mar22_ramen_12_e4tdxz"
Chirashi Sushi,Japanese,Umami,Seafood,100-150,seafood,https://www.justonecookbook.com/wp-content/uploads/2020/02/Chirashi-Sushi-7722-I-1.jpg
Okonomiyaki,Japanese,Savory and Salty,Fry,50-100,seafood,https://www.spoonforkbacon.com/wp-content/uploads/2021/09/okonomiyaki-recipe-card.jpg
Miso Soup,Japanese,Umami salty,Soup,30-50,vegetable,https://www.justonecookbook.com/wp-content/uploads/2022/06/Miso-Soup-8297-I.jpg
Udon,Japanese,Umami salty,Soup noodle,50-100,pork,https://www.justonecookbook.com/wp-content/uploads/2021/11/Beef-Udon-4306-I-500x500.jpg
curry udon,Japanese,Umami salty,Soup noodle,50-100,pork,https://images.squarespace-cdn.com/content/v1/568e8fe6b204d5cbecd5c77e/7b0234cc-03ea-4bc5-a3cf-405c2edab053/Japanese+Curry+Udon-1550.jpg
Gyoza,Japanese,Umami and Crispy,Fry,30-50,Pork,"https://assets.epicurious.com/photos/628ba0d3fa016bab2139efa2/1:1/w_4546,h_4546,c_limit/Gyoza_RECIPE_051922_34332.jpg"
Daifuku,Japanese,Sweet,dessert,50-100,dessert,https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Daifuku_1.jpg/1200px-Daifuku_1.jpg
Chawanmushi,Japanese,Savory and Silky,Snack,30-50,vegetable,https://www.justonecookbook.com/wp-content/uploads/2022/09/Chawanmushi-9784-I-500x500.jpg
Nikujaga,Japanese,Sweet and Savory,One-dish,30-50,vegetable,https://www.justonecookbook.com/wp-content/uploads/2021/05/Nikujaga-6915-I.jpg
Unagi Don,Japanese,Sweet and Grilled,One-dish,100-150,seafood,https://www.justonecookbook.com/wp-content/uploads/2021/07/Unadon-Eel-Rice-9543-I-1-500x500.jpg
Sushi Rolls,Japanese,Various Flavors,Snack,50-100,seafood,https://www.justonecookbook.com/wp-content/uploads/2020/01/Sushi-Rolls-Maki-Sushi-%E2%80%93-Hosomaki-1106-II.jpg
Hokkaido Soup Curry,Japanese,Spicy and Comforting,Soup,50-100,pork,https://asianinspirations.com.au/wp-content/uploads/2018/11/R001337_Hokkaido-Soup-Curry.jpg
Takoyaki,Japanese,Savory and Octopus,Snack,30-50,seafood,https://www.wandercooks.com/wp-content/uploads/2019/09/takoyaki-recipe-ft.jpg
Yudofu,Japanese,Simple and Comforting,Soup,30-50,vegetable,https://assets.bonappetit.com/photos/57b018d253e63daf11a4e904/master/pass/yudofu.jpg
Matcha Ice Cream,Japanese,Bitter and Sweet,Dessert,30-50,dessert,https://sudachirecipes.com/wp-content/uploads/2022/08/matcha-ice-cream-thumbnail.jpg
Peking Noodles, Chinese,Savory and Spicy,Noodle,30-50,pork,https://myhungrytraveler.com/wp-content/uploads/2022/05/peking-noodles.jpg
Moo Shu Pork, Chinese,Savory and Sweet,One-dish,30-50,pork,https://www.jocooks.com/wp-content/uploads/2021/02/moo-shu-pork-1-13.jpg
Shrimp Dumplings, Chinese,Savory and Juicy,Snack,30-50,seafood,https://www.thespruceeats.com/thmb/vIG_HVecrucAWQXHQJr5xppwG2E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/har-gow-shrimp-dumplings-recipe-694503-Hero_01-db5847b769a64c0ebdf963c875e32297.jpg
Pineapple Bun, Chinese,Sweet and Crispy,Snack,50-100,,"https://assets.epicurious.com/photos/6230dbdf1f7a61a76db5180b/4:3/w_3963,h_2972,c_limit/2_Pineapple_Buns_2_9780785238997.jpg"
Zongzi, Chinese,Savory and Sticky,Snack,30-50,,https://thewoksoflife.com/wp-content/uploads/2015/05/zongzi-26.jpg
Duck Spring Rolls, Chinese,Crispy and Flavorful,Snack,30-50,pork,https://media-cdn2.greatbritishchefs.com/media/olvf3tkl/img15303.whqc_768x512q80fpt440fpl568.jpg
Lanzhou Beef Noodle Soup, Chinese,Savory and Spicy,Soup,50-100,,https://thewoksoflife.com/wp-content/uploads/2014/10/lanzhou-beef-noodle-soup-4.jpg
Dan Dan Noodles, Chinese,Spicy and Nutty,Noodle,30-50,Peanuts,https://www.halfbakedharvest.com/wp-content/uploads/2019/10/Better-Than-Takeout-Dan-Dan-Noodles-1.jpg
Mooncakes, Chinese,Sweet and Filled,Dessert,30-50,dessert,https://smellylunchbox.com/wp-content/uploads/2022/09/featuredmooncake.jpg
Sichuan Hot Pot, Chinese,Spicy and Savory,Soup,50-100,Seafood,https://www.hwcmagazine.com/wp-content/uploads/2012/02/Spicy-Sichuan-Hot-Pot-1200-x-1200-1295.jpg
Chili Oil Wontons, Chinese,Spicy and Umami,Snack,30-50,Seafood,https://whisperofyum.com/wp-content/uploads/2021/11/wontons-in-chili-oil.jpg
Baozi, Chinese,Savory and Steamed,Snack,50-100,,https://asianinspirations.com.au/wp-content/uploads/2019/06/R02325_Chinese_Steamed_Pork_Buns.jpg
Cantonese Roast Duck, Chinese,Savory and Roasted,Meat,50-100,,https://www.thespruceeats.com/thmb/hFvJHMdZFC_4k5F0v5cwa_IZy1U=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cantonese-roast-duck-694866-hero-04-f960161e87eb45f4a22bb6bafdab352a.jpg
Malatang, Chinese,Spicy and Numbing,Soup,30-50,,https://blog.themalamarket.com/wp-content/uploads/2022/12/malatang-newsletter-11.jpg
Dan Dan Mian, Chinese,Spicy and Nutty,Noodle,30-50,Peanuts,https://i2.wp.com/seonkyounglongest.com/wp-content/uploads/2019/10/Dan-Dan-Noodles-11.jpg?fit=2000%2C1333&ssl=1
Xiao Long Bao, Chinese,Savory and Soupy,Dumpling,30-50,None,https://www.seriouseats.com/thmb/4sQ_PSwAk3NI3DiLwFkA0dESLIo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Soup_Dumplings_hero-AntonisAchilleos-4de81e0b74dd4e7690aea42918eb97ef.JPG
Chrysanthemum Fish, Chinese,Savory and Floral,Seafood,100-150,seafood,https://www.yuncheng.gov.cn/home/uploadfiles/202108/16/2021081616422093056305.png
Suan La Tang, Chinese,Spicy and Sour,Soup,30-50,vegetable,https://redhousespice.com/wp-content/uploads/2021/08/hot-sour-soup-scaled.jpg
Shengjian Bao, Chinese,Savory and Pan-fried,Dumpling,30-50,,https://redhousespice.com/wp-content/uploads/2017/08/Sheng-Jian-Bao-pork-buns.jpg
Zha Jiang Mian, Chinese,Savory and Bean Sauce,Noodle,30-50,,https://www.marionskitchen.com/wp-content/uploads/2022/03/Beijing-style-Noodles-Zha-Jiang-Mian-02.jpg
Peking Duck,Chinese,Sweet and Crispy,Meat,150-250,,https://redhousespice.com/wp-content/uploads/2022/01/sliced-peking-duck-with-pancakes-scaled.jpg
shrimp dim sum,Chinese,Various Flavors,Snack,50-100,seafood,https://media-cdn2.greatbritishchefs.com/media/nd3bemis/img34601.whqc_1426x713q80.jpg
Hot and Sour Soup,Chinese,Spicy and Sour,Soup,30-50,,https://www.gimmesomeoven.com/wp-content/uploads/2017/01/Chinese-Hot-and-Sour-Soup-Recipe-1-2.jpg
General Tso's Chicken,Chinese,Sweet and Spicy,Fry,50-100,Chicken,https://www.onceuponachef.com/images/2023/04/general-tsos-chicken-4.jpg
Mapo Tofu,Chinese,Spicy and Umami,One-dish,30-50,vegetable,https://thewoksoflife.com/wp-content/uploads/2019/06/mapo-tofu-10.jpg
chicken Chow Mein,Chinese,Savory and Crispy,Noodle,50-100,Chicken,https://tiffycooks.com/wp-content/uploads/2023/09/188E6766-B4B4-48FB-80F9-9E7EBA5B6278-scaled.jpg
Sweet and Sour Pork,Chinese,Sweet and Tangy,Meat,50-100,pork,https://www.kitchensanctuary.com/wp-content/uploads/2021/01/Sweet-and-Sour-Pork-square-FS.jpg
Spring Rolls,Chinese,Crispy and Fresh,Snack,30-50,,https://www.sugarsaltmagic.com/wp-content/uploads/2023/01/Chinese-Spring-Rolls-4FEAT-500x500.jpg
Szechuan Shrimp,Chinese,Spicy and Savory,Seafood,50-100,seafood,https://omnivorescookbook.com/wp-content/uploads/2021/04/210204_Sichuan-Shrimp-Stir-Fry_550.jpg
Mongolian Beef,Chinese,Savory and Sweet,Meat,50-100,,https://therecipecritic.com/wp-content/uploads/2023/08/easy-mongolian-beef-1.jpg
Crab Rangoon,Chinese,Creamy and Crispy,Snack,30-50,seafood,https://christieathome.com/wp-content/uploads/2022/04/Cran-Rangoon-6.jpg
Egg Drop Soup,Chinese,Simple and Comforting,Soup,50-100,,https://thewoksoflife.com/wp-content/uploads/2019/05/egg-drop-soup-4.jpg
Ma Po Eggplant,Chinese,Spicy and Umami,Vegetarian,30-50,,https://omnivorescookbook.com/wp-content/uploads/2020/08/200730_Mapo-Eggplant_550.jpg
Scallion Pancakes,Chinese,Savory and Crispy,Snack,30-50,,https://www.seriouseats.com/thmb/pSgKgm8cI4f8OotIu9xihcpkvWE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/31.scallion-pancakes-beauty-shot-5219b2b53f51496199fde8fc7582c92b.jpg
Honey Walnut Shrimp,Chinese,Sweet and Nutty,Seafood,100-150,seafood,"https://hips.hearstapps.com/hmg-prod/images/honey-walnut-shrimp-horizontal-1548093880.png?crop=0.667xw:1xh;center,top&resize=1200:*"
Sesame Chicken,Chinese,Sweet,Fry,50-100,Chicken,https://www.kitchensanctuary.com/wp-content/uploads/2016/06/Crispy-Sesame-Chicken-square-FS.jpg
Vegetable Lo Mein,Chinese,salty,Noodle,30-50,vegetable,https://joyfoodsunshine.com/wp-content/uploads/2022/08/vegetable-lo-mein-recipe-4.jpg
Wonton Soup,Chinese,salty,Soup,50-100,,https://www.recipetineats.com/wp-content/uploads/2016/09/Wontons_1-1.jpg
Kimchi,South Korean,Spicy and Sour,Snack,30-50,vegetable,https://mykoreankitchen.com/wp-content/uploads/2022/01/5.-Homemade-Kimchi.jpg
Bulgogi,South Korean,Sweet and Savory,Meat,50-100,Pork,https://assets.bonappetit.com/photos/57acd741f1c801a1038bc801/1:1/w_2560%2Cc_limit/basic-bulgogi.jpg
Japchae,South Korean,Savory and Sweet,Fry,30-50,vegetable,https://www.recipetineats.com/wp-content/uploads/2023/07/Japchae-Korean-noodles_9.jpg
Samgyeopsal,South Korean,Savory,Meat,30-50,pork,https://www.honestfoodtalks.com/wp-content/uploads/2022/04/Samgyeopsal-with-kimchi-and-beansprouts.jpg
Dolsot Bibimbap,South Korean,Spicy and Savory,One-dish,50-100,vegetable,https://futuredish.com/wp-content/uploads/2017/12/Dolsot-Bibimbap-500x375.jpg
Haemul Pajeon,South Korean,Savory and Crispy,Seafood,30-50,Seafood,https://koreancuisinerecipes.com/wp-content/uploads/2021/08/haemul-pajeon-seafood-pancake.png
Sundubu Jjigae,South Korean,Spicy and Umami,Soup,50-100,,https://drivemehungry.com/wp-content/uploads/2021/10/soondubu-jjigae-korean-tofu-soup.jpg
Kimchi Jjigae,South Korean,Spicy and Sour,Soup,30-50,vegetable,https://www.koreanbapsang.com/wp-content/uploads/2014/03/DSC5897-2.jpg
Tteokbokki,South Korean,Spicy and Sweet,Snack,100-150,,https://twoplaidaprons.com/wp-content/uploads/2022/12/close-top-down-of-tteokbokki-thumbnail.jpg
Yangnyeom Chicken,South Korean,Spicy and Sweet,Fry,30-50,Chicken,https://asianinspirations.com.au/wp-content/uploads/2019/07/R00825_Yangnyeom-Chickin.jpg
Bibimbap, South Korean,Spicy and Savory,One-dish,50-100,vegetable,"https://assets.bonappetit.com/photos/624f3dc73a6e981591892a9d/1:1/w_2800,h_2800,c_limit/0407-bibimbap-at-home-lede.jpg"
Samgyetang, South Korean,Savory and Comforting,Soup,50-100,Chicken,https://www.maangchi.com/wp-content/uploads/2007/10/samgyetang11.jpg
Jajangmyeon, South Korean,Savory and Rich,Noodle,30-50,Seafood,https://twoplaidaprons.com/wp-content/uploads/2022/04/Korean-noodles-topped-with-jajangmyeon-sauce-thumbnail-500x500.jpg
Kimchi Fried Rice, South Korean,Spicy and Savory,One-dish,30-50,,https://takestwoeggs.com/wp-content/uploads/2022/03/Kimchi-Fried-Rice-Kimchi-bokkeumbap-takestwoeggs-final-photography-sq.jpg
Dak Galbi, South Korean,Spicy and Sweet,Meat,50-100,,https://www.marionskitchen.com/wp-content/uploads/2022/09/Korean-Dakgalbi-Spicy-Chicken-Vegetables-01.jpg
Sannakji, South Korean,Crispy and Fresh,Seafood,50-100,seafood,https://img.atlasobscura.com/lBfQpvamgk7fBlzj4rXL4SSM8Bp1r9jZeonvANEybvI/rs:fill:780:520:1/g:ce/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3RoaW5n/X2ltYWdlcy85Y2Qx/MGIxNDdkYTUwYzBi/YzdfU2FubmFramlf/U2h1dHRlcnN0b2Nr/LmpwZw.jpg
Kimchi Pancake, South Korean,Savory and Crispy,Snack,30-50,,https://food-images.files.bbci.co.uk/food/recipes/korean_kimchi_pancake_23271_16x9.jpg
Budae Jjigae, South Korean,Spicy and Umami,Soup,50-100,,https://www.simplyrecipes.com/thmb/VYi5144besj_hTlsgDfVvmzdrFs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Budae-Jjigae-LEAD-02-a22325eea5b54891826b2d78c52fd90c.jpg
Hotteok, South Korean,Sweet and Chewy,Dessert,100-150,,https://whatgreatgrandmaate.com/wp-content/uploads/2023/06/hotteok-sq.jpg
Kimbap, South Korean,Savory and Portable,Snack,30-50,,https://www.koreanbapsang.com/wp-content/uploads/2018/09/DSC8399-2-e1696691292303.jpg
Jjapaghetti,Korean,salty,One-dish,30-50,,https://futuredish.com/wp-content/uploads/2020/09/Jjapaghetti-8-1.jpg
Odeng, South Korean,Savory and Fish Cake,Snack,50-100,,https://futuredish.com/wp-content/uploads/2017/10/Korean-Eomuk.jpg
Korean BBQ, South Korean,Savory and Grilled,Meat,50-100,pork,"https://hips.hearstapps.com/vidthumb/images/korean-bbq-chicken-skewers-644164f0b56bc.jpg?crop=1xw:1xh;center,top&resize=1200:*"
Bindaetteok, South Korean,Savory and Mung Bean Pancake,Snack,30-50,vegetable,https://platefulofveggies.com/wp-content/uploads/2021/01/mung-bean-pancake.jpg
Pajeon, South Korean,Savory and Scallion Pancake,Snack,30-50,vegetable,https://www.maangchi.com/wp-content/uploads/2011/03/pajeonwithsauce-590x504.jpg
Gungjung Tteokbokki, South Korean,Sweet and Nutty,Snack,30-50,vegetable,https://static01.nyt.com/images/2021/04/28/dining/kc-tteokbokki/merlin_186997692_0fbd60bd-ed0e-4b1f-adc7-9ebd34d61c21-articleLarge.jpg
Dak Kimchi, South Korean,Spicy and Tangy,Snack,100-150,vegetable,"https://static.wixstatic.com/media/489bd7_9df5e086dc344b3e8881913029fefa05~mv2.jpg/v1/fill/w_266,h_348,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/489bd7_9df5e086dc344b3e8881913029fefa05~mv2.jpg"
Soy Garlic Chicken, South Korean,Savory and Garlicky,Meat,30-50,Chicken,https://takestwoeggs.com/wp-content/uploads/2022/10/Soy-Garlic-Wings-Takestwoeggs-final-photography-sq.jpg
Panzanella,Italian,Savory and Crunchy,One-dish,30-50,vegetable,https://www.foodiecrush.com/wp-content/uploads/2022/06/Panzanella-foodiecrush.com-13.jpg
Osso Buco Alla Milanese,Italian,Savory and Rich,Meat,100-150,Pork,https://www.insidetherustickitchen.com/wp-content/uploads/2021/05/Ossobuco-1200px-inside-the-rustic-kitchen.jpg
Cannoli,Italian,Sweet and Creamy,Dessert,100-150,dessert,https://www.cookingclassy.com/wp-content/uploads/2020/02/cannoli-20.jpg
Pasta Puttanesca,Italian,Savory and Tangy,Noodle,30-50,,https://www.recipetineats.com/wp-content/uploads/2021/08/Spaghetti-Puttanesca_64-SQ.jpg
Caprese Pizza,Italian,Savory and Fresh,One-dish,50-100,,https://www.gozney.com/cdn/shop/articles/Caprese_Pizza_Feng_Chen_leopardcrust_-_Large_b45ed4e9-09f8-4bad-a6e9-f2391392a2a0.jpg?v=1653033792
Pesto Genovese,Italian,Savory and Herbal,Noodle,30-50,vegetable,https://www.sipandfeast.com/wp-content/uploads/2023/07/pesto-alla-genovese-recipe-snippet.jpg
Affogato,Italian,Bitter and Sweet,Dessert,100-150,dessert,https://www.recipetineats.com/wp-content/uploads/2023/06/Affogato_0-SQ.jpg
Pappa al Pomodoro,Italian,Savory and Comforting,Soup,30-50,,https://en.julskitchen.com/wp-content/uploads/sites/2/2017/07/Pappa-al-pomodoro-001.jpg
Tartufo Ice Cream,Italian,Sweet and Truffle-flavored,Dessert,30-50,dessert,"https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipe%20Ramp%20Up%2F2021-08-Tartufo%2FTartufo_3_01"
Margherita Pizza,Italian,Savory and Cheesy,One-dish,50-100,,"https://images.prismic.io/eataly-us/ed3fcec7-7994-426d-a5e4-a24be5a95afd_pizza-recipe-main.jpg?auto=compress,format"
Ravioli,Italian,Savory and Filled,One-dish,50-100,Seafood,https://cdn11.bigcommerce.com/s-cjh14ahqln/product_images/uploaded_images/cheese-ravioli-2-web.jpg
Torta Caprese,Italian,Chocolate and Nutty,Dessert,30-50,dessert,https://www.giallozafferano.com/images/227-22721/torta-caprese-chocolate-cake_1200x800.jpg
Gnocchi,Italian,Savory and Soft,One-dish,30-50,,https://img.delicious.com.au/sSc-RuJP/del/2022/05/gnocchi-168125-1.png
Caponata,Italian,Sweet and Sour,Snack,30-50,vegetable,"https://assets.epicurious.com/photos/642aedcf23c7d3bf4c8df1d4/1:1/w_4634,h_4634,c_limit/Caponata_RECIPE_033023_50007.jpg"
Tiramisu Gelato,Italian,Sweet and Smooth,Dessert,100-150,dessert,https://www.recipesfromitaly.com/wp-content/uploads/2023/06/tiramisu-gelato-recipe-1x1-1200x1200-1.jpg
Pasta Carbonara,Italian,Savory and Creamy,Noodle,50-100,pork,https://www.cookingclassy.com/wp-content/uploads/2020/10/spaghetti-carbonara-01.jpg
Prosciutto e Melone,Italian,Salty and Sweet,Snack,30-50,,https://italianchef.com/wp-content/uploads/2011/07/ProsciuttoAndMelon.jpg
Amatriciana,Italian,Savory and Tangy,Noodle,30-50,,https://assets.bonappetit.com/photos/57afff221b33404414976058/master/pass/bucatini-all-amatriciana.jpg
Focaccia,Italian,Savory and Herby,Snack,30-50,,https://www.177milkstreet.com/assets/site/Recipes/_large/Tomato-Olive-Focaccia.jpg
Ossobuco,Italian,Savory and Rich,Meat,100-150,pork,https://www.insidetherustickitchen.com/wp-content/uploads/2021/05/Ossobuco-1200px-inside-the-rustic-kitchen.jpg
Fettuccine Alfredo,Italian,Creamy and Savory,One-dish,50-100,,https://www.allrecipes.com/thmb/8W5wmwmSqlRYoTQJ9BTid-yo1bM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8065111-b0dbefd1f1b343259810f4771829f970.jpg
Minestrone,Italian,Savory and Hearty,Soup,30-50,Pork,https://www.spendwithpennies.com/wp-content/uploads/2022/02/Minestrone-Soup-SpendWithPennies-7.jpg
Tiramisu,Italian,Sweet and Coffee-flavored,Dessert,100-150,dessert,https://www.culinaryhill.com/wp-content/uploads/2021/01/Tiramisu-Culinary-Hill-1200x800-1.jpg
Risotto,Italian,Creamy,One-dish,30-50,vegetable,https://sugarspunrun.com/wp-content/uploads/2021/02/Easy-Risotto-Recipe-1-of-1.jpg
Lasagna,Italian,Savory and Hearty,One-dish,50-100,Pork,https://static01.nyt.com/images/2023/08/31/multimedia/RS-Lasagna-hkjl/RS-Lasagna-hkjl-superJumbo.jpg
Bruschetta,Italian,Savory and Fresh,Snack,30-50,,https://natashaskitchen.com/wp-content/uploads/2020/07/Tomato-Bruschetta-Recipe-7.jpg
Caprese Salad,Italian,Fresh and Light,One-dish,50-100,vegetable,https://natashaskitchen.com/wp-content/uploads/2019/08/Caprese-Salad-6.jpg
Matcha Gelato,Italian,Sweet and Smooth,Dessert,50-100,dessert,https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Gelato.jpg/640px-Gelato.jpg
Vegan chicken,chinese,salty,snack,30-50,chicken,https://fullofplants.com/wp-content/uploads/2019/04/the-best-vegan-chickn-shredded-tender-seitan-thumb-1400x1400.jpg
fry chicken(thai),thai,savory,snack,10-50,chicken,https://www.seriouseats.com/thmb/Mdc2XIiGIi9WQpzMc3QGlHO1q7U=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2012__03__20120314-197278-thai-deep-fried-chicken-primary-4b0561b0ae0d4f6fa9cc9fceae208518.jpg
new orleans chicken,thai,savory,snack,50-150,chicken,https://www.seriouseats.com/thmb/enKXosffA-Vl-A3YMh9kTVtMu5M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cajun-chicken-wings-recipe-hero-03_1-e927580737e24730b053c1c99bcd6a29.JPG
chocolate frappe,,sweet,beverage,30-80,dessert,https://www.whiskaffair.com/wp-content/uploads/2020/08/Chocolate-Chip-Frappe-2-3.jpg
Katsu curry (pork curry rice),japanese,spicy,one-dish,60-150,pork,https://lh6.googleusercontent.com/9ijNJx1Ju7LV8pNO3x1VQU4iOav3HSSEBqpZADVmcLFhKuQ0rdfPwxpy6AVPjWOcDFw-r_jhkGG7Y1AsQIwqIi7obuz4Y0495Z3rkm0s_uBAI9q_aKR3pd0iPM70tQqltbdo2ISN
coconut chicken curry,thai,spicy,main course,30-60,chicken,https://www.jocooks.com/wp-content/uploads/2019/10/coconut-chicken-curry-1-10.jpg
katsudon,japanese,savory,one-dish,60-150,pork,https://www.marionskitchen.com/wp-content/uploads/2019/07/Katsudon-01.jpg
thai fried oysters,thai,savory,appetizer,60-150,seafood,https://1.bp.blogspot.com/-zDYcTZVs7dQ/URIUv0Y2lHI/AAAAAAAAEnc/omoTSXzJm7U/s1600/RIMG4964.JPG
Ebi fry(fry shrimp),japanese,savory,snack,60-100,seafood,https://www.thespruceeats.com/thmb/5xkGMB8ZXz3KGF_y4Uxf7ZfQAvQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/ebi-fry-fried-shrimp-2031450-hero-01-46c436a89c164a9ab5980f888097fcd2.jpg
italian pork burger,italian,savory,snack,60-100,pork,https://www.certifiedangusbeef.com/recipes/images/recipes/3136762e-bb5b-40af-b6a1-fa7380a70c93.jpg
Italian porkchop,italian,savory,one-dish,50-100,https://lilluna.com/wp-content/uploads/2017/10/italian-pork-chops-resize-4.jpg
dorayaki,Japan,sweet,dessert,20-50,dessert,https://www.honestfoodtalks.com/wp-content/uploads/2022/02/Dorayaki-recipe-red-bean.jpg
Thong yod,thai,sweet,dessert,20-40,dessert,https://www.thaifoodplus.com/wp-content/uploads/2017/02/Thong-yot.jpg
Foi thong,thai,sweet,dessert,20-40,dessert,https://kanomsiam.com/cdn/shop/products/CHEM0490.jpg?v=1589266928
chocolate cake,,sweet,dessert,60-150,dessert,https://hips.hearstapps.com/hmg-prod/images/chocolate-cake-index-64b83bce2df26.jpg?crop=0.6668359143606668xw:1xh;center,top&resize=1200:*
ice cream cake,,sweet,dessert,60-150,dessert,https://www.cookingclassy.com/wp-content/uploads/2022/08/ice-cream-cake-11.jpg
Oreo ice cream cake,,sweet,dessert,60-150,dessert,https://sugargeekshow.com/wp-content/uploads/2021/03/oreo_icecream_cake_recipe_featured.jpg
Cake roll,,sweet,dessert,20-50,dessert,https://i0.wp.com/smittenkitchen.com/wp-content/uploads//2018/05/ice-cream-cake-roll.jpg?fit=1200%2C800&ssl=1
cheesecake,,sweet,dessert,70-150,dessert,https://hips.hearstapps.com/hmg-prod/images/strawberry-shortcake-ice-cream-cake-1660592794.jpeg?crop=1xw:0.7973582474226805xh;center,top&resize=1200:*
berry cheesecake,,sweet,dessert,70-150,dessert,https://i0.wp.com/www.womensweeklyfood.com.au/wp-content/uploads/sites/4/2015/12/09/31196/HL0878-CHRISTMAS-ICE-CREAM-015.jpg?resize=980%2C980&ssl=1
christmas cake,,sweet,dessert,70-150,dessert,https://food.fnr.sndimg.com/content/dam/images/food/fullset/2021/11/19/Bakery_Inspired_Christmas_Wreath_Layer_Cake_2021_s4x3.jpg.rend.hgtvcom.1280.1280.suffix/1637351961661.jpeg
chocolate ice cream,,sweet,dessert,10-40,dessert,https://www.cookingclassy.com/wp-content/uploads/2023/07/chocolate-ice-cream-5.jpg
strawberry ice cream,,sweet,dessert,10-40,dessert,https://www.thespruceeats.com/thmb/kpuMkqk0BhGMTuSENf_IebbHu1s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/strawberry-ice-cream-10-0b3e120e7d6f4df1be3c57c17699eb2c.jpg
milk ice cream,,sweet,dessert,10-40,dessert,https://www.wikihow.com/images/e/e4/Make-Ice-Cream-with-Milk-Step-22-Version-2.jpg
lemon ice cream,,sweet,dessert,10-40,dessert,https://icecreamfromscratch.com/wp-content/uploads/2022/05/Lemon-Ice-Cream-1.2-735x1103.jpg
strawberry cake,,sweet,dessert,60-150,dessert,https://www.allrecipes.com/thmb/Huh-I63aYc_zZ0NbLECEpFD0BcI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/60564-StrawberryCakeFromScratch-ddfms-4X3-0291-1-cd8254e28ea14112b5fc49e25cd08ff6.jpg
strawberry crape,,sweet,dessert,30-70,dessert,https://www.shutterstock.com/image-photo/strawberry-crepes-isolated-on-white-260nw-1182343741.jpg
sushi salmon,japanese,savory,snack,20-50,seafood,https://izzycooking.com/wp-content/uploads/2020/10/Salmon-Nigiri-thumbnail.jpg
sashimi,japanese,savory,snack,50-150,seafood,https://images.immediate.co.uk/production/volatile/sites/30/2020/02/sashimi-c123df7.jpg?quality=90&resize=556,505
Teriyaki chicken,japanese,savory,main course,50-150,chicken,https://static01.nyt.com/images/2016/05/28/dining/28COOKING-CHICKEN-TERIYAKI1/28COOKING-CHICKEN-TERIYAKI1-articleLarge.jpg?w=1280&q=75
beef sukiyaki,japanese,savory,main course,100-150,,https://www.hairybikers.com/uploads/images/_recipeImage/BeefSukiyaki.jpg
yakisoba,japanese,savory,one-dish,50-120,vegetable,https://www.jocooks.com/wp-content/uploads/2021/06/yakisoba-1-11.jpg
saba no shioaki,japanese,savory,one-dish,100-150,seafood,https://sudachirecipes.com/wp-content/uploads/2022/08/saba-no-shioyaki-thumbnail.jpg
gyudon,japanese,savory,one-dish,100-150,,https://twoplaidaprons.com/wp-content/uploads/2022/09/gyudon-in-bowl-thumbnail.jpg
KFC Wing zab chicken,thai,savory,snack,30-50,chicken,https://i.pinimg.com/originals/4a/44/9f/4a449fe9f13bd5a30d1c6477b5660b0b.jpg
italian cheeseburger,italian,savory,one-dish,100-150,pork,https://www.joyfulhealthyeats.com/wp-content/uploads/2015/05/Italian-Cheeseburger-23-Joyful-Healthy-Eats-041823.jpg
japanese hamburger,japanese,savory,one-dish,100-150,pork,https://www.justonecookbook.com/wp-content/uploads/2020/06/Japanese-Hamburger-Steak-Hambagu-1214-I-1-500x375.jpg
Espresso coffee,,bitter,beverage drink,40-100,,https://www.aromathailand.com/wp-content/uploads/2023/04/Cover-Espresso-1080x675.jpg
Café Americano,,bitter,beverage drink,40-100,,https://ajnownirun.files.wordpress.com/2015/02/americano.jpg
Latte,,sweet & bitter,beverage drink,40-100,,https://www.foodandwine.com/thmb/CCe2JUHfjCQ44L0YTbCu97ukUzA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Partners-Latte-FT-BLOG0523-09569880de524fe487831d95184495cc.jpg
Strawberry frappe,,sweet,beverage drink,60-120,dessert,https://shottbeverages.com/wp-content/uploads/2020/08/strawberry_frappe.jpg
Oreo frappe,,sweet,beverage drink,60-120,dessert,https://myveganminimalist.com/wp-content/uploads/2021/12/Oreo-Frappe-DIY-6-Ingredient-Chocolate-Frappuccino-2.jpg
orange juice,,sweet sour,beverage drink,30-50,,https://upload.wikimedia.org/wikipedia/commons/0/05/Orangejuice.jpg
watermelon juice,,sweet,beverage drink,30-50,,https://www.thatcutedish.com/wp-content/uploads/2023/06/frozen-watermelon-juice-korean-style-1.jpg
banana frappe,,sweet,beverage drink,30-60,dessert,https://tornadoughalli.com/wp-content/uploads/2017/07/Banana-Cream-Frappe3-2.jpg
thai coconut pancake,thai,sweet,dessert,10-30,dessert,https://images.squarespace-cdn.com/content/v1/560c9d6fe4b081f0a96ec772/1598685184461-DZLY3P90BKPZYHYRFARR/babin-pancake.jpg?format=2500w
Bread with jam,,sweet,dessert,10-30,,https://monksbread.com/cdn/shop/products/breadJam-1-2_1024x.jpg?v=1594393100
bacon salad(healthy),italian,savory,salad vegetable,100-150,pork vegetable,https://cleanfoodcrush.com/wp-content/uploads/2020/09/CleanFoodCrush-Healthy-Printable-Recipe-Broccoli-Fresh-Corn-Bacon-Salad.jpg
pork salad(healthy),italian,savory,salad,100-150,vegetable,https://www.tasteofhome.com/wp-content/uploads/2018/01/Savory-Pork-Salad_EXPS_CF2BZ19_35244_E12_13_2b-4.jpg
Salmon salad(healthy),italian,savory,salad,100-150,seafood vegetable,https://www.primaverakitchen.com/wp-content/uploads/2020/01/Easy-Chopped-Salmon-Salad-Primavera-Kitchen-1.jpg
Caesar salad(healthy),italian,savory,salad,100-150,vegetable,https://www.asweetpeachef.com/wp-content/uploads/2010/06/Chicken-Caesar-Salad-17-500x500.jpg
Strawberry juice(healthy),,sweet,beverage drink,50-100,,https://cdn3.foodviva.com/static-content/food-images/juice-recipes/strawberry-juice-recipe/strawberry-juice-recipe.jpg
mango juice(healthy),,sweet,beverage drink,50-100,,https://www.theconsciousplantkitchen.com/wp-content/uploads/2022/06/Mango-Juice-9.jpg
Avocado juice(healthy),,sweet,beverage drink,40-100,,https://cdn.loveandlemons.com/wp-content/uploads/2017/08/avocado-smoothie-recipe.jpg
Sashimi salad(healthy),japanese,savory,salad,100-150,seafood vegetable,,https://assets.epicurious.com/photos/555cf321644d45515b759070/master/pass/51221630_sashimi-salad-with-soy-orange_6x4.jpg
Tuna spicy salad(healthy),,spicy,salad,100-150,,https://www.marionskitchen.com/wp-content/uploads/2020/01/Spicy-Thai-style-Tuna-Salad4.jpg
Tako spicy salad(healthy),,spicy,salad,100-150,seafood vegetable,https://www.eatingbirdfood.com/wp-content/uploads/2021/01/healthy-taco-salad-overhead.jpg
black coffee,,bitter,beverage drink,30-100,,https://www.sharmispassions.com/wp-content/uploads/2021/05/BlackCoffee4.jpg
Milk coffee,,mild sweet,beverage drink,30-100,,https://sakiproducts.com/cdn/shop/articles/20230125111927-turkish-coffee-with-milk-recipe-blog_1200x1200.webp?v=1674645576
bubble milk tea,,sweet,beverage drink,25-100,dessert,https://assets.epicurious.com/photos/629f98926e3960ec24778116/4:3/w_4658,h_3493,c_limit/BubbleTea_RECIPE_052522_34811.jpg
milk iced tea,,mild sweet,beverage drink,25-100,dessert,https://brewedleaflove.com/wp-content/uploads/2023/03/milk-tea-without-boba.jpg
ice green tea latte,,mild sweet,beverage drink,25-100,dessert,https://www.starbucks.co.th/stb-media/2020/08/81.Iced-Green-Tea-Latte1080.png
thai iced tea,thai,sweet,beverage drink,25-100,dessert,https://sakiproducts.com/cdn/shop/articles/20230310181037-thai-tea-recipe_1200x1200.webp?v=1678471844
hot coco,,sweet,beverage drink,30-100,dessert,https://feelgoodfoodie.net/wp-content/uploads/2021/11/how-to-make-hot-chocolate-7.jpg
Milkshake,,sweet,beverage drink,40-100,dessert,https://preppykitchen.com/wp-content/uploads/2021/04/Milkshake-Recipe-Card.jpg
Caramel milkshake,,sweet,beverage drink,45-100,dessert,https://bakingmischief.com/wp-content/uploads/2020/04/caramel-milkshake-image-square.jpg
lemon juice(healthy),,sweet,beverage drink,30-100,,https://hips.hearstapps.com/hmg-prod/images/lemon-juice-royalty-free-image-510180395-1531432390.jpg?crop=1.00xw:0.717xh;0,0.157xh&resize=640:*
"""

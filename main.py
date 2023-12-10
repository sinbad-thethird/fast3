#ใช้อันนี้ ใช้ได้แล้ว
#uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import csv
import random

app = FastAPI()

# Enable CORS for all routes (only for development, consider restricting it in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change as needed)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FoodRequest(BaseModel):
    random: str = None
    avoid: str = None
    nation: str = None
    taste: str = None
    price: str = None
    type: str = None
    mood: str = None
def get_random_recommendations(food_list: List[str]):
    return random.sample(food_list, min(5, len(food_list)))


# Load CSV data
csv_data = """
foodname,country,taste,type,price,avoid,mood
Pad Thai,thai,salty & spicy & umami,one-dish & seafood ,30-50 or 50-100,seafood,happy & energetic & comfort
Thai noodle seafood,thai,salty & umami  ,one-dish,50-100,seafood,happy & energetic & comfort
krapao pla,thai,salty umami ,one-dish,50-100,seafood,happy & energetic & comfort
krapao kung,thai,salty umami,one-dish,50-100,seafood,happy & energetic & comfort
crab fried rice,thai,salty umami,one-dish,50-100,seafood,happy & energetic & comfort
fire squid with curry,thai,salty umami,one-dish,50-100,seafood,happy & energetic & comfort
Tom Yum Spicy Soup,Thai,spicy salty,soup,50-100,seafood,energetic & happy & comfort
Mango Sticky Rice,Thai,sweet umami,dessert,50-100,,happy & energetic & comfort
Som Tum,Thai,spicy sour,salad,50-100,,angry & energetic & comfort
Khao Pad,Thai,umami salty,one-dish,40-80,,happy & energetic & comfort
Pad Kra Paw Moo,Thai,salty spicy umami,one-dish,40-80,pork,happy & energetic & comfort
Mama Phad,Thai,salty spicy umami,one-dish,40-80,,happy & energetic & comfort
Coconut Milk Ice Cream,Thai,sweet umami,dessert,10-30,,happy & energetic & comfort
Sushi,Japan,salty umami salty,snack,30-50,,happy& energetic & comfort
Ramen,Japan,salty umami salty,soup,30-50,pork,happy & energetic & comfort
Pasta,Italy,salty umami salty,meat,40-80,seafood,happy & energetic & comfort
Bibimbap,Korea,spicy salty,one-dish,40-80,,happy & energetic & comfort
Hot Pot,Chinese,salty,soup,50-100,seafood,happy & energetic & comfort
Dumplings,Chinese,salty,snack,30-50,chicken,happy & energetic & comfort
Tom Yum Goong,Thai,Spicy and Sour,Soup,50-100,Seafood,Energetic 
Pad See Ew,Thai,Salty and Sweet,Fry,30-50,None,Satisfied
Green Curry,Thai,Spicy,Soup,50-100,Chicken,Comfort
Som Tum,Thai,Spicy and Sour,Snack,10-30,None,Joyful
Massaman Curry,Thai,Spicy and Umami,Soup,100-150,None,Happy
Pad Kra Pao,Thai,Spicy and Salty,Meat,50-100,Pork,Angry
Tom Kha Gai,Thai,Umami and Spicy,Soup,30-50,Chicken,Sad
Moo Ping,Thai,Sweet and Savory,One-dish,10-30,None,Lonely
Khao Soi,Thai,Creamy and Spicy,One-dish,50-100,Chicken,Joyful
Pla Rad Prik,Thai,Spicy and Salty,Seafood,100-150,seafood,Satisfied
Green Papaya Salad,Thai,Spicy and Sour,Snack,10-30,None,Joyful
Pad Thai,Thai,Salty and Sweet,Noodle,30-50,Peanuts,Happy
Kai Med Ma Muang,Thai,Sweet and Spicy,Meat,30-50,None,Satisfied
Yam Talay,Thai,Spicy and Sour,Seafood,50-100,None,Joyful
Khao Niew Mamuang,Thai,Sweet and Sticky,Dessert,10-30,None,Happy
Gaeng Keow Wan Kai,Thai,Spicy and Sweet,Curry,50-100,None,Satisfied
Pla Pao,Thai,Salty and Grilled,Seafood,100-150,seafood,Comfort
Larb Gai,Thai,Spicy and Tangy,One-dish,30-50,None,Joyful
Khao Pad,Thai,Savory,One-dish,30-50,None,Satisfied
Tod Mun Pla,Thai,Spicy and Crispy,Snack,10-30,None,Joyful
Sashimi,Japanese,Umami,Seafood,100-150,None,Energetic
Tempura,Japanese,Salty and Crispy,Fry,50-100,None,Satisfied
Ramen,Japanese,Umami,Soup,30-50,Egg,Comfort
Chirashi Sushi,Japanese,Umami,Seafood,100-150,None,Joyful
Okonomiyaki,Japanese,Savory and Salty,Fry,50-100,Pork,Happy
Yakitori,Japanese,Salty and Grilled,Meat,30-50,Pork,Satisfied
Miso Soup,Japanese,Umami,Soup,10-30,None,Angry
Udon,Japanese,Umami,Soup,50-100,Pork,Sad
Gyoza,Japanese,Umami and Crispy,Fry,30-50,Pork,Joyful
Hōtō,Japanese,Umami and Comforting,Soup,50-100,None,Lonely
Tonkatsu,Japanese,Savory and Crispy,Fry,50-100,None,Comfort
Pizza Margherita,Italian,Savory and Cheesy,One-dish,50-100,None,Happy
Ossobuco,Italian,Savory and Rich,Meat,100-150,Pork,Satisfied
Fettuccine Alfredo,Italian,Creamy and Savory,One-dish,50-100,None,Joyful
Minestrone,Italian,Savory and Hearty,Soup,30-50,Pork,Angry
Tiramisu,Italian,Sweet and Coffee-flavored,Dessert,10-30,None,Happy
Risotto,Italian,Creamy,One-dish,30-50,None,Happy
Lasagna,Italian,Savory and Hearty,One-dish,50-100,Pork,Comfort
Bruschetta,Italian,Savory and Fresh,Snack,30-50,None,Joyful
Caprese Salad,Italian,Fresh and Light,One-dish,50-100,None,Happy
Gelato,Italian,Sweet and Smooth,Dessert,10-30,None,Happy
Kimchi,South Korean,Spicy and Sour,Snack,30-50,None,Energetic
Bulgogi,South Korean,Sweet and Savory,Meat,50-100,None,Satisfied
Japchae,South Korean,Savory and Sweet,Fry,30-50,None,Joyful
Samgyeopsal,South Korean,Savory,Meat,30-50,None,Satisfied
Dolsot Bibimbap,South Korean,Spicy and Savory,One-dish,50-100,None,Joyful
Haemul Pajeon,South Korean,Savory and Crispy,Seafood,30-50,Seafood,Satisfied
Sundubu Jjigae,South Korean,Spicy and Umami,Soup,10-30,None,Angry
Kimchi Jjigae,South Korean,Spicy and Sour,Soup,30-50,None,Sad
Tteokbokki,South Korean,Spicy and Sweet,Snack,10-30,None,Joyful
Yangnyeom Chicken,South Korean,Spicy and Sweet,Fry,30-50,None,Satisfied
Peking Duck,Chinese,Sweet and Crispy,Meat,150-250,None,Happy
Dim Sum,Chinese,Various Flavors,Snack,50-100,None,Joyful
Hot and Sour Soup,Chinese,Spicy and Sour,Soup,30-50,None,Comfort
General Tso's Chicken,Chinese,Sweet and Spicy,Fry,50-100,None,Satisfied
Mapo Tofu,Chinese,Spicy and Umami,One-dish,30-50,None,Joyful
Chow Mein,Chinese,Savory and Crispy,Noodle,50-100,None,Satisfied
Sweet and Sour Pork,Chinese,Sweet and Tangy,Meat,50-100,None,Happy
Spring Rolls,Chinese,Crispy and Fresh,Snack,30-50,None,Joyful
Kung Pao Chicken,Chinese,Spicy and Nutty,Meat,50-100,Peanuts,Satisfied
Fried Rice,Chinese,Savory,One-dish,30-50,None,Comfort
Szechuan Shrimp,Chinese,Spicy and Savory,Seafood,50-100,None,Joyful
Mongolian Beef,Chinese,Savory and Sweet,Meat,50-100,None,Happy
Crab Rangoon,Chinese,Creamy and Crispy,Snack,30-50,None,Joyful
Egg Drop Soup,Chinese,Simple and Comforting,Soup,10-30,None,Comfort
Ma Po Eggplant,Chinese,Spicy and Umami,Vegetarian,30-50,None,Satisfied
Scallion Pancakes,Chinese,Savory and Crispy,Snack,30-50,None,Joyful
Honey Walnut Shrimp,Chinese,Sweet and Nutty,Seafood,100-150,None,Happy
Sesame Chicken,Chinese,Sweet and Nutty,Fry,50-100,None,Satisfied
Vegetable Lo Mein,Chinese,Savory and Vegetarian,Noodle,30-50,None,Comfort
Wonton Soup,Chinese,Simple and Comforting,Soup,10-30,None,Happy
Foodname,Country,Taste,Type,Price,Avoid,Mood
Green Mango Salad,Thai,Sour and Spicy,Snack,10-30,None,Energetic
Khao Man Gai,Thai,Savory and Ginger,One-dish,30-50,None,Satisfied
Sticky Rice with Mango,Thai,Sweet and Creamy,Dessert,10-30,None,Happy
Tom Yum Talay,Thai,Spicy and Sour,Seafood,50-100,None,Joyful
Yum Woon Sen,Thai,Spicy and Tangy,Seafood,30-50,None,Joyful
Kao Pad Tom Yum,Thai,Spicy and Savory,One-dish,30-50,None,Comfort
Larb Moo,Thai,Spicy and Tangy,Meat,30-50,Chicken,Joyful
Kai Jeow,Thai,Savory and Crispy,One-dish,10-30,None,Satisfied
Massaman Neua,Thai,Sweet and Savory,Curry,50-100,None,Happy
Pad Krapow Moo Saap,Thai,Spicy and Salty,Meat,50-100,Pork,Angry
Shrimp Tempura,Japanese,Salty and Crispy,Fry,50-100,None,Satisfied
Chawanmushi,Japanese,Savory and Silky,Snack,30-50,None,Comfort
Nikujaga,Japanese,Sweet and Savory,One-dish,30-50,None,Satisfied
Unagi Don,Japanese,Sweet and Grilled,One-dish,100-150,None,Happy
Sushi Rolls,Japanese,Various Flavors,Snack,50-100,None,Joyful
Hokkaido Soup Curry,Japanese,Spicy and Comforting,Soup,50-100,None,Comfort
Takoyaki,Japanese,Savory and Octopus,Snack,30-50,None,Satisfied
Hōrensō no Goma-ae,Japanese,Savory and Nutty,Vegetarian,10-30,None,Happy
Yudofu,Japanese,Simple and Comforting,Soup,30-50,None,Lonely
Matcha Ice Cream,Japanese,Bitter and Sweet,Dessert,10-30,None,Happy
Margherita Pizza,Italian,Savory and Cheesy,One-dish,50-100,None,Happy
Ravioli,Italian,Savory and Filled,One-dish,50-100,Seafood,Comfort
Torta Caprese,Italian,Chocolate and Nutty,Dessert,30-50,None,Happy
Gnocchi,Italian,Savory and Soft,One-dish,30-50,None,Satisfied
Caponata,Italian,Sweet and Sour,Snack,30-50,None,Joyful
Tiramisu Gelato,Italian,Sweet and Smooth,Dessert,10-30,None,Happy
Pasta Carbonara,Italian,Savory and Creamy,Noodle,50-100,None,Comfort
Prosciutto e Melone,Italian,Salty and Sweet,Snack,30-50,None,Joyful
Amatriciana,Italian,Savory and Tangy,Noodle,30-50,None,Satisfied
Focaccia,Italian,Savory and Herby,Snack,30-50,None,Joyful
Bibimbap, South Korean,Spicy and Savory,One-dish,50-100,None,Joyful
Samgyetang, South Korean,Savory and Comforting,Soup,50-100,None,Comfort
Jajangmyeon, South Korean,Savory and Rich,Noodle,30-50,Seafood,Satisfied
Kimchi Fried Rice, South Korean,Spicy and Savory,One-dish,30-50,None,Joyful
Dak Galbi, South Korean,Spicy and Sweet,Meat,50-100,None,Happy
Sannakji, South Korean,Crispy and Fresh,Seafood,50-100,None,Joyful
Kimchi Pancake, South Korean,Savory and Crispy,Snack,30-50,None,Satisfied
Banchan, South Korean,Various Flavors,Snack,10-30,None,Joyful
Budae Jjigae, South Korean,Spicy and Umami,Soup,50-100,None,Comfort
Hoeddeok, South Korean,Sweet and Chewy,Dessert,10-30,None,Happy
Peking Noodles, Chinese,Savory and Spicy,Noodle,30-50,None,Joyful
Moo Shu Pork, Chinese,Savory and Sweet,One-dish,30-50,None,Satisfied
Shrimp Dumplings, Chinese,Savory and Juicy,Snack,30-50,None,Happy
Pineapple Bun, Chinese,Sweet and Crispy,Snack,10-30,None,Joyful
Zongzi, Chinese,Savory and Sticky,Snack,30-50,None,Satisfied
Duck Spring Rolls, Chinese,Crispy and Flavorful,Snack,30-50,None,Joyful
Lanzhou Beef Noodle Soup, Chinese,Savory and Spicy,Soup,50-100,None,Comfort
Dan Dan Noodles, Chinese,Spicy and Nutty,Noodle,30-50,Peanuts,Satisfied
Mooncakes, Chinese,Sweet and Filled,Dessert,30-50,None,Happy
Sichuan Hot Pot, Chinese,Spicy and Savory,Soup,50-100,Seafood,Comfort
Foodname,Country,Taste,Type,Price,Avoid,Mood
Laab Gai,Thai,Spicy and Tangy,Meat,30-50,None,Joyful
Kao Niew Neung Mamuang,Thai,Sweet and Fruity,Dessert,10-30,None,Happy
Pla Kapong Neung Manao,Thai,Sour and Spicy,Seafood,100-150,None,Joyful
Pad Kana Moo Krob,Thai,Salty and Crispy,Meat,50-100,None,Comfort
Khao Pad Sapparod,Thai,Sweet and Savory,One-dish,30-50,None,Satisfied
Ebi Nigiri,Japanese,Savory and Sweet,Snack,50-100,None,Happy
Saba Shioyaki,Japanese,Salty and Grilled,Seafood,30-50,None,Satisfied
Yaki Udon,Japanese,Savory and Stir-fried,Noodle,50-100,None,Joyful
Tamago Sushi,Japanese,Sweet and Eggy,Snack,30-50,None,Happy
Sukiyaki,Japanese,Savory and Sweet,One-dish,100-150,None,Comfort
Panzanella,Italian,Savory and Crunchy,One-dish,30-50,None,Joyful
Osso Buco Alla Milanese,Italian,Savory and Rich,Meat,100-150,Pork,Satisfied
Cannoli,Italian,Sweet and Creamy,Dessert,10-30,None,Happy
Pasta Puttanesca,Italian,Savory and Tangy,Noodle,30-50,None,Comfort
Caprese Pizza,Italian,Savory and Fresh,One-dish,50-100,None,Joyful
Pesto Genovese,Italian,Savory and Herbal,Noodle,30-50,None,Satisfied
Affogato,Italian,Bitter and Sweet,Dessert,10-30,None,Happy
Pappa al Pomodoro,Italian,Savory and Comforting,Soup,30-50,None,Comfort
Tartufo Ice Cream,Italian,Sweet and Truffle-flavored,Dessert,30-50,None,Happy
Kimbap, South Korean,Savory and Portable,Snack,30-50,None,Joyful
Japaghetti, South Korean,Savory and Black Bean Noodles,One-dish,30-50,None,Satisfied
Odeng, South Korean,Savory and Fish Cake,Snack,10-30,None,Joyful
Korean BBQ, South Korean,Savory and Grilled,Meat,50-100,None,Comfort
Bindaetteok, South Korean,Savory and Mung Bean Pancake,Snack,30-50,None,Satisfied
Pajeon, South Korean,Savory and Scallion Pancake,Snack,30-50,None,Joyful
Gungjung Tteokbokki, South Korean,Sweet and Nutty,Snack,30-50,None,Happy
Dak Kimchi, South Korean,Spicy and Tangy,Snack,10-30,None,Joyful
Soy Garlic Chicken, South Korean,Savory and Garlicky,Meat,30-50,None,Satisfied
Chili Oil Wontons, Chinese,Spicy and Umami,Snack,30-50,Seafood,Joyful
Baozi, Chinese,Savory and Steamed,Snack,10-30,None,Happy
Cantonese Roast Duck, Chinese,Savory and Roasted,Meat,50-100,None,Satisfied
Malatang, Chinese,Spicy and Numbing,Soup,30-50,None,Comfort
Dan Dan Mian, Chinese,Spicy and Nutty,Noodle,30-50,Peanuts,Joyful
Xiao Long Bao, Chinese,Savory and Soupy,Dumpling,30-50,None,Happy
Chrysanthemum Fish, Chinese,Savory and Floral,Seafood,100-150,None,Joyful
Suan La Tang, Chinese,Spicy and Sour,Soup,30-50,None,Comfort
Shengjian Bao, Chinese,Savory and Pan-fried,Dumpling,30-50,None,Satisfied
Zha Jiang Mian, Chinese,Savory and Bean Sauce,Noodle,30-50,None,Joyful

"""

csv_lines = csv_data.strip().split('\n')
field_names = csv_lines[0].split(',')
food_data = [dict(zip(field_names, line.split(','))) for line in csv_lines[1:]]

def get_random_foods():
    return random.sample([food['foodname'] for food in food_data], min(5, len(food_data)))

@app.post("/api/recommend")
def recommend_food(request: FoodRequest):
    try:
        data = request.dict()
        if 'random' in data and data['random'].lower() == 'yes':
            random_food_names = get_random_foods()
            return  random_food_names
        user_avoid = request.avoid
        user_nation = request.nation
        user_taste = request.taste
        user_price = request.price
        user_type = request.type
        user_mood = request.mood

        A = [food['foodname'] for food in food_data if food['avoid'].lower() != user_avoid.lower()]
        B = [food['foodname'] for food in food_data if food['country'].lower() == user_nation.lower()]
        Intersection_of_nationandavoid = list(set(A).intersection(B))
        D = [food['foodname'] for food in food_data if user_taste.lower() in food['taste'].lower()]
        E = list(set(D).intersection(Intersection_of_nationandavoid))
        F = [food['foodname'] for food in food_data if user_price.lower() in food['price'].lower()]
        g = list(set(F).intersection(E))
        H = [food['foodname'] for food in food_data if user_type.lower() in food['type'].lower()]
        j = list(set(H).intersection(g))
        L = [food['foodname'] for food in food_data if user_mood.lower() in food['mood'].lower()]
        k = list(set(j).intersection(L))
        final_element = len(k)

        if final_element == 5:
            recommended_food = k
            return {"recommended_food": recommended_food}
        elif final_element > 5:
            recommended_food = get_random_recommendations(k)
            return {"recommended_food": recommended_food[:5]} #กลับไปแค่5ตัว
        else:  # final_element < 5
                c = 0
                recommended_food = []
                
                # Randomly select from 'j'
                random_j_elements = get_random_recommendations(j)
                recommended_food.extend(random_j_elements)
                c += len(random_j_elements)

                # Check if 'j' has enough elements to reach 5
                if c < 5:
                    # Randomly select additional elements from 'k'
                    remaining_k_elements = [food_name for food_name in k if food_name not in random_j_elements]
                    random_k_elements = get_random_recommendations(remaining_k_elements)
                    recommended_food.extend(random_k_elements)
                    c += len(random_k_elements)

                # Check if 'j' and 'k' together have enough elements to reach 5
                if c < 5:
                    # Randomly select additional elements from 'g'
                    remaining_g_elements = [food_name for food_name in g if food_name not in (random_j_elements + random_k_elements)]
                    random_g_elements = get_random_recommendations(remaining_g_elements)
                    recommended_food.extend(random_g_elements)
                    c += len(random_g_elements)

                # Check if 'j', 'k', and 'g' together have enough elements to reach 5
                if c < 5:
                    # Randomly select additional elements from 'E'
                    remaining_E_elements = [food_name for food_name in E if food_name not in (random_j_elements + random_k_elements + random_g_elements)]
                    random_E_elements = get_random_recommendations(remaining_E_elements)
                    recommended_food.extend(random_E_elements)

                return {"recommended_food": recommended_food[:5]}

        



    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")




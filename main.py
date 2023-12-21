#uvicorn bytext:app --reload
from pydantic import BaseModel
from fastapi import FastAPI,Query
from typing import List
import difflib
import csv
from fastapi.middleware.cors import CORSMiddleware
import random
from fooddata import csv_data
from io import StringIO
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Parse CSV data
csv_lines = csv_data.strip().split('\n')
csv_reader = csv.DictReader(csv_lines)
foods = list(csv_reader)


def calculate_similarity(user_input, food):
    # Concatenate values from multiple columns into a single string
    food_description = f"{food['foodname'].lower()} {food['country'].lower()} {food['taste'].lower()} {food['type'].lower()} {food['price'].lower()}"
    # Use difflib to calculate similarity
    similarity_score = difflib.SequenceMatcher(None, user_input, food_description).ratio()
    return similarity_score

@app.post("/recommend")
async def find_food(
    keyword: str = Query(None, title="General Search Keyword", min_length=1),
    avoid_preference: str = Query(None, title="Avoid Preference"),
):
    # If there's no input for keyword, return 5 random foods without the specified avoid preference
    if not keyword and avoid_preference:
        foods_without_avoid = [food for food in foods if avoid_preference.lower() not in food['avoid'].lower()]
        random_foods = random.sample(foods_without_avoid, min(5, len(foods_without_avoid)))
        result = [{"foodname": food['foodname'], "type": food['type'], "price": food['price'], "country": food['country'], "images": food['images']} for food in random_foods]
        return result

    # Filter out foods to avoid
    foods_to_consider = [food for food in foods if avoid_preference.lower() not in food['avoid'].lower()] if avoid_preference else foods

    # If there's no input for both keyword and avoid_preference, return random 5 foods
    if not keyword and not avoid_preference:
        random_foods = random.sample(foods, 5)
        result = [{"foodname": food['foodname'], "type": food['type'], "price": food['price'], "country": food['country'], "images": food['images']} for food in random_foods]
        return result

    # Convert user input to lowercase
    user_input = keyword.lower()

    # Calculate similarity using a more flexible approach
    similarity_scores = [
        (
            food['foodname'],
            food['type'],
            food['price'],
            food['country'],
            food['images'],  # Add 'images' here
            calculate_similarity(user_input, food)
        ) 
        for food in foods_to_consider
    ]

    # Find the top 5 foods with the highest similarity scores
    top_matches = sorted(similarity_scores, key=lambda x: x[5], reverse=True)[:5]

    # Format the results
    result = [{"foodname": foodname, "type": foodtype, "price": foodprice, "country": foodcountry, "images": images}
              for foodname, foodtype, foodprice, foodcountry, images, _ in top_matches]
    return result

def filter_food_by_criteria(data, criteria, header_mapping):
    filtered_food = [food for i, food in enumerate(csv.reader(data.strip().split("\n"))) if i > 0]

    for criterion, value in criteria.items():
        if value and criterion != 'price':
            if criterion == 'avoid':
                avoid_values = [av.lower() for av in value]
                filtered_food = [food for food in filtered_food if not any(any(av.lower() in tag.lower() for tag in food[header_mapping['avoid']].split(',')) for av in avoid_values)]
            elif criterion == 'country':
                # Improved handling of 'country' criterion (case-insensitive and stripping whitespace)
                filtered_food = [food for food in filtered_food if isinstance(food, list) and value.lower().strip() in food[header_mapping[criterion]].lower().strip()]
            else:
                filtered_food = [food for food in filtered_food if isinstance(food, list) and any(val.lower() in food[header_mapping[criterion]].lower() for val in value.split(','))]

        if value and criterion == 'price':
            min_price, max_price = map(int, value.split('-'))
            if isinstance(filtered_food[0][header_mapping[criterion]], list):
                # Case when it's a list
                filtered_food = [food for food in filtered_food if min_price < int(food[header_mapping[criterion]][0].split('-')[0]) < max_price]
            else:
                # Case when it's not a list
                filtered_food = [food for food in filtered_food if min_price < int(food[header_mapping[criterion]].split('-')[0]) < max_price]

    return filtered_food

# รหัสหัวข้อ
header_mapping = {
    'foodname': 0,
    'country': 1,
    'taste': 2,
    'type': 3,
    'price': 4,
    'avoid': 5,
    'images': 6,
}



@app.post("/all")
def recommend_food(
    avoid: List[str] = Query([], description="Foods to avoid"),
    country: str = Query(None, description="Preferred country"),
    taste: str = Query(None, description="Preferred taste"),
    price: str = Query(None, description="Preferred price range"),
    food_type: str = Query(None, description="Preferred food type")
):
    try:
        user_criteria = {
            'avoid': avoid,
            'country': country,
            'taste': taste,
            'price': price,
            'type': food_type,
        }

        # Filter food based on user criteria
        recommended_food = filter_food_by_criteria(csv_data, user_criteria, header_mapping)

        # Extract relevant information for the response
        response_data = [
            {
                "foodname": food[header_mapping['foodname']],
                "price": food[header_mapping['price']],
                "type": food[header_mapping['type']],
                "country": food[header_mapping['country']],
                "images": food[header_mapping['images']],
            } for food in recommended_food
        ]

        return response_data

    except Exception as e:
        return {"error": str(e)}

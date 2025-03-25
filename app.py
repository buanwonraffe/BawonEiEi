from nicegui import ui
import json

# Load USDA Foundation JSON data
with open("foundationDownload.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def search_food(query):
    """Search for food item and return calorie info, considering variations."""
    found_foods = []
    
    for food in data["FoundationFoods"]:
        if query.lower() in food["description"].lower():
            # Extract calorie information (Energy) from the foodNutrients list
            calories = next(
                (nutrient["amount"] for nutrient in food["foodNutrients"]
                 if nutrient["nutrient"]["name"] == "Energy (Atwater General Factors)"), "N/A"
            )
            found_foods.append({
                "name": food["description"],
                "calories": calories,
                "food_details": food  # Store the entire food data for detailed view
            })
    
    return found_foods

def display_results():
    """Handle search and display more specific results."""
    query = search_box.value
    
    result = search_food(query)
    
    if result:
        result_label.set_text(f'Search Results: {len(result)} found')
        
        # Clear previous results before displaying new ones
        result_options.clear()
        
        # Create clickable options for each found food item
        for food in result:
            ui.button(f'{food["name"]} - {food["calories"]} kcal', 
                      on_click=lambda food=food: show_details(food)).classes('w-full')
    else:
        result_label.set_text("No results found.")

def show_details(food):
    """Show detailed information when a food item is clicked."""
    details = f"Name: {food['name']}\nCalories: {food['calories']} kcal\n"
    
    # Set the details text
    detail_label.set_text(details)

# UI Components
ui.label("🥗 USDA Calorie Tracker").classes("text-2xl font-bold")
search_box = ui.input("Enter food item...").classes("w-full")
ui.button("Search", on_click=display_results)

result_label = ui.label("").classes("text-lg mt-4")
result_options = ui.column().classes("mt-4")
detail_label = ui.label("").classes("text-lg mt-4")

ui.run(port=8080)
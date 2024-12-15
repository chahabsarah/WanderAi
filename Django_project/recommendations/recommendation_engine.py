# recommendation_engine.py
from voyages.models import Voyage
from datetime import date

class RecommendationEngine:
    @staticmethod
    def calculate_match_score(user_preferences, voyage):
        match_score = 0
        
        
        if user_preferences.travel_type.lower() == voyage.travel_type.lower()   and user_preferences.duration.lower() == voyage.duration.lower() and user_preferences.budget == voyage.prix:
            match_score += 100
            
       

        final_score = match_score
        return final_score

    @staticmethod
    def get_recommendations(user_preferences, max_recommendations=5):
        available_voyages = Voyage.objects.all()

        voyage_scores = []
        for voyage in available_voyages:
            score = RecommendationEngine.calculate_match_score(user_preferences, voyage)
            voyage_scores.append((voyage, score))


        recommended_voyages = [voyage_scores for voyage_scores, score in voyage_scores if score > 99.99  ][:max_recommendations]
        return recommended_voyages
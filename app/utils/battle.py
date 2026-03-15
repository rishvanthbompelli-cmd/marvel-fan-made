"""Battle probability calculator for character comparisons."""


# Weights for different stats
STAT_WEIGHTS = {
    'strength': 0.20,      # Physical power
    'speed': 0.15,         # Agility and reaction time
    'intelligence': 0.15,  # Strategic thinking
    'abilities': 0.20,     # Unique powers
    'combat': 0.15,       # Fighting skills
    'durability': 0.15    # Endurance and resistance
}


def calculate_win_probability(hero1_stats, hero2_stats):
    """
    Calculate the win probability between two characters based on their stats.
    
    Args:
        hero1_stats: Dictionary containing stats for hero 1
        hero2_stats: Dictionary containing stats for hero 2
        
    Returns:
        Dictionary with win probabilities for both heroes and detailed breakdown
    """
    if not hero1_stats or not hero2_stats:
        return {
            'hero1_probability': 50,
            'hero2_probability': 50,
            'breakdown': {},
            'factors': []
        }
    
    # Calculate weighted scores for each hero
    hero1_score = 0
    hero2_score = 0
    breakdown = {}
    factors = []
    
    for stat, weight in STAT_WEIGHTS.items():
        h1_value = hero1_stats.get(stat, 0)
        h2_value = hero2_stats.get(stat, 0)
        
        # Normalize values to 0-100 scale if needed
        h1_value = min(max(h1_value, 0), 100)
        h2_value = min(max(h2_value, 0), 100)
        
        # Calculate weighted contribution
        hero1_score += h1_value * weight
        hero2_score += h2_value * weight
        
        breakdown[stat] = {
            'hero1': h1_value,
            'hero2': h2_value,
            'weight': weight,
            'hero1_contribution': h1_value * weight,
            'hero2_contribution': h2_value * weight
        }
        
        # Determine factor advantage
        if h1_value > h2_value:
            factors.append({
                'stat': stat,
                'winner': 'hero1',
                'difference': h1_value - h2_value
            })
        elif h2_value > h1_value:
            factors.append({
                'stat': stat,
                'winner': 'hero2',
                'difference': h2_value - h1_value
            })
    
    # Calculate probabilities using sigmoid-like function
    total_score = hero1_score + hero2_score
    
    if total_score == 0:
        hero1_probability = 50
        hero2_probability = 50
    else:
        # Add small buffer to avoid division by zero and extreme probabilities
        buffer = 0.1
        hero1_probability = ((hero1_score / total_score) * 100 * (1 - buffer)) + buffer
        hero2_probability = 100 - hero1_probability
    
    # Sort factors by difference to show most impactful ones first
    factors.sort(key=lambda x: x['difference'], reverse=True)
    
    return {
        'hero1_probability': round(hero1_probability, 1),
        'hero2_probability': round(hero2_probability, 1),
        'hero1_score': round(hero1_score, 2),
        'hero2_score': round(hero2_score, 2),
        'breakdown': breakdown,
        'factors': factors[:6]  # Return top 6 factors
    }


def get_stat_percentages(hero1_stats, hero2_stats):
    """Get stat-by-stat comparison percentages."""
    if not hero1_stats or not hero2_stats:
        return {}
    
    percentages = {}
    
    for stat in STAT_WEIGHTS.keys():
        h1_value = hero1_stats.get(stat, 0)
        h2_value = hero2_stats.get(stat, 0)
        total = h1_value + h2_value
        
        if total == 0:
            percentages[stat] = {'hero1': 50, 'hero2': 50}
        else:
            percentages[stat] = {
                'hero1': round((h1_value / total) * 100, 1),
                'hero2': round((h2_value / total) * 100, 1)
            }
    
    return percentages


def get_overall_stats(characters_list):
    """Get overall stat averages for a list of characters."""
    if not characters_list:
        return {}
    
    total_stats = {
        'strength': 0,
        'speed': 0,
        'intelligence': 0,
        'abilities': 0,
        'combat': 0,
        'durability': 0
    }
    
    count = 0
    for character in characters_list:
        stats = character.get('stats', {})
        for stat in total_stats:
            total_stats[stat] += stats.get(stat, 0)
        count += 1
    
    if count > 0:
        return {stat: round(value / count, 1) for stat, value in total_stats.items()}
    
    return total_stats


def get_power_rankings(characters_list):
    """Get rankings of characters based on overall power score."""
    rankings = []
    
    for character in characters_list:
        stats = character.get('stats', {})
        
        # Calculate overall power score
        power_score = 0
        for stat, weight in STAT_WEIGHTS.items():
            power_score += stats.get(stat, 0) * weight
        
        rankings.append({
            'id': character.get('id'),
            'name': character.get('name'),
            'universe': character.get('universe'),
            'category': character.get('category'),
            'image': character.get('image'),
            'power_score': round(power_score, 2)
        })
    
    # Sort by power score descending
    rankings.sort(key=lambda x: x['power_score'], reverse=True)
    
    return rankings


def get_stat_labels():
    """Get human-readable labels for stats."""
    return {
        'strength': 'Strength',
        'speed': 'Speed',
        'intelligence': 'Intelligence',
        'abilities': 'Special Abilities',
        'combat': 'Combat Skills',
        'durability': 'Durability'
    }


def get_stat_descriptions():
    """Get descriptions for each stat."""
    return {
        'strength': 'Physical power and ability to exert force',
        'speed': 'Agility, reflexes, and movement speed',
        'intelligence': 'Strategic thinking and problem-solving',
        'abilities': 'Unique superhuman powers and abilities',
        'combat': 'Fighting techniques and experience',
        'durability': 'Resistance to damage and endurance'
    }

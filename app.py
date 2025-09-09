from flask import Flask, render_template, request, jsonify
import sys
import itertools

# Add src to path
sys.path.append('src')

app = Flask(__name__)

def basic_filter(combinations):
    """Apply basic filtering to combinations"""
    filtered = []
    for combo, combined in combinations:
        if (3 <= len(combined) <= 12 and combined.isalpha()):
            filtered.append((combo, combined))
    return filtered

def generate_combinations(words, max_length=4):
    """Generate word combinations"""
    all_combos = []
    
    for length in range(2, min(max_length + 1, len(words) + 1)):
        for combo in itertools.combinations(words, length):
            combined = ''.join(combo)
            all_combos.append((combo, combined))
        
        for combo in itertools.permutations(words, length):
            combined = ''.join(combo)
            all_combos.append((combo, combined))
    
    return all_combos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    words = [word.strip().lower() for word in data['words'].split() if word.strip()]
    max_length = int(data.get('max_length', 4))
    
    if len(words) < 2:
        return jsonify({'error': 'Please provide at least 2 words'})
    
    all_combos = generate_combinations(words, max_length)
    filtered = basic_filter(all_combos)
    
    # Remove duplicates
    seen = set()
    unique_results = []
    for combo, combined in filtered:
        if combined not in seen:
            seen.add(combined)
            unique_results.append({
                'combination': ' + '.join(combo),
                'result': combined,
                'length': len(combined)
            })
    
    return jsonify({
        'total_generated': len(all_combos),
        'filtered_count': len(filtered),
        'unique_count': len(unique_results),
        'results': unique_results[:50]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    portfolio_projects = [
        {"title": "Medical Data Visualizer", "link": "https://jerriward007.github.io/medical-data-visualizer/"},
        {"title": "Sea Level Predictor", "link": "https://jerriward007.github.io/sea-level-predictor/"},
        {"title": "Demographic Data Analyzer", "link": "https://jerriward007.github.io/demographic-data-analyzer-/"},
        {"title": "Mean Variance Std Dev Calculator", "link": "https://jerriward007.github.io/mean-variance-standard-deviation-calculator/"},
        {"title": "Appreciation Message Page", "link": "https://jerriward007.github.io/appreciation-message/"},
        {"title": "Estatiq Wears Survey Form", "link": "https://jerriward007.github.io/estatiq-wears-survey-form/"},
        {"title": "Estatiq Wears Homepage", "link": "https://jerriward007.github.io/estatiq-wears/"},
        {"title": "Time Series Visualizer", "link": "https://jerriward007.github.io/page-view-time-series-visualizer/"},
        {"title": "Technical Documentation Site", "link": "https://jerriward007.github.io/technical-documentation/"}
    ]
    return render_template("index.html", projects=portfolio_projects)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

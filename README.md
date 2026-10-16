# Political Spectrum Quiz

A Streamlit-based political spectrum quiz based on the **Datafolha/Folha de S.Paulo** methodology (2022). Discover your ideological positioning across three scales: Behavioral, Economic, and General.

## Features

- **16 questions** covering social, political, cultural, and economic values
- **Three scales** with Datafolha's exact methodology:
  - **Behavioral Scale** (10 questions, 0-10): Social values, civil liberties, law & order
  - **Economic Scale** (6 questions, 0-6): State intervention, taxes, labor rights, public services
  - **General Scale** (0-12): Weighted 50/50 combination of both scales
- **Five categories** per scale: Left, Center-left, Center, Center-right, Right
- **Bilingual**: Portuguese (default) and English
- **Visual results**: Horizontal gradient bars with positioned markers
- **Detailed explanations** for each classification
- **Methodology credits** to Datafolha/Folha de S.Paulo

## Methodology

Based on [Datafolha's ideological profiling method](https://www1.folha.uol.com.br/poder/2022/06/datafolha-desenvolveu-metodo-de-pontuacao-para-tracar-perfil-ideologico.shtml) (June 2022):

> "In 2013, Datafolha developed a methodology to understand the ideological profile of Brazilians based on a series of questions involving social, political, cultural, and economic values. The combination of the behavioral and economic thought scales resulted in a general ideological positioning scale."

### Scoring

| Scale | Questions | Range | Left | Center-left | Center | Center-right | Right |
|-------|-----------|-------|------|-------------|--------|--------------|-------|
| Behavioral | 10 | 0-10 | 8-10 | 6-7 | 5 | 3-4 | 0-2 |
| Economic | 6 | 0-6 | 5-6 | 4 | 3 | 2 | 0-1 |
| General | - | 0-12 | 9-12 | 7-8 | 6 | 4-5 | 0-3 |

General score = (Behavioral × 6/10) + Economic, rounded to nearest integer.

## Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone <repository-url>
cd spectrum-politic-quiz
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

### Run Tests

```bash
pytest -v
```

## Project Structure

```
spectrum-politic-quiz/
├── app.py                      # Entry point
├── requirements.txt
├── pytest.ini
├── README.md
├── .streamlit/config.toml      # Streamlit theme & server config
├── locales/
│   ├── pt_BR.json              # Portuguese translations
│   └── en_US.json              # English translations
├── src/
│   ├── core/
│   │   ├── questions.py        # Question definitions & thresholds
│   │   ├── scoring.py          # Pure scoring functions
│   │   └── i18n.py             # Internationalization
│   ├── ui/
│   │   ├── components.py       # Reusable UI components
│   │   ├── styles.py           # CSS injection
│   │   └── pages/
│   │       ├── welcome.py      # Landing page
│   │       ├── quiz.py         # Paginated quiz flow
│   │       └── results.py      # Results visualization
│   └── utils/
│       └── session.py          # Session state helpers
└── tests/
    ├── test_questions.py       # Question structure validation
    ├── test_scoring.py         # Scoring logic (100% coverage)
    ├── test_i18n.py            # Translation loading
    └── test_integration.py     # Full flow with mocked Streamlit
```

## Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → Select your repo → Branch: `main` → Main file: `app.py`
4. Deploy!

No additional configuration needed — `.streamlit/config.toml` handles theme and server settings.

## Customization

### Adding Languages

1. Create `locales/<lang_code>.json` with all keys from `pt_BR.json`
2. Translate all values
3. Language will appear in selector automatically

### Modifying Questions

Edit `src/core/questions.py`:
- Update `QUESTIONS` list with new question definitions
- Ensure `BEHAVIORAL_QUESTION_IDS` and `ECONOMIC_QUESTION_IDS` are correct
- Adjust thresholds if question count changes

### Changing Thresholds

Modify threshold dictionaries in `src/core/questions.py`:
- `BEHAVIORAL_THRESHOLDS`
- `ECONOMIC_THRESHOLDS`
- `GENERAL_THRESHOLDS`

Each maps classification → (min_score, max_score). All scores must be covered exactly once.

## License

This project implements the Datafolha methodology for educational purposes. The original methodology and questions are copyright of **Datafolha/Folha de S.Paulo**.

## Credits

- **Methodology**: Datafolha / Folha de S.Paulo (2022)
- **Original Test**: [Teste Esquerda-Direita-Centro](https://www1.folha.uol.com.br/poder/teste-esquerda-direita-centro/)
- **Methodology Article**: [Datafolha desenvolveu método de pontuação](https://www1.folha.uol.com.br/poder/2022/06/datafolha-desenvolveu-metodo-de-pontuacao-para-tracar-perfil-ideologico.shtml)
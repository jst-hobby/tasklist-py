# Tehtävälista

Yksinkertainen tehtävälista-sovellus, joka on toteutettu käyttäen FastAPI:a ja Supabase-tietokantaa.

Toteutuksessa on käytetty ainoastaan suomenkielistä sanelua. Ei koodausta (no code).

## Teknologiat

- Python 3.x
- FastAPI
- Supabase (PostgreSQL)
- Jinja2 Templates

## Asennus

1. Kloonaa repositorio:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Asenna riippuvuudet:
```bash
pip install fastapi uvicorn jinja2 python-multipart supabase python-dotenv
```

3. Luo `.env` tiedosto ja lisää Supabase-tunnukset:
```
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

4. Luo Supabase-tietokantaan tasks-taulu suorittamalla `create_tasks_table.sql` tiedoston sisältö Supabasen SQL-editorissa.

## Käynnistäminen

Käynnistä sovellus komennolla:
```bash
python main.py
```

Sovellus käynnistyy osoitteeseen http://localhost:8000

## Ominaisuudet

- Tehtävien listaus
- Uuden tehtävän lisääminen
- Tehtävän merkitseminen tehdyksi/tekemättömäksi
- Tehtävän poistaminen

## Tietokannan rakenne

Tasks-taulu sisältää seuraavat kentät:
- `id` (UUID): Tehtävän yksilöllinen tunniste
- `title` (TEXT): Tehtävän otsikko
- `completed` (BOOLEAN): Tehtävän tila (tehty/tekemätön)
- `created_at` (TIMESTAMP): Luomisaika
- `updated_at` (TIMESTAMP): Viimeisimmän päivityksen aika

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import load_json

profiles = load_json("data/profiles.json")
jobs = load_json("data/jobs.json")

model = SentenceTransformer("all-MiniLM-L6-v2")

job_desc = jobs[0]["description"]
job_embed = model.encode([job_desc])

results = []
for profile in profiles:
    text = profile["summary"] + " " + profile["experience"]
    embed = model.encode([text])
    sim = cosine_similarity(job_embed, embed)[0][0]
    results.append((profile["name"], sim))

results.sort(key=lambda x: x[1], reverse=True)
print("Top matches:")
for name, score in results:
    print(f"{name} - Score: {score:.3f}")

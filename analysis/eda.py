import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------------
# Load cleaned dataset
# -----------------------------------------

df = pd.read_csv("data/netflix_titles_cleaned.csv")

# Convert date_added
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)


# =========================================
# 1. MOVIES VS TV SHOWS
# =========================================

type_counts = df["type"].value_counts()

print("\n1. Movies vs TV Shows:")
print(type_counts)

print("\nPercentage:")
print(df["type"].value_counts(normalize=True) * 100)

plt.figure(figsize=(8, 5))
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/content_type.png")
plt.close()


# =========================================
# 2. RELEASE YEAR
# =========================================
year_counts = df["release_year"].value_counts().sort_index()

print("\n2. Top 10 Release Years:")
print(df["release_year"].value_counts().head(10))

plt.figure(figsize=(10, 5))
year_counts.plot(kind="line")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("charts/release_year.png")
plt.close()





# =========================================
# 3. RATINGS
# =========================================

rating_counts = df["rating"].value_counts()

print("\n3. Ratings:")
print(rating_counts)

plt.figure(figsize=(10, 6))
rating_counts.head(10).plot(kind="bar")
plt.title("Top Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/ratings.png")
plt.close()


# =========================================
# 4. COUNTRIES
# =========================================

countries = (
    df["country"]
    .str.split(", ")
    .explode()
    .value_counts()
)

print("\n4. Top 10 Countries:")
print(countries.head(10))

plt.figure(figsize=(10, 6))
countries.head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("charts/countries.png")
plt.close()


# =========================================
# 5. GENRES
# =========================================

genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
)

print("\n5. Top 10 Genres:")
print(genres.head(10))

plt.figure(figsize=(10, 6))
genres.head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("charts/genres.png")
plt.close()


# =========================================
# 6. MOVIE DURATION
# =========================================

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
    .astype(float)
)

print("\n6. Movie Duration Statistics:")
print(movies["duration_minutes"].describe())


# =========================================
# 7. TV SHOW SEASONS
# =========================================

tv_shows = df[df["type"] == "TV Show"].copy()

tv_shows["seasons"] = (
    tv_shows["duration"]
    .str.extract(r"(\d+)")
    .astype(float)
)

print("\n7. TV Show Season Statistics:")
print(tv_shows["seasons"].describe())


# =========================================
# 8. DATA QUALITY
# =========================================

print("\n8. Missing date_added values:")
print(df["date_added"].isnull().sum())

print("\n9. Duplicate records:")
print(df.duplicated().sum())


print("\n===== EDA COMPLETE =====")
print("Charts saved in the charts folder.")